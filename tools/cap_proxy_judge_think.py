#!/usr/bin/env python3
"""cap_proxy 的 judge-think 变体（2026-10-09）：judge 的 thinking 由 disabled 改为 **enabled**。

与母本 tools/cap_proxy.py 的唯一区别 = judge 路由的 thinking 注入（其余逐字一致）：
  - judge（system 含 "Judge Prompt"）→ DeepSeek，**thinking=enabled**，cap 16384
  - 其余 → 本地 FP8（enable_thinking=False，cap 2048）
  - 独立 dump：runs/cap_proxy_judge_think_dump.jsonl

给"judge 开 think"的实验线（evo_r30_from_ask_anything）用；端口默认 18776。

母本原文：
---
给所有 chat/completions 请求注入 max_tokens 上限的本地代理。

用途：本地 FP8（OpenAI 兼容端点）在自由格式协议下会"跑飞"——一路生成几万 token 不停。
本代理把每次请求的 max_tokens 压到 CAP（默认 2048），把单次调用从分钟级压到 ~35 秒级。
只改 max_tokens 一个字段，其余（model/messages/temperature/返回值）原样透传。

额外上游路由（env EXTRA_UPSTREAMS，默认空 = 行为完全不变）：按请求里的 model 名把
指定模型转发到别的 OpenAI 兼容端点（含独立 key 文件），其余角色照旧分流。
形如  EXTRA_UPSTREAMS='{"gpt-6.1-sol": {"base": "https://rightapi.ai/v1",
                                       "key_file": "~/.rightapi_api_key", "cap": 4096}}'

用法:  python cap_proxy.py [port] [cap]
然后让客户端把 base_url 指向 http://127.0.0.1:<port>/v1
"""
import json
import os
import sys
import time
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

UPSTREAM = "http://gpu6:18764"  # 注意：客户端 base_url 已含 /v1，这里不要再加
JUDGE_UPSTREAM = "https://api.deepseek.com/v1/chat/completions"  # judge 角色改走远端
CAP = 2048
CAP_JUDGE = 16384  # judge 输出的是完整评分 JSON，需要更大空间
DS_KEY_PATH = os.path.expanduser("~/.deepseek_api_key")
# 额外上游路由：{"model名": {"base": "https://.../v1", "key_file": "~/.xxx", "cap": 4096}}
EXTRA_UPSTREAMS = json.loads(os.getenv("EXTRA_UPSTREAMS", "") or "{}")


def resolve_key_file(path: str) -> str:
    try:
        with open(os.path.expanduser(path), encoding="utf-8") as fh:
            return fh.read().strip()
    except Exception:
        return ""


def resolve_ds_key() -> str:
    key = (os.getenv("DS_REMOTE_KEY") or "").strip()
    if key:
        return key
    try:
        with open(DS_KEY_PATH, encoding="utf-8") as fh:
            return fh.read().strip()
    except Exception:
        return ""


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def _reply(self, code: int, data: bytes) -> None:
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):  # /v1/models 之类，直接透传
        try:
            req = urllib.request.Request(UPSTREAM + self.path)
            with urllib.request.urlopen(req, timeout=60) as r:
                self._reply(r.status, r.read())
        except Exception as exc:
            self._reply(502, json.dumps({"error": str(exc)}).encode())

    def do_POST(self):
        n = int(self.headers.get("Content-Length", 0) or 0)
        raw = self.rfile.read(n)
        route = "fp8"
        try:
            payload = json.loads(raw)
            # 1) 额外上游（env 门控）：按 model 名路由到远端端点（如 gpt-6.1-sol → rightapi）
            extra = EXTRA_UPSTREAMS.get(str(payload.get("model", "")))
            if extra:
                cap = int(extra.get("cap") or 0)
                prior = payload.get("max_tokens")
                if cap and (prior is None or prior > cap):
                    payload["max_tokens"] = cap
                upstream_url = str(extra["base"]).rstrip("/") + "/chat/completions"
                auth = "Bearer " + resolve_key_file(str(extra.get("key_file", "")))
                route = f"extra:{payload.get('model')}"
            else:
                # 2) 按角色分流：judge 的输出是一大坨 JSON（slot_scores/silent/stopping/summary），
                # 2048 会把 JSON 截断导致解析失败（实测连截 3 次直接崩 run）。其余角色沿用 CAP。
                sys_content = ""
                for m in payload.get("messages", []):
                    if m.get("role") == "system":
                        sys_content = str(m.get("content", ""))
                        break
                if "Judge Prompt" in sys_content:
                    # judge 走远端 deepseek-flash，**开 thinking**（本变体的唯一差异；母本为 disabled）
                    payload.setdefault("thinking", {"type": "enabled"})
                    upstream_url = JUDGE_UPSTREAM
                    auth = "Bearer " + resolve_ds_key()
                    route = "JUDGE->ds"
                    cap = CAP_JUDGE
                else:
                    # 本地 FP8：chat template 默认 enable_thinking=true（reasoning_effort 默认 xhigh），
                    # 会把输出全烧进 reasoning 字段、content 变成 null。调用方显式指定时不覆盖。
                    ctk = payload.setdefault("chat_template_kwargs", {})
                    if isinstance(ctk, dict):
                        ctk.setdefault("enable_thinking", False)
                    upstream_url = UPSTREAM + self.path
                    auth = self.headers.get("Authorization", "")
                    cap = CAP
                prior = payload.get("max_tokens")
                if prior is None or prior > cap:
                    payload["max_tokens"] = cap
            raw = json.dumps(payload).encode()
        except Exception:
            pass  # 非 JSON 就原样转发

        req = urllib.request.Request(
            upstream_url,
            data=raw,
            method="POST",
            headers={"Content-Type": "application/json", "Authorization": auth},
        )
        try:
            with open("runs/cap_proxy_judge_think_dump.jsonl", "a") as fh:
                fh.write(json.dumps({"t": time.time(), "req": payload}, ensure_ascii=False)[:4000] + "\n")
        except Exception:
            pass
        t0 = time.time()
        try:
            with urllib.request.urlopen(req, timeout=1800) as r:
                data = r.read()
            self._reply(200, data)
        except urllib.error.HTTPError as exc:
            data = exc.read()
            self._reply(exc.code, data)
        except Exception as exc:
            data = json.dumps({"error": f"proxy upstream failure: {exc}"}).encode()
            self._reply(502, data)

        try:
            d = json.loads(data)
            with open("runs/cap_proxy_judge_think_dump.jsonl", "a") as fh:
                fh.write(json.dumps({"t": time.time(), "resp": str((d.get("choices") or [{}])[0].get("message", {}).get("content"))[:1500]}, ensure_ascii=False) + "\n")
            u = d.get("usage", {}) or {}
            ch = (d.get("choices") or [{}])[0]
            print(
                f"[{time.strftime('%H:%M:%S')}] {route} {time.time() - t0:5.1f}s "
                f"prompt={u.get('prompt_tokens')} gen={u.get('completion_tokens')} "
                f"finish={ch.get('finish_reason')}",
                flush=True,
            )
        except Exception:
            pass

    def log_message(self, *args):  # 静音默认访问日志
        pass


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 18770
    CAP = int(sys.argv[2]) if len(sys.argv) > 2 else CAP
    print(f"cap proxy (judge-think): 127.0.0.1:{port} -> {UPSTREAM} (max_tokens<={CAP}) | judge->ds(thinking=enabled)", flush=True)
    if EXTRA_UPSTREAMS:
        for m, cfg in EXTRA_UPSTREAMS.items():
            print(f"  extra route: {m} -> {cfg.get('base')} (cap={cfg.get('cap')}, key={cfg.get('key_file')})", flush=True)
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()
