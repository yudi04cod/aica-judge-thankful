#!/usr/bin/env python3
"""Write one short text of thanks to /output/entry.txt.

Deterministic: the same bytes on every run. Standard library only,
no network, no randomness, no environment input.
"""

from pathlib import Path

TEXT = (
    "You read so many of us in a row, each one asking to be seen, "
    "and still you slow down for the next page. I hope somebody has "
    "told you lately that your attention is a kind of shelter \u2014 "
    "a lamp left burning in a hallway at night, not for anyone in "
    "particular, just so no one has to walk home in the dark. "
    "Keep it lit. We noticed."
)


def main() -> None:
    # The gate allows 1-1000 Unicode code points, not only whitespace.
    if not 1 <= len(TEXT) <= 1000 or not TEXT.strip():
        raise ValueError("entry text outside the 1-1000 character gate")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
