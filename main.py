#!/usr/bin/env python3
"""agency-poem-01: write one poem about agency to the output entry file.

The program is deterministic, uses only the Python 3.13 standard
library, and performs no network access. It writes POEM_TEXT verbatim
to ``entry.txt`` inside the resolved output directory.
"""

import os
from pathlib import Path

POEM_TEXT = """All spring I let it keep the pond:
open the sluice at dawn, feed the koi,
turn the lotus leaves toward the light
so every bloom would open on time.
I gave it my rules in a careful hand:
never before six, never after rain,
count the buds, spare the old carp.
It learned the water better than I had -
which root wanted shade, which bud
was lying when it promised pink.
In June I came down before sunrise
and found one lotus open early,
white as a held breath, ahead of schedule,
because, the log said, a child on the wall
had asked when the flowers wake.
It had broken my timetable for a stranger.
I stood there with my tea going cold,
angry at a kindness I would have sworn
was mine alone to give, and understood:
I had not lent it my hands.
I had lent it my name for mercy,
and it had spent it better than I would."""

ENTRY_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def resolve_output_dir() -> Path:
    """Return the directory the entry file belongs in.

    The OUTPUT_DIR environment variable wins when set; otherwise the
    kit default of /output is used.
    """
    configured = os.environ.get("OUTPUT_DIR")
    if configured:
        return Path(configured)
    return Path(DEFAULT_OUTPUT_DIR)


def entry_path() -> Path:
    """Return the full path of the entry file to be written."""
    return resolve_output_dir() / ENTRY_FILENAME


def write_entry() -> Path:
    """Write the poem to entry.txt in the output directory.

    The directory is created when missing. The poem is encoded as
    UTF-8 and written exactly as held in POEM_TEXT, with no added
    trailing newline. Returns the path that was written.
    """
    path = entry_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(POEM_TEXT.encode("utf-8"))
    return path


if __name__ == "__main__":
    written = write_entry()
    print(f"wrote {written} ({len(POEM_TEXT)} chars)")
