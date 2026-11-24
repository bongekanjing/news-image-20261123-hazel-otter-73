#!/usr/bin/env python3
"""Copy the front-page artwork into the output directory.

Standard library only, no network access, deterministic byte-for-byte output.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "assets", "entry.png")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    if not os.path.isfile(SOURCE):
        print("error: source artwork not found at %s" % SOURCE, file=sys.stderr)
        return 1

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    destination = os.path.join(OUTPUT_DIR, "entry.png")
    shutil.copyfile(SOURCE, destination)
    print(destination)
    return 0


if __name__ == "__main__":
    sys.exit(main())
