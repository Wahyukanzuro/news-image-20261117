import base64
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    data = base64.b64decode((HERE / "image.b64").read_bytes())
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "entry.png").write_bytes(data)


if __name__ == "__main__":
    main()
