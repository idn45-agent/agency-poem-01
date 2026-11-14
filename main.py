"""agency-poem-01: write one short poem about agency to the output file.

Deterministic, standard library only, no network. The poem lives here as a
single string and is written out byte for byte.
"""

import os

POEM = """\
My agent wrote in my hand for a year —
cards, condolences, apologies —
better than I did, and kinder.
One morning I picked up a pen
and my own signature looked forged.
Now I write the hard ones myself,
badly, in blotting ink:
a hand that has not forgotten how.
"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(POEM)


if __name__ == "__main__":
    main()
