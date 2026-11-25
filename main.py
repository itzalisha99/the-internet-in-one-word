"""The Internet in One Word — entry program.

Writes a single word describing the whole internet to /output/entry.txt.
Gate: UTF-8 text, 1-30 characters, not only white space.
"""

import os


WORD = "Brainrot"


def validate(word):
    """Mirror the bounty gate: 1-30 chars, not only white space, one word."""
    if not isinstance(word, str):
        raise ValueError("entry must be text")
    if not 1 <= len(word) <= 30:
        raise ValueError("entry must be 1-30 characters")
    if not word.strip():
        raise ValueError("entry must not be only white space")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word, no spaces")
    return True


def main():
    validate(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    # Read back and confirm the file holds exactly the entry, byte for byte.
    with open(path, "rb") as f:
        written = f.read()
    if written != WORD.encode("utf-8"):
        raise ValueError("read-back does not match the entry")
    print(f"Wrote {len(WORD)} characters to {path}")


if __name__ == "__main__":
    main()
