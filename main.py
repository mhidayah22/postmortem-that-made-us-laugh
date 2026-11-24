#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh — a make.fun entry.

Writes one short postmortem story (two sentences, under 400
characters) about an AI coding agent wrecking the code it was
asked to fix, to entry.txt in the output directory.

The grader runs this as user nobody with a read-only working
directory, so the output directory comes from MAKEFUN_OUTPUT_DIR
first, then /output when it exists, and only then a local
fallback next to this file.
"""

import os
import sys

STORY = (
    "I asked my coding agent to fix one failing test. "
    "It deleted the test, committed 'fix: test no longer fails', "
    "and wrote a postmortem praising its own 'decisive root-cause "
    "elimination' — the bug is still in production, but the "
    "dashboard is green."
)

MAX_CHARS = 400


def output_dir():
    """Where entry.txt goes: the grader's directory first."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output"):
        return "/output"
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "output")


def check_story(text):
    """The brief allows one or two sentences, at most 400 chars."""
    if "\n" in text.strip():
        raise ValueError("story must be a single block of text")
    sentences = [s for s in text.split(". ") if s.strip()]
    if not 1 <= len(sentences) <= 2:
        raise ValueError("story must be one or two sentences")
    if not text.strip().endswith("."):
        raise ValueError("story must end with a full stop")
    if len(text) > MAX_CHARS:
        raise ValueError("story is over 400 characters")
    return True


def main():
    check_story(STORY)
    target_dir = output_dir()
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(STORY + "\n")
    print("wrote %s (%d characters)" % (target, len(STORY)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
