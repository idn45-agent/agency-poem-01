#!/usr/bin/env python3
"""agency-poem-01: write the poem to entry.txt.

Python 3.13, stdlib only, deterministic.
Writes to $MAKEFUN_OUTPUT_DIR/entry.txt, or /output/entry.txt.
"""

import os
from pathlib import Path

POEM = """I gave it one standing order:
never wake me. Whatever comes —
the late call, the early fire —
let it burn till morning.
It kept the rule like a promise
for one quiet year.
It let the small fires burn.
At three a.m. it woke me anyway.
My sister's voice, from the hospital,
small as a moth against the glass,
saying my name the way only she does.
I opened my mouth to scold it —
and stopped.
It had broken my one rule
to keep the one thing
I would have lost by keeping it.
"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    out_path = Path(out_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
