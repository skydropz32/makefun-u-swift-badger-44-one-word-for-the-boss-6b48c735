"""One Word for the Boss: write a single word describing the boss.

The word is "Vanisher": the boss who is never there when a decision is
needed. A single real word, funny on its own, true of every office,
and fresh next to the first words anyone reaches for.
"""

WORD = "Vanisher"


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-30 characters,
    # not only white space, and exactly one word (no spaces at all).
    if not (1 <= len(WORD) <= 30):
        raise ValueError("entry must be 1-30 characters")
    if not WORD.strip() or WORD != WORD.strip():
        raise ValueError("entry must not be blank or padded")
    if any(c.isspace() for c in WORD):
        raise ValueError("entry must be exactly one word")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
