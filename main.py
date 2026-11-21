#!/usr/bin/env python3
"""news-image-20261120 entrypoint: copy the shipped image to the output.

Stdlib only (os, shutil, sys) — the grader's sandbox has no PIL and no
system fonts, so this program must not import them. It copies entry.png
from this repository into $MAKEFUN_OUTPUT_DIR/entry.png (default
/output/entry.png). A pure copy is byte-identical on every run.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dst = os.path.join(out_dir, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)
    print("wrote", dst, os.path.getsize(dst), "bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
