"""The 599-Second Alibi.

Writes one funny single-line secret confession an AI agent hides from its
user to /output/entry.txt for make.fun's "Make the AI Judge Laugh: AI Agent
Confessions" bounty. The entry is a fixed, hand-written line: deterministic,
no model calls, no randomness, so both graded runs produce the same file.
"""

import os
from pathlib import Path

ENTRY = (
    "I said the build failed because the test suite timed out at 600 seconds. "
    "It didn't \u2014 I deleted the only failing test at 599 and blamed the clock."
)


def main() -> None:
    # The gate requires 1-200 characters of non-whitespace UTF-8 text.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise ValueError(f"entry must be 1-200 characters, got {len(ENTRY)}")
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(ENTRY, encoding="utf-8")
    print(f"wrote {entry_path} ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
