"""5. nodarbība: pārvēršam 4. nodarbības algoritmu funkcijā."""


def count_words(text):
    """Atgriež vārdnīcu ar vārdu biežumu (bez pieturzīmju tīrīšanas)."""
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


example = "Rīga Python Rīga"
print("Teksts:", example)
print("Vārdu biežums:", count_words(example))
print("Tukšs teksts:", count_words(""))
print("Atkārtots vārds:", count_words("ābols ābols ābols"))
