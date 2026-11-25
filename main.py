#!/usr/bin/env python3
"""Midnight Fridge Roast: one line, funniest takes top.

Writes a single roast line (at most 200 characters) about a smart
fridge that refuses to open after midnight to /output/entry.txt.
Python 3.13 standard library only; fully deterministic: no
randomness, no clock, no network.
"""

import os

ROAST = (
    "My fridge locks at midnight, flashes its light like a bouncer "
    "checking ID, then hums a lullaby so the leftovers can get their "
    "beauty sleep."
)


def main() -> None:
    # The house gate: /output/entry.txt must be UTF-8 text of 1 to
    # 200 characters, not only white space. Refuse to write a line
    # that would fail it rather than shipping an invalid entry.
    if not 1 <= len(ROAST) <= 200 or not ROAST.strip():
        raise SystemExit("roast line fails the 1-200 character gate")
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Exactly the line, no trailing newline: fewer bytes wins ties,
    # and the gate counts every character in the file.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
