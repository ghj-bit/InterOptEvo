#!/usr/bin/env python3
"""cap_proxy 的专用变体：把「执行 agent = deepseek-flash」的请求也路由到远端 DeepSeek。

与 tools/cap_proxy.py 的唯一区别是路由顺序（原文件保持不动）：
  1) system prompt 含 "Judge Prompt"        -> DeepSeek（关 thinking，cap 16384）← 必须先判 judge
  2) model 名 == "deepseek-flash"（agent 角色）-> DeepSeek（关 thinking，cap 与 FP8 臂对齐 2048）
  3) 其余（user simulator / detector）      -> 本地 FP8（chat template 关 thinking，cap 2048）

用法: python cap_proxy_dsagent.py [port] [cap]
"""
import json
import os
import sys
import time
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

UPSTREAM = "http://gpu6:18764"  # 注意：客户端 base_url 已含 /v1，这里不要再加
DS_UPSTREAM = "https://api.deepseek.com/v1/chat/completions"
CAP = 2048
CAP_JUDGE = 16384
CAP_DS_AGENT = 2048
DS_KEY_PATH = os.path.expanduser("~/.deepseek_api_key")
DUMP_PATH = "runs/test50_eval/cap_proxy_dsagent_dump.jsonl"


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

    def do_GET(self):  # /v1/models 之类，透传
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
        payload = {}
        upstream_url = UPSTREAM + self.path
        auth = self.headers.get("Authorization", "")
        cap = CAP
        try:
            payload = json.loads(raw)
            sys_content = ""
            for m in payload.get("messages", []):
                if m.get("role") == "system":
                    sys_content = str(m.get("content", ""))
                    break
            if "Judge Prompt" in sys_content:
                # 1) judge：远端 deepseek-flash，关 thinking，放宽 cap（评分 JSON 大）
                payload.setdefault("thinking", {"type": "disabled"})
                upstream_url = DS_UPSTREAM
                auth = "Bearer " + resolve_ds_key()
                route = "JUDGE->ds"
                cap = CAP_JUDGE
            elif str(payload.get("model", "")) == "deepseek-flash":
                # 2) 执行 agent（本变体的目的）：远端 deepseek-flash，关 thinking，cap 与 FP8 臂对齐
                payload.setdefault("thinking", {"type": "disabled"})
                upstream_url = DS_UPSTREAM
                auth = "Bearer " + resolve_ds_key()
                route = "AGENT->ds"
                cap = CAP_DS_AGENT
            else:
                # 3) 本地 FP8：chat template 默认 enable_thinking=true，显式关掉
                ctk = payload.setdefault("chat_template_kwargs", {})
                if isinstance(ctk, dict):
                    ctk.setdefault("enable_thinking", False)
                route = "fp8"
                cap = CAP
            prior = payload.get("max_tokens")
            if prior is None or prior > cap:
                payload["max_tokens"] = cap
            raw = json.dumps(payload).encode()
        except Exception:
            pass  # 非 JSON 就原样转发

        req = urllib.request.Request(
            upstream_url, data=raw, method="POST",
            headers={"Content-Type": "application/json", "Authorization": auth},
        )
        try:
            os.makedirs(os.path.dirname(DUMP_PATH), exist_ok=True)
            with open(DUMP_PATH, "a") as fh:
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

    def log_message(self, *args):  # 静音访问日志
        pass


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 18772
    if len(sys.argv) > 2:
        CAP = CAP_DS_AGENT = int(sys.argv[2])
    print(f"cap proxy (dsagent): 127.0.0.1:{port} | judge->ds(16384) | agent(deepseek-flash)->ds({CAP_DS_AGENT}) | 其余->{UPSTREAM}({CAP})", flush=True)
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()
