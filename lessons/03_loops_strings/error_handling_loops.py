# mēs varam kombinēt while ciklu ar try except bloku, lai apstrādātu kļūdas, kas var rasties cikla laikā
summa = 0
skaitlis = 0
while True:
    print("Cikla sākums")
    try:
        ievads = input("Ievadi skaitli vai Q (beigt): ")
        if ievads == "Q" or ievads == "q" or ievads == "QUIT": #kā to padarīt vispārīgaku?
            print("Labs ir beidzam")
            break # ejam ārā no while cikla
        skaitlis = float(ievads) # šim ir jēga būt iekš try bloka, jo var būt kļūda
        # šī rindiņa tiks izpildīta tikai tad, ja iepriekšējā rindiņa neizraisīs kļūdu
        print(f"Tu ievadīji {skaitlis}")
    except ValueError: # es ķeru specifisku kļūdas tipu
        print("Kļūda: ievadīts nav skaitlis")
        continue #mēģinam vēlreiz ejam uz while True sākumu
    except KeyboardInterrupt: # tas aktivizēsies pie Ctrl-C (cmd-c uz mac)
        print("Lietotājs atsauca programmu")
        break
    # šeit mums ir garantija, ka skaitlis ir ievadīts pareizi
    summa += skaitlis
    print(f"Summa ir {summa}")

# ārpus cikla
print(f"Programmas beigās summa ir {summa}")
print(f"Pēdejais skaitlis kas bija korekts {skaitlis}") # potenciāli varētu arī nebūt nekas

# varam arī izmanto šo konstrukcijau vienkāršāk lai garantētu ka mums ir skaitlis

while True:
    print("Lūdzu ievadiet veselu skaitli!")
    try:
        ievads = input("IEVADS: ")
        vesels_skaitlis = int(ievads) # te ir tā kļūdas ķeršana!
        # te mums jau veselais varam beigt
        print(f"Paldies jūsu skaitlis ir {vesels_skaitlis}")
        break
    except ValueError:
        print(f"Jūsu {ievads} nav vesels skaitlis :(")
    # te mēs atgriežamies cikla sākumā

# te mēs varam sākt strādāt ar šo skaitli, mums ir 100% garantija ka tas ir vesels
print(f"Strādājam ar veselo skaitli {vesels_skaitlis}")