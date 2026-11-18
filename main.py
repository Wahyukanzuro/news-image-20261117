"""Write the front-page image to the output directory.

The image bytes are stored base64-encoded in image.b64 next to this
file; this program only decodes them and writes them out, so both runs
produce identical bytes.
"""
import base64
import os
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "image.b64"


def output_path():
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"


def main():
    image = base64.b64decode(DATA_FILE.read_text().strip())
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(image)


if __name__ == "__main__":
    main()
