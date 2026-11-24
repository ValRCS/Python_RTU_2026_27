"""Vārdnīcas: atslēgas, vērtības un praktiskas darbības."""
# 1. Izveido un papildini
prices = {}
prices["maize"] = 1.50
prices["piens"] = 1.20
prices["ābols"] = 0.60
prices["piens"] = 1.30
print(prices, len(prices))
print(prices["maize"])
print("siers" in prices, prices.get("siers"), prices.get("siers", "nav cenas"))
print(1.50 in prices, 1.50 in prices.values())  # Atslēga pret vērtību

# 2. Trīs iterācijas veidi; .items() atgriež pārus.
for product in prices:
    print(product, prices[product])
for price in prices.values():
    print(price)
for product, price in prices.items():
    print(f"{product}: {price:.2f} EUR")
print("Visu cenu summa:", sum(prices.values()))

# 3. Papildināšana, dzēšana un sakārtošana
prices.update({"siers": 3.20, "maize": 1.60})
removed = prices.pop("piens")
print(removed, prices)
for product in sorted(prices):
    print(product, prices[product])

# 4. Atslēgas ir unikālas; vienādas vērtības atļautas.
scores = {"Anna": 8, "Jānis": 8, "Ilze": 9}
scores["Anna"] = 10
print(scores)
# Noderīga izvēle: dict, ja vajag vērtību atrast pēc atslēgas.
