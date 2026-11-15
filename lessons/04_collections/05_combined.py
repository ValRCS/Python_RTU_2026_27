"""4. nodarbība: produktu saraksts kopā ar cenu vārdnīcu."""

prices = {"maize": 1.50, "piens": 1.20, "ābols": 0.60}
basket = ["maize", "ābols", "ābols", "piens", "siers"]

total = 0.0
unknown = []
for product in basket:
    if product in prices:
        total += prices[product]
    else:
        unknown.append(product)

print("Groza produkti:", basket)
print("Kopējā cena:", f"{total:.2f} EUR")
print("Nav cenu:", unknown)

# Papildu vingrinājums: no groza izveido produktu daudzuma vārdnīcu.
quantities = {}
for product in basket:
    quantities[product] = quantities.get(product, 0) + 1
print("Daudzumi:", quantities)
