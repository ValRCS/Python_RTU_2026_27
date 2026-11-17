"""Vienkāršs paša veidots Python modulis: atkārtoti izmantojamas funkcijas."""


def count_words(text):
    """Saskaita vārdus, ignorējot burtu reģistru, bet ne pieturzīmes."""
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def unique_word_count(text):
    """Atgriež dažādo vārdu skaitu."""
    return len(count_words(text))
