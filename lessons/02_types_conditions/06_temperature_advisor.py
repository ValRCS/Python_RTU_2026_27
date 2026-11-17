"""2. nodarbība: pilns piemērs ar ievadi un nosacījumiem.

Palaid programmu un ievadi temperatūru grādos (piem., 12.5)
un j vai n. Skaitļa vietā ievadot tekstu, saņemsi ValueError;
pilnu kļūdu apstrādi mācīsimies vēlāk.
"""
temperatura = float(input("Kāda ir āra temperatūra (°C)? "))
atbilde = input("Vai līst lietus (j/n)? ").strip().lower()
ir_lietus = atbilde == "j"

if atbilde != "j" and atbilde != "n":
    print("Lūdzu norādi j vai n un palaid programmu vēlreiz.")
else:
    if temperatura < 0:
        print("Ieteikums: silta ziemas jaka, cepure un cimdi.")
    elif temperatura < 15:
        print("Ieteikums: jaka un piemēroti apavi.")
    elif temperatura < 25:
        print("Ieteikums: viegls apģērbs.")
    else:
        print("Ieteikums: viegls apģērbs un ūdens.")

    # Otrs nosacījums papildina pirmo ieteikumu.
    if ir_lietus:
        print("Paņem lietussargu vai lietusjaku.")
    else:
        print("Lietussargs nav nepieciešams, ja laikapstākļi nemainās.")

    if temperatura >= 25 and not ir_lietus:
        print("Silts un sauss: neaizmirsti padzerties ūdeni.")
