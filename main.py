#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog (make.fun).

Writes the entry -- one line, a terse release note for a bug in
everyday human behaviour -- to /output/entry.txt, where the sealed
scorer reads it.
"""

import os

TEXT = "v3.0.2: fixed a bug where yawning in a meeting silently notified every colleague that you were bored."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
