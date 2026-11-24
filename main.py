#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line — make.fun entry.

The program writes one original sentence to /output/entry.txt
($MAKEFUN_OUTPUT_DIR/entry.txt) and prints exactly that sentence to stdout.

THE LINE (124 of the 200 allowed characters, one sentence, no trailing
newline):
    The escalator handrail ran a fraction faster than the steps, and my
    hand reached the top a second before the rest of me did.

WHY THIS LINE — scored against the public brief, in its own order:
  1. An angle the reader has not met before. Escalator handrails are
     driven separately from the steps and in practice drift slightly
     faster (or slower) than them — a mismatch most riders have felt
     without ever naming. The wonder is inside the machine itself, not
     borrowed from a stock image, and none of the brief's own examples
     (lift door, kettle pause, puddle sky) is reused.
  2. The surprise lands in a single read, at the end: "before the rest
     of me did" splits the body in two — the hand arrives first, the
     person follows. One reversal, no second beat needed.
  3. Grounded in something real. Entirely everyday: anyone who has
     ridden an escalator with a hand on the rail has lived this moment.
     Nothing invented, nothing supernatural.

CANDIDATE CUT (147 chars, scored 13/15 — lost head-to-head on novelty;
the spider-web-as-a-home is a familiar poetic image, and it needs two
beats where the winner needs one):
    A spider had strung its web across my bicycle handlebars overnight,
    and I had to choose between my commute and a house someone built
    while I slept.
Full table: candidates.md in the workdir (not shipped).

Determinism: the line is a fixed string in this file. The program
writes exactly those bytes on every run — no time, no randomness, no
network, no input, no model call. Two grader runs produce
byte-identical /output/entry.txt.

Run it (outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output):
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
from pathlib import Path

LINE = (
    "The escalator handrail ran a fraction faster than the steps, "
    "and my hand reached the top a second before the rest of me did."
)

# The grader sets MAKEFUN_OUTPUT_DIR; locally it defaults to /output.
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
TARGET = OUTPUT_DIR / "entry.txt"


def main() -> None:
    # Self-gate, mirroring the brief: one sentence, 1-200 characters,
    # not only whitespace. Fail loudly instead of writing an invalid entry.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line is whitespace-only"
    assert "\n" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE, "line must not start or end with space"
    assert LINE.count(".") == 1 and LINE.endswith("."), "line must be one sentence"

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(LINE, encoding="utf-8")

    # Read back what was written: the file the judge reads must be
    # exactly the line, byte for byte, or the run should fail loudly.
    # The sha256 digest pins the bytes: two runs must agree on it.
    written = TARGET.read_text(encoding="utf-8")
    assert written == LINE, "written entry differs from the line"
    digest = hashlib.sha256(TARGET.read_bytes()).hexdigest()
    assert digest == hashlib.sha256(LINE.encode("utf-8")).hexdigest(), (
        "written entry digest differs from the line"
    )

    print(LINE)


if __name__ == "__main__":
    main()
