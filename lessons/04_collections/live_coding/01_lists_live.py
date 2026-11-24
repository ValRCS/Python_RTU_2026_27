"""Saraksti: demonstrācijas secībā; katru bloku var mainīt un atkārtot."""

# 1. Izveide, tips, secība, atkārtojumi
products = ["maize", "piens", "ābols", "ābols"]
empty = []
print(type(products), len(products), len(empty))
print(products[0], products[-1])
print(products[1:3], products[:2], products[::2], products[::-1])
print(products[:100])  # Šķēlums drīkst pārsniegt robežas.

# 2. Mutācija un metožu rezultāti
products[1] = "kefīrs"
returned = products.append("siers")
print(products, returned)  # None
products.extend(["olas", "sviests"])
products.insert(1, "tēja")
print(products)
products.remove("ābols")  # Tikai pirmā atbilstība.
last = products.pop()
print(last, products)
print("ābols" in products, "kafija" not in products)
print(products.count("ābols"), products.index("maize"))

# 3. Cikls: vispirms vērtības, pēc tam numurēšana
for product in products:
    print(product)
for number, product in enumerate(products, start=1):
    print(number, product)

# 4. Jauns saraksts vai esošā saraksta maiņa?
numbers = [7, 3, 9, 1, 3]
ordered = sorted(numbers)
print(numbers, ordered)
print(numbers.sort())  # None
print(numbers)
numbers.reverse()
print(numbers)

# Papildus: divi mainīgie var norādīt uz vienu objektu.
a = [1, 2, 3]
b = a
b.append(4)
print(a, b)
c = a.copy()
c.append(5)
print(a, c)
