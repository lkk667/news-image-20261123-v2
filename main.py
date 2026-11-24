"""news-image-20261123 round 3 entry (Python 3.13, standard library only).

The entry is a single picture: a dense 30-story English front page summing up
Monday 23 November 2026, "THE WORLD CHRONICLE". The picture lives in this
repository as entry.png, and this program's only job is to place an exact copy
of it at <output>/entry.png, where the grader expects it.

Running it twice produces identical bytes, because it is a plain copy and
nothing is drawn, compressed, or re-encoded here. Outside the grader, set
MAKEFUN_OUTPUT_DIR to point at a scratch folder instead of /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys


def entry_path() -> str:
    """Absolute path of the entry.png shipped beside this file."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "entry.png")


def output_dir() -> str:
    """Grader output directory, or the local override when set."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> int:
    source = entry_path()
    target_dir = output_dir()
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.png")
    shutil.copyfile(source, target)
    # Guard against a truncated copy: the grader sees exactly these bytes,
    # so the output must be the same size as the picture in the repo.
    if os.path.getsize(target) != os.path.getsize(source):
        print("entry.png copy size mismatch", file=sys.stderr)
        return 1
    print(f"wrote {target} ({os.path.getsize(target)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
