"""4. nodarbība: korteži; kopas kā izvēles papildu tēma."""

coordinates = (56.95, 24.10)
print("Rīgas aptuvenās koordinātas:", coordinates)
print("Platums:", coordinates[0])
print("Garums:", coordinates[1])
print("Korteža garums:", len(coordinates))

single = (5,)
print("Vienas vērtības kortežs:", single)

# coordinates[0] = 57.0  # TypeError: tuple nemaināms.
# Kortežā var atrasties maināmi objekti, bet šeit tos neapskatām.

names = ["Anna", "Jānis", "Anna", "Ilze"]
unique_names = set(names)
print("Unikālo vārdu skaits:", len(unique_names))
print("Anna ir kopā?", "Anna" in unique_names)
print("Sakārtots izvadam:", sorted(unique_names))

# Kopai nav indeksu; elementu izvadīšanas secība nav garantēta.
# Tukšu kopu veido set(), bet {} ir tukša vārdnīca.
group_a = {"Anna", "Jānis", "Ilze"}
group_b = {"Jānis", "Marta"}
print("Abās grupās:", sorted(group_a & group_b))
