"""Papildu uzdevumu A–G atsauces risinājumi."""
import sys

# A
temperatures = [4, -2, 1, -3]
negative = []
for t in temperatures:
    if t < 0:
        negative.append(t)
if temperatures:
    print("A:", sum(temperatures) / len(temperatures), negative)
else:
    print("A: Nav datu")

# B
numbers = [3, 2, 4, 3, 0]
even = []
for n in numbers:
    if n % 2 == 0:
        even.append(n)
print("B:", even)

# C
text = "Rīga ir skaista"
print("C:", " ".join(text.split()[::-1]))

# D
counts = {}
for char in "Aa B".lower():
    if not char.isspace():
        counts[char] = counts.get(char, 0) + 1
print("D:", counts)

# E
products = ["maize", "piens", "maize"]
if "--input" in sys.argv:
    products = []
    while True:
        product = input("Produkts (beigt): ").strip().lower()
        if product == "beigt":
            break
        if product:
            products.append(product)
inventory = {}
for product in products:
    inventory[product] = inventory.get(product, 0) + 1
print("E:", inventory)

# F
a = {"Anna", "Ilze"}
b = {"Anna", "Jānis"}
print("F:", sorted(a & b))

# G
alphabet = set("aābcčdeēfgģhiījkķlļmnņoprsštuūvzž")
text = "aābcčdeēfgģhiījkķlļmnņoprsštuūvzž"
print("G:", alphabet <= set(text.lower()))
print("G tukšs:", alphabet <= set(""))
