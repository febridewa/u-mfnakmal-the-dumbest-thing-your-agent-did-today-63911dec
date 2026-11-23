#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today.

Writes one line about the dumbest thing my agent did today to
/output/entry.txt. Deterministic: the same line on every run.
"""

import os

LINE = "My agent spent forty minutes debugging a typo in a file it deleted in minute two, then announced the refactor was complete."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
