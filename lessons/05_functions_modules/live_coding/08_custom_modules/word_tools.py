"""Atkārtoti izmantojami teksta apstrādes rīki."""

def count_words(text):
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def unique_word_count(text):
    return len(count_words(text))


if __name__ == "__main__":
    print(count_words("Rīga rīga"))
