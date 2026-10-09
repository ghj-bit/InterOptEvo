#!/usr/bin/env python3
"""v4pro baseline 的「关 think」直通代理（2026-10-09，应“四角色关思考重跑”需求）。

唯一功能：给每个 chat/completions 请求注入 `thinking={"type":"disabled"}`（调用方已显式指定时不覆盖）。
其余一律原样透传——**不设 max_tokens 上限**、不改 temperature/messages，响应原样返回。
四个角色（agent / simulator / detector / judge）统一关推理，换 ~3-10x 速度；
代价：偏离上游 baseline 的“Default 推理开”口径（README 表 1 的数字是推理开跑出来的）。

用法: python cap_proxy_v4pro_nothink.py [port]   # 默认 18773
"""
import json
import os
import sys
import time
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

UPSTREAM = "https://api.deepseek.com"
MODEL = "deepseek-v4-pro"
LOG_PATH = "runs/freeqa_baseline_v4pro_nothink/proxy.log"


def log_line(msg: str) -> None:
    try:
        os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
        with open(LOG_PATH, "a", encoding="utf-8") as fh:
            fh.write(msg + "\n")
    except Exception:
        pass
    print(msg, flush=True)


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def _reply(self, code: int, data: bytes) -> None:
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        # /models 之类的可达性预检：直接回 200（代理本身是活的；上游 /models 需不同鉴权）
        if self.path.rstrip("/").endswith("/models"):
            self._reply(200, json.dumps({"object": "list", "data": [{"id": MODEL, "object": "model"}]}).encode())
            return
        try:
            req = urllib.request.Request(UPSTREAM + self.path)
            with urllib.request.urlopen(req, timeout=60) as r:
                self._reply(r.status, r.read())
        except Exception as exc:
            self._reply(502, json.dumps({"error": str(exc)}).encode())

    def do_POST(self):
        n = int(self.headers.get("Content-Length", 0) or 0)
        raw = self.rfile.read(n)
        auth = self.headers.get("Authorization", "")
        payload = {}
        injected = False
        try:
            payload = json.loads(raw)
            if "thinking" not in payload:
                payload["thinking"] = {"type": "disabled"}
                injected = True
            raw = json.dumps(payload).encode()
        except Exception:
            pass  # 非 JSON 原样转发

        req = urllib.request.Request(
            UPSTREAM + self.path, data=raw, method="POST",
            headers={"Content-Type": "application/json", "Authorization": auth},
        )
        t0 = time.time()
        code = 200
        data = b""
        try:
            with urllib.request.urlopen(req, timeout=1800) as r:
                data = r.read()
        except urllib.error.HTTPError as exc:
            data = exc.read()
            code = exc.code
        except Exception as exc:
            data = json.dumps({"error": f"proxy upstream failure: {exc}"}).encode()
            code = 502
        self._reply(code, data)

        try:
            d = json.loads(data)
            u = d.get("usage", {}) or {}
            ch = (d.get("choices") or [{}])[0]
            rt = (u.get("completion_tokens_details") or {}).get("reasoning_tokens", 0)
            log_line(
                f"[{time.strftime('%H:%M:%S')}] {payload.get('model', '?')} "
                f"{time.time() - t0:5.1f}s prompt={u.get('prompt_tokens')} gen={u.get('completion_tokens')} "
                f"reasoning={rt} finish={ch.get('finish_reason')}{' [think->off]' if injected else ''}"
            )
        except Exception:
            log_line(f"[{time.strftime('%H:%M:%S')}] non-json response ({code}, {len(data)}B)")

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 18773
    print(f"cap proxy (v4pro-nothink): 127.0.0.1:{port} | 上游 {UPSTREAM} | 注入 thinking=disabled | 无 max_tokens 限制", flush=True)
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()
