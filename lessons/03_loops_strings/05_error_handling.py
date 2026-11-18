"""3. nodarbība: ievades atkārtošana ar while un try/except.

Izmēģini secīgi: abc, -2, 5.
"""
while True:
    text = input("Ievadi nenegatīvu veselu skaitli: ")
    try:
        number = int(text)
    except ValueError:
        print("Nederīga ievade. Mēģini vēlreiz!")
        continue

    if number < 0:
        print("Skaitlim jābūt nenegatīvam.")
        continue
    break

print("Paldies! Ievadītais skaitlis:", number)
