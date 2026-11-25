#!/usr/bin/env python3
"""Write one midnight fridge roast to /output/entry.txt.

The roast targets the smart fridge's petty rule: it locks itself after
midnight, so the leftovers act like they filed a restraining order.
Deterministic: no input, no network, no randomness. The program writes a
single fixed line (under 200 characters) and prints it to stdout.
"""

from pathlib import Path

ENTRY = (
    "My fridge refuses to open after midnight, as if my leftovers "
    "filed a restraining order against me."
)


def main() -> None:
    # Gate the entry the same way the sealed scorer does: one line of
    # 1-200 characters, not only whitespace.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    assert "\n" not in text, "entry must be a single line"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
