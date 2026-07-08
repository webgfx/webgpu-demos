#!/usr/bin/env python3
"""Threaded, Range-capable static file server for the WebGPU demos.

Serve the whole project root so a demo page (e.g.
/webgpu-demos/demos/webgpu-ort-llm/index.html) can also reach models by an
absolute path (e.g. /agents/ai-models/Phi-4-mini-instruct/onnx-webgpu). Range
support is required for large model weight files.

Usage:
    python webgpu-demos/serve.py                 # serves D:\\workspace\\project on :8000
    python webgpu-demos/serve.py --root . --port 8000
"""
import argparse
import functools
import http.server
import os
import socketserver


class RangeHandler(http.server.SimpleHTTPRequestHandler):
    def send_head(self):
        # Fall back to the default (which handles full-file GET/HEAD) unless the
        # client asked for a byte range.
        rng = self.headers.get("Range")
        if not rng:
            return super().send_head()
        path = self.translate_path(self.path)
        if os.path.isdir(path):
            return super().send_head()
        try:
            f = open(path, "rb")
        except OSError:
            self.send_error(404, "File not found")
            return None
        try:
            fs = os.fstat(f.fileno())
            size = fs.st_size
            start, end = 0, size - 1
            unit, _, rangespec = rng.partition("=")
            if unit.strip() == "bytes" and "-" in rangespec:
                s, _, e = rangespec.partition("-")
                if s.strip():
                    start = int(s)
                if e.strip():
                    end = int(e)
            start = max(0, start)
            end = min(end, size - 1)
            if start > end:
                self.send_error(416, "Requested Range Not Satisfiable")
                f.close()
                return None
            self.send_response(206)
            ctype = self.guess_type(path)
            self.send_header("Content-Type", ctype)
            self.send_header("Accept-Ranges", "bytes")
            self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
            self.send_header("Content-Length", str(end - start + 1))
            self.end_headers()
            f.seek(start)
            self._range_remaining = end - start + 1
            return f
        except Exception:
            f.close()
            raise

    def copyfile(self, source, outputfile):
        remaining = getattr(self, "_range_remaining", None)
        if remaining is None:
            return super().copyfile(source, outputfile)
        while remaining > 0:
            chunk = source.read(min(1 << 20, remaining))
            if not chunk:
                break
            try:
                outputfile.write(chunk)
            except (BrokenPipeError, ConnectionAbortedError):
                return
            remaining -= len(chunk)


class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=r"D:\workspace\project",
                    help="directory to serve (default the project root)")
    ap.add_argument("--port", type=int, default=8000)
    args = ap.parse_args()
    handler = functools.partial(RangeHandler, directory=args.root)
    with ThreadingHTTPServer(("0.0.0.0", args.port), handler) as httpd:
        print(f"serving {args.root} on http://127.0.0.1:{args.port}")
        print("  Phi-4 demo: "
              f"http://127.0.0.1:{args.port}/webgpu-demos/demos/webgpu-ort-llm/?model=phi4")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
