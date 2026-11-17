"""2. nodarbība: salikti nosacījumi un ligzdoti if."""
# Bibliotēkas darba laika vienkāršots modelis.
stunda = 18
darba_diena = True
ir_registrets = True

# Pieņemam, ka darba dienās atvērts [9, 19),
# brīvdienās [10, 16). Augšējā robeža nav iekļauta.
if darba_diena and 9 <= stunda < 19:
    print("Bibliotēka ir atvērta darba dienā.")
elif not darba_diena and 10 <= stunda < 16:
    print("Bibliotēka ir atvērta brīvdienā.")
else:
    print("Bibliotēka ir slēgta.")

# Ligzdots nosacījums: otrā pārbaude notiek tikai tad,
# ja pirmā ir patiesa.
if 0 <= stunda < 24:
    if ir_registrets:
        print("Var izmantot lasītāja karti.")
    else:
        print("Vispirms jāreģistrējas.")
else:
    print("Nepareizi norādīta stunda.")

# Ievēro: 'and' saista ciešāk nekā 'or'; iekavas palīdz lasīt.
ir_darbinieks = False
ir_ielugums = True
var_ienakt = ir_darbinieks or (ir_registrets and ir_ielugums)
print("Vai var ienākt pasākumā?", var_ienakt)

# Maini stundu uz 9, 16, 19 un 24; ievēro atšķirīgās robežas.
