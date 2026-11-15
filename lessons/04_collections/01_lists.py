"""4. nodarbība: sarakstu izveide, indeksi, modificēšana un cikli."""

fruits = ["ābols", "banāns", "bumbieris"]
print("Sākumā:", fruits)
print("Pirmais:", fruits[0])
print("Pēdējais:", fruits[-1])
print("Pirmie divi:", fruits[:2])

fruits.append("plūme")
fruits[1] = "ķirsis"
print("Pēc izmaiņām:", fruits)

fruits.remove("ābols")
removed = fruits.pop()
print("Izņemtais pēdējais:", removed)
print("Atlikušais saraksts:", fruits)

for fruit in fruits:
    print("Auglis:", fruit)

numbers = [4, 8, 6]
print("Skaits:", len(numbers))
print("Summa:", sum(numbers))
print("Mazākais:", min(numbers))
print("Lielākais:", max(numbers))

empty = []
print("Tukšs saraksts:", empty, "garums:", len(empty))

# Pārbaudi atšķirību starp append() un list piesaisti mainīgajam:
# returned = numbers.append(10)  # returned ir None, bet numbers mainās.
