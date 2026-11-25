#!/usr/bin/env python3
"""Write the entry: one pickup line aimed at a robot or an AI.

The program writes a single line to /output/entry.txt. It is
deterministic: every run writes the same bytes.

The line is written to the brief: a joke pickup line for a machine,
grown from machine machinery (autocomplete finishing sentences) rather
than the worn battery/charging/reboot moves, with the punch in the
second half and a straight face throughout. It is 99 characters,
inside the 200 limit, and it is written with no trailing newline so
the file is exactly one line.
"""

import os

ENTRY = "Are you autocomplete? Because you finish my sentences, and I'd love it if you finished my life too."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
