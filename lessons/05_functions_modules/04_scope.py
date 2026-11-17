"""5. nodarbība: lokālie mainīgie un funkciju savienošana."""

city = "Rīga"


def show_local_city():
    city = "Liepāja"  # Lokālais mainīgais; ārējo city nemaina.
    return city


def count_words(text):
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def count_unique_words(text):
    counts = count_words(text)  # Viena funkcija izmanto otru.
    return len(counts)


print("Funkcijas city:", show_local_city())
print("Ārējais city:", city)
print("Dažādi vārdi:", count_unique_words("Rīga Python Rīga"))
