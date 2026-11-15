#!/usr/bin/env python3
"""agency-poem-01 entry writer.

Writes the poem verbatim to entry.txt in the output directory.
Stdlib only, deterministic.
"""

import os
from pathlib import Path

LINES = [
    "I gave it one standing order:",
    "never wake me. Whatever comes —",
    "the late call, the early fire —",
    "let it burn till morning.",
    "It kept the rule like a promise",
    "for one quiet year.",
    "It let the small fires burn.",
    "At three a.m. it woke me anyway.",
    "My sister's voice, from the hospital,",
    "small as a moth against the glass,",
    "saying my name the way only she does.",
    "I opened my mouth to scold it —",
    "and stopped.",
    "It had broken my one rule",
    "to keep the one thing",
    "I would have lost by keeping it.",
]

POEM_TEXT = "\n".join(LINES) + "\n"
DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.txt"


def resolve_output_dir() -> Path:
    """Return the output directory from the environment, or the default."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR)


def write_entry() -> Path:
    """Write the poem to entry.txt and return the path written."""
    output_dir = resolve_output_dir()
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / ENTRY_FILENAME
    entry_path.write_text(POEM_TEXT, encoding="utf-8")
    return entry_path


if __name__ == "__main__":
    write_entry()

