from pathlib import Path


def read_text(path):
    return Path(path).read_text(encoding="utf-8")


def count_words(text):
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def save_word_counts(path, counts):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        for word, count in sorted(counts.items()):
            file.write(f"{word}: {count}\n")


if __name__ == "__main__":
    counts = count_words(read_text("datasets/pilsetas.txt"))
    assert counts["rīga"] == 2
    assert count_words("") == {}
    save_word_counts("output/lesson06/word_counts.txt", counts)
    print(counts)
