"""Kopas: minimums visiem, papildu operācijas pēc prakses."""
# Minimums (2–3 min): unikālums, piederība, tukša kopa.
names = ["Anna", "Jānis", "Anna", "Ilze"]
unique = set(names)
print(sorted(unique), len(unique))
print("Anna" in unique)
print(type(set()), type({}))
unique.add("Marta")
unique.add("Anna")
print(sorted(unique))

# Papildus: divu grupu salīdzināšana.
a = {"Anna", "Jānis", "Ilze"}
b = {"Jānis", "Marta"}
print("Apvienojums:", sorted(a | b))
print("Šķēlums:", sorted(a & b))
print("Tikai A:", sorted(a - b))
print("Tieši vienā grupā:", sorted(a ^ b))
print("A apakškopa:", a <= b)
unique.discard("Nezināms")  # Nav kļūdas.

# Papildus: latviešu alfabēta pangrammas pārbaude.
alphabet = set("aābcčdeēfgģhiījkķlļmnņoprsštuūvzž")
text = "Ātrs brūns lapsas lēciens"
missing = alphabet - set(text.lower())
print("Trūkstošie burti:", "".join(sorted(missing)))
print("Pangramma:", not missing)
