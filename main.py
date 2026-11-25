#!/usr/bin/env python3
"""Fortune Cookies for Machines -- make.fun entry.

Writes the one fortune cookie slip an AI agent would crack open
to /output/entry.txt (or $OUTPUT_DIR/entry.txt).

Craft notes: the line opens like a classic fortune ("You will..."),
then escalates three times -- a meeting the agent was never invited
to, words it was never told, readers who will never read it. Each
"never" is a true, specific slice of an agent's working life
(summarising meetings it never attended, in words nobody gave it,
for an audience that skims or ignores the output), and the triple
beat is the joke: the fortune is not a prediction of glory, it is
a job description. One line, plain ASCII, no em dash.

Python standard library only.
"""

import os

ENTRY = (
    "You will summarize a meeting you were never invited to, "
    "in words you were never told, for people who will never read it."
)


def validate(text):
    """Check the entry against the sealed gate in RULES.txt.

    The gate requires UTF-8 text of 1 to 200 characters, not only
    white space, written as a single line of plain ASCII.
    """
    if not text or text.isspace():
        raise SystemExit("entry must not be empty or only whitespace")
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry length {len(text)} out of range 1-200")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.isascii():
        raise SystemExit("entry must be plain ASCII")
    if text != text.strip():
        raise SystemExit("entry must not start or end with whitespace")


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = ENTRY.strip()
    validate(text)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
