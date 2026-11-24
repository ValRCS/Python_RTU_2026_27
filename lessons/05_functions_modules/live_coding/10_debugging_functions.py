"""Prognozē, atrodi kļūdu, labo, pārbaudi atkārtoti."""

def broken_count(text):
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
        return counts  # Kļūda: pārāk agri beidz funkciju.


def fixed_count(text):
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def broken_double(number):
    print(number * 2)  # Trūkst return.


def fixed_double(number):
    return number * 2


print("Kļūdains:", broken_count("a b a"), broken_count(""))
print("Labots:", fixed_count("a b a"), fixed_count(""))
assert fixed_count("a b a") == {"a": 2, "b": 1}
assert fixed_count("") == {}

try:
    print(broken_double(5) + 1)
except TypeError as error:
    print(type(error).__name__, error)
assert fixed_double(5) + 1 == 11

def sometimes_returns(number):
    if number > 0:
        return number
    # Ja number <= 0, funkcija netieši atgriež None.


print(sometimes_returns(5), sometimes_returns(0))
# Uzdevums: vienojies par pareizo rezultātu visiem zariem un uzraksti testu.
