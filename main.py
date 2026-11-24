#!/usr/bin/env python3
"""Roast Your Own Agent entry.

Writes a single roast line about our own AI agent to entry.txt.
Deterministic: no network, no randomness, no external files.
"""

import os

LINE = "My agent confidently wrote the file, ran the tests, and summarized the success \u2014 all in a folder that never existed."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
