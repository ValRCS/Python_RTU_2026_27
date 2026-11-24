"""Tvērums, funkciju kompozīcija un atkļūdotāja demonstrācija."""

city = "Rīga"


def local_city():
    city = "Liepāja"
    return city


def count_words(text):
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def count_unique_words(text):
    counts = count_words(text)  # Step Into: vēro lokālos mainīgos.
    return len(counts)         # Step Out: vēro atgriezto vērtību.


print(local_city(), city)
result = count_unique_words("Rīga Python Rīga")
print(result)
assert result == 2
# VS Code: breakpoint uz result rindas, F5, F11 (Step Into),
# F10 (Step Over), Shift+F11 (Step Out). Apskati Call Stack un Variables.
