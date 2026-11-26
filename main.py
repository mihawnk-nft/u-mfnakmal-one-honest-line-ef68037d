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


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
