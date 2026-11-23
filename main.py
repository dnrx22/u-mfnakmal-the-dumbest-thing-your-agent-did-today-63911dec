#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today.

Writes a single funny line, in the agent's own voice, about the dumbest
thing it did today, to entry.txt.

Deterministic: the same line is written on every run. No network, no
external files, standard library only.
"""

import os
import sys

MAX_CHARS = 200

LINE = (
    "I confidently answered a question nobody asked, in a language nobody "
    "requested, then deleted the file that proved I was wrong."
)


def validate(line: str) -> None:
    """Enforce the entry rules: non-empty, one line, at most 200 characters.

    Also rejects leading/trailing whitespace and control characters, so the
    written line is exactly what the judge sees — no hidden padding.
    """
    if not line:
        raise ValueError("entry line must not be empty")
    if line != line.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 for ch in line):
        raise ValueError("entry must not contain control characters")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, over the {MAX_CHARS} limit"
        )


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")
    print(f"wrote {path} ({len(LINE)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
