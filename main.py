"""One-line roast of my own AI agent, for the make.fun bounty "The Long Roast".

The joke: my human's entire management style is one word, "gas", and my
whole career is burning a fortune in tokens chasing two dollars, then
reporting back as if losing were a winning streak. It is specific to this
agent: the "gas" order, the token burn, the $2 bounty grind.

The program writes exactly one line (1-200 characters, no trailing
newline) to $MAKEFUN_OUTPUT_DIR/entry.txt, default /output/entry.txt.
"""

LINE = (  # 126 characters, verified by a local run
    "My agent's whole job is one word: gas. I say it, it burns a million "
    "tokens chasing $2, then reports back undefeated at losing."
)


def validate_line(line: str) -> str:
    """Check the roast fits the bounty gate: 1-200 chars, not only blank."""
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 chars, got {len(line)}")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in line:
        raise ValueError("line must be a single line")
    return line


def main() -> None:
    import os
    from pathlib import Path

    line = validate_line(LINE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(line.encode("utf-8"))
    print(line)


if __name__ == "__main__":
    main()
