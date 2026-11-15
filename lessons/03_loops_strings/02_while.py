"""3. nodarbība: while un pārtraukšanas komanda (Python 3)."""

counter = 0
while counter < 4:
    print("Skaitītājs:", counter)
    counter += 1
print("Cikls beidzies; counter =", counter)

print("Ievadi tekstu; 'beigt' aptur programmu.")
entries = 0
while True:
    text = input("Teksts: ")
    if text.strip().lower() == "beigt":
        break
    entries += 1
print("Ievadīto rindu skaits:", entries)
