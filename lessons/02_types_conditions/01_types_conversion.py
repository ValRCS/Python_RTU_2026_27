"""2. nodarbība: datu tipu un ievades atkārtojums.

Šis ir neinteraktīvs piemērs: maini vērtības un palaid failu vēlreiz.
"""
# 1. nodarbībā iepazinām mainīgos, input() un datu tipus.
vecums_teksts = "18"  # input("Vecums: ") arī atgriež str.
print("Sākotnējā vērtība:", vecums_teksts, type(vecums_teksts))

vecums = int(vecums_teksts)
print("Pēc int():", vecums, type(vecums))
print("Nākamajā gadā:", vecums + 1)

# Virknes reizināšana atkārto tekstu, nevis aprēķina cenu.
cena_teksts = "2.50"
print("Virkne * 2:", cena_teksts * 2)
cena = float(cena_teksts)
print("Skaitlis * 2:", cena * 2)

# int() atmet daļu aiz komata (virzienā uz nulli), nevis noapaļo.
print("int(-3.7):", int(-3.7))
print("round(-3.7):", round(-3.7))

# bool() parāda, kā vērtības tiek interpretētas loģiskā kontekstā.
print("bool(0):", bool(0))
print("bool(5):", bool(5))
print("bool(''):", bool(""))
print("bool('False'):", bool("False"))  # Netukša virkne: True!

# Pamēģini atsevišķi: int("divi") -> ValueError.
# Lai ievadītu decimālskaitli, Python parasti sagaida punktu: 2.5.
