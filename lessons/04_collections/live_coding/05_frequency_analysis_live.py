"""Biežuma algoritms: no teksta līdz atslēgu un skaitu vārdnīcai."""
text = "Rīga Python Rīga dators Python Rīga"
words = text.lower().split()
print(words)
counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
    print(word, "->", counts)  # Vārdnīcas stāvoklis katrā solī.

short_counts = {}
for word in words:
    short_counts[word] = short_counts.get(word, 0) + 1
print(short_counts)
assert counts == short_counts
print("Vārdu skaits:", len(words), "unikālie:", len(counts))
print("Pārbaude:", sum(counts.values()) == len(words))

# Papildus: simbolu biežums un vienkārša pieturzīmju tīrīšana.
characters = {}
for char in text.lower():
    if not char.isspace():
        characters[char] = characters.get(char, 0) + 1
print(characters)
clean_counts = {}
for word in "Rīga, Rīga! Python.".lower().split():
    word = word.strip(".,!?;:")
    if word:
        clean_counts[word] = clean_counts.get(word, 0) + 1
print(clean_counts)

# Papildus: biežākais vārds; vienāda skaita gadījumā pirmais ievietotais.
best_word = None
best_count = 0
for word, count in counts.items():
    if count > best_count:
        best_word, best_count = word, count
print(best_word, best_count)
# Izmēģini text = "" un "a b".
