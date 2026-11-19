summa = 0
while True:
    try:
        ievads = input("Ievadi skaitli vai Q:")
        if ievads == "Q" or ievads == "q":
            print("Beidzam")
            break  # ejam area no while
        skaitlis = float(ievads)
        print(f"Tu ievadiji skaitli {skaitlis}")
        print(f"Tu ievadiju {skaitlis}")
    except ValueError:
        print("Kluda: ievadits nav skaitlis")
        continue  # velreiz ejam un while true sakumu
    except KeyboardInterrupt:
        print("User atsauca programmu")
        break
    # seit mums ir garantija, ka skaitlis ir ievadits pareizi
    summa += skaitlis
    print(f"Summa ir {summa}")

# arpus cikla
print(f"Programmas beigas summaa ir {summa}")
print(f"pedejais skaitlis kas bija korenkts {skaitlis}")
