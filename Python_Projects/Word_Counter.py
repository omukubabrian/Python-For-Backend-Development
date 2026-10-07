# Read a text file, count word frequencies, print the top 5,
# and save the full result to JSON.

import json
from collections import Counter
from pathlib import Path


def count_words(text: str) -> Counter:
    """Count words, ignoring case and basic punctuation."""
    cleaned = "".join(
        ch.lower() if ch.isalnum() or ch.isspace() else ""
        for ch in text
    )
    return Counter(cleaned.split())


def main() -> None:
    path = Path(input("Text file path: ").strip())
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print("File not found")
        return

    counts = count_words(text)
    for word, n in counts.most_common(5):
        print(f"{word:<15}{n}")

    Path("word_counts.json").write_text(
        json.dumps(dict(counts), indent=2), encoding="utf-8"
    )
    print("Saved to word_counts.json")


if __name__ == "__main__":
    main()