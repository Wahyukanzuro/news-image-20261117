#!/usr/bin/env python3
"""Entry point for the news-image-20261117 make.fun submission.

Decodes the bundled base64 image (image.b64, stored next to this file)
and writes it to /output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png).
Standard library only. Deterministic: the same input always produces
the same output bytes. The bundled image is a 1024x1024 JPEG.
"""

import base64
import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "image.b64")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    out_path = os.path.join(out_dir, "entry.png")
    with open(src, "r", encoding="ascii") as f:
        data = base64.b64decode(f.read(), validate=True)
    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "wb") as f:
        f.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
