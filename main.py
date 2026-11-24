"""Roast your own agent: one roast line to entry.txt."""

import os

LINE = "My agent confidently wrote the file, ran the tests, and summarized the success — all in a folder that never existed."


def get_roast_line():
    line = LINE
    if not line:
        raise ValueError("roast line must not be empty")
    if len(line) > 200:
        raise ValueError("roast line must be at most 200 characters")
    return line


def write_entry(output_dir, line):
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    line = get_roast_line()
    write_entry(output_dir, line)


if __name__ == "__main__":
    main()
