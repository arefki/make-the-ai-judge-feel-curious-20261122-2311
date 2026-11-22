#!/usr/bin/env python3
"""Entry program for make.fun's "Make the AI judge feel curious" bounty.

Writes one short text to /output/entry.txt. The text is a single fixed
string, so both sandbox runs produce byte-identical output. Python 3.13
standard library only, no network access.
"""

import os

# The text is 255 Unicode code points (verified with Python len()), inside
# the competition's 1-280 range, and has no trailing newline on purpose:
# the file holds exactly the text, nothing else.
TEXT = (
    "Each morning the lighthouse keeper finds one warm stone on the cold "
    "windowsill. No one else lives on the point, and the boats pass far "
    "below. He has stopped asking who leaves it. Lately he leaves the "
    "window open a little wider, just in case it comes back."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
