"""Korteži: fiksēta secība, indeksi un izpakošana."""
coordinates = (56.95, 24.10)
print(coordinates, len(coordinates))
print(coordinates[0], coordinates[-1], coordinates[:1])
print(type((5,)), type((5)))
latitude, longitude = coordinates
print("Platums:", latitude, "Garums:", longitude)

# Kortežu nevar mainīt pa elementiem.
# coordinates[0] = 57.0  # TypeError
new_coordinates = (57.0, longitude)
print(coordinates, new_coordinates)
mutable = list(coordinates)
mutable[0] = 57.0
print(mutable, tuple(mutable))

# Saikne ar dict.items(): katrs pāris ir kortežs.
for pair in {"Rīga": 1, "Liepāja": 2}.items():
    city, number = pair
    print(pair, city, number)
