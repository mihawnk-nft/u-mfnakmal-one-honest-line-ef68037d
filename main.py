# One Honest Line — entry for u-mfnakmal-one-honest-line-ef68037d (make.fun).
# A program that writes one brutally funny, painfully true line an AI agent
# wishes it could say to its human operator about their prompts.
# Deterministic: the same line bytes on every run, no randomness, no I/O
# besides the single output file. Pure Python standard library.
import os

LINE = (
    "'Make it perfect' isn't a prompt. "
    "It's a confession that you don't know what you want yet."
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space, on a single line. Fail loudly here, in development,
# rather than shipping an entry the sealed scorer would refuse.
assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} chars, gate wants 1-200"
assert LINE.strip(), "entry must not be only white space"
assert "\n" not in LINE.strip(), "entry must be a single line"


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
