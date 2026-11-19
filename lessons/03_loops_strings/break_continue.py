# var būt noderīgi izmantot mūžīgo ciklu bet no tā "izlausties"
# tam izmantojam atslēgas vārdu break

summa = 0
while True: # mūžigais cikls!!
    # summa += 5 # šis izpildīsiem vienmēr, ja negribam tad jāiek aiz if
    ievads = input("Vai turpināt? Y/N ")
    if ievads == "N":
        print("Labs ir beidzam")
        break # iziet no visa while cikla uzreiz un aiziet uz 13 rindiņu
    summa += 5 # tātad ja iziesim pirmo reizi tad nekas nemainīsies
    print(f"Turpinam ciklu summa ir {summa}")

# esam ārā no cikla
print(f"Summa ir {summa}")
