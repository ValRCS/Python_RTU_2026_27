"""No 4. nodarbības algoritma līdz atkārtoti izmantojamai funkcijai."""
import sys


# 1. Pazīstamais cikls (viena konkrēta ievade).
text = "Rīga Python Rīga"
counts = {}
for word in text.lower().split():
    counts[word] = counts.get(word, 0) + 1
print("Pirms refaktoringa:", counts)


# 2. Tas pats algoritms, bet dati tiek padoti kā arguments.
def count_words(text):
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


print(count_words(text))
print(count_words("Python Python"))
print(count_words(""))
assert count_words(text) == counts

# 3. Aprēķinu nodalām no ievades un izdrukas.
def calculate_price(price, quantity):
    return price * quantity


print(f"Kopā: {calculate_price(2.50, 3):.2f} EUR")
# Ievades variants tikai tad, ja palaiž ar --input.
if "--input" in sys.argv:
    while True:
        try:
            price = float(input("Cena: "))
            quantity = int(input("Daudzums: "))
            if price < 0 or quantity < 0:
                print("Vērtībām jābūt nenegatīvām.")
                continue
            break
        except ValueError:
            print("Ievadi skaitļus.")
    print(f"Kopā: {calculate_price(price, quantity):.2f} EUR")
