"""Integrēts piemērs: inventārs, daudzumi un kopsumma."""
# Atšķirīgi dati no patstāvīgā darba uzdevuma.
prices = {"tēja": 2.00, "kafija": 4.50, "cepumi": 1.25}
basket = ["tēja", "cepumi", "tēja", "kafija", "sula"]

# 1. Biežuma algoritmu var izmantot arī produktiem.
quantities = {}
for product in basket:
    quantities[product] = quantities.get(product, 0) + 1
print(quantities)

# 2. Viena rinda katram produktam; nezināma cena nav nulle.
total = 0.0
missing = []
for product, quantity in quantities.items():
    if product not in prices:
        missing.append(product)
        print("Cena nav zināma:", product)
        continue
    subtotal = quantity * prices[product]
    total += subtotal
    print(f"{product}: {quantity} × {prices[product]:.2f} = {subtotal:.2f}")
print(f"Zināmo cenu summa: {total:.2f} EUR")  # 9.75
if missing:
    print("Grozs nav pilnībā novērtēts:", missing)

# Pārbaudes: tukšs grozs, atkārtojumi, tikai nezināms produkts.
