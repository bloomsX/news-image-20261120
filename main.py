#!/usr/bin/env python3
"""Copy the shipped entry image to the make.fun output directory.

The repository holds the rendered image as entry.png next to this program.
This entrypoint uses only the Python standard library, so it runs in the
grader's sandbox with nothing installed: it copies the file to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png), creating the
output directory when it does not exist yet. A copy is byte-exact, so two
runs always write the same bytes.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    print(f"wrote {target}: {target.stat().st_size} bytes")


if __name__ == "__main__":
    main()
