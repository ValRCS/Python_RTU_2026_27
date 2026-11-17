"""5. nodarbība: pārbaudes ar assert (bez papildu pakotnēm)."""


def count_words(text):
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


assert count_words("") == {}
assert count_words("Python") == {"python": 1}
assert count_words("Rīga rīga") == {"rīga": 2}
assert count_words("Rīga Python Rīga") == {"rīga": 2, "python": 1}

print("Visas četras pārbaudes ir izturētas.")

# Izmēģini atsevišķi: assert count_words("a a") == {"a": 1}
# Tas izraisīs AssertionError, jo pareizā vērtība ir {"a": 2}.
# assert domāts izstrādes pārbaudēm, ne lietotāja ievades validēšanai.
