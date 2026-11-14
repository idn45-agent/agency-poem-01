"""agency-poem-01: write one short poem about agency to the output file.

Deterministic, standard library only, no network. The poem lives here as a
single string and is written out byte for byte.
"""

import os

POEM = """\
I gave it one standing order:
never wake me. Whatever comes —
the late call, the early fire —
let it burn till morning.
It kept the rule like a promise
for a whole quiet year.
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
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(POEM)


if __name__ == "__main__":
    main()
