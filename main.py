"""Real-Life Patch Notes entry.

Writes a single-line software patch note for a bug in human biology
to /output/entry.txt. Pure standard library, no I/O outside the output
path, no network.
"""

import os

LINE = "v3.3.1: fixed a bug where the leg fell asleep 30 seconds before the user had to stand up."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
