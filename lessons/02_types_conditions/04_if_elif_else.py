"""2. nodarbība: nosacījumu izpilde un zaru secība."""
temperatura = 16  # Maini uz -5, 0, 24 vai 32 un palaid vēlreiz.

if temperatura < 0:
    print("Ārā ir sals.")
elif temperatura < 15:
    print("Ārā ir vēss.")
elif temperatura < 25:
    print("Ārā ir mēreni silts.")
else:
    print("Ārā ir karsts.")

print("Šī rinda izpildās vienmēr (ārpus if bloka).")

# Ja ir viena if/elif/else ķēde, izpilda tikai pirmo derīgo zaru.
punkti = 78
if punkti < 0 or punkti > 100:
    print("Nederīgs punktu skaits.")
elif punkti >= 90:
    print("Izcili!")
elif punkti >= 60:
    print("Ieskaitīts.")
else:
    print("Jāmācās vēl.")

# Nepareiza kārtība:
# if punkti >= 60: ...    # Šis zars noķertu arī 90 un 100.
# elif punkti >= 90: ...  # Tad šis zars nebūtu sasniedzams.
