# teksts / str tātad ir simbolu virkne
# simbols ir tā sauktais Unicode simbols
# simbols var būt angļu burts, latviešu burts, ķīniešu simbols, emoji un 
# vēl daudz kas cits
english_name = "Valdis"
latvian_name = "Voldemārs"
name_with_emoji = "Valdis ar alu 🍺"
# cik simbolu name_with_emoji ir?
print(f"Name with emoji {name_with_emoji} ir {len(name_with_emoji)} simboli")

# pirmais ko darīt ar pēdiņām?
# varam izmantot " un varam izmantot ' , bet ja vajag iekšā vienu no tām tad jāizmanto otra
quotes_inside = "Valdis teica 'Sveiks!'"
double_quotes_inside = 'Valdis teica "Sveiks!"'
# python treats both " and ' equally
# print both
print(quotes_inside)
print(double_quotes_inside)
# ja vajag abas " un ' tad jāizmanto trīskāršās pēdiņas
triple_quotes = """Valdis teica "Sveiks!" un tad vēl 'Sveiks!' """
print(triple_quotes)

# mēs varam izmantot trīskāršas pēdiņas arī lai rakstītu vairākas rindas
multi_line = """Valdis teica "Sveiks!"
Un tad vēl 'Sveiks!'
Un tad aizgāja uz mājām
"""
print(multi_line)

# ja gribam vairākas rindas vienkāršās pēdiņās tad jāizmanto \n
# \t nozīmē tabulāciju jeb atstarpi
multi_line_2 = "Valdis teica \"Sveiks!\"\n\tUn tad vēl"
print(multi_line_2)

# var kombinēt f-strings ar trīskāršām pēdiņām
# ļoti noderīgi ja gribam izveidot vairākas rindas ar mainīgajiem
name = "Valdis"
job = "Python programmētājs"
residence = "Rīga"
year = 2026
message = f"""Sveiks {name}!
Tu esi {job} un dzīvo {residence}.
Gads ir {year}"""
print(message)

# mēs varam izmanot in lai pārbaudītu vai kāds simbols ir tekstā
if "V" in name:
    print(f"Burts V ir vārda {name} iekšā")
else:
    print(f"Burts V nav vārda {name} iekšā")

# bieži izmanto mainīgo sauktu par needle kas tad ir tas kas tiek meklēts
needle = "aldis"
if needle in name:
    print(f"Virkne {needle} ir vārda {name} iekšā")
else:
    print(f"Virkne {needle} nav vārda {name} iekšā")

# string indeksācija sākas ar 0
print(f"Vārda {name} pirmais burts ir {name[0]}")
print(f"Vārda {name} otrais burts ir {name[1]}")
print(f"Vārda {name} trešais burts ir {name[2]}")
# mēs varam ar try mēģināt piekļūt arī ārpusē esošam simbolam
try:
    print(f"Vārda {name} piektais burts ir {name[4]}")
except IndexError:
    print(f"Vārda {name} piektais burts nav jo vārds ir par īsu")

# vēlreiz
try:
    print(f"Vārda {name} divdesmit sestais burts ir {name[25]}")
except IndexError:
    print(f"Vārda {name} divdesmit sestais burts nav jo vārds ir par īsu")
    print(f"Vārda {name} garums ir {len(name)} simboli")

# tad sanāktu formula pēdejam burtam ir len(name)-1
print(f"Vārda {name} pēdējais burts ir {name[len(name)-1]}") # tā var bet tas nav ērti
# ērtāk ir izmantot negatīvo indeksāciju
print(f"Vārda {name} pēdējais burts ir {name[-1]}")
# priekšpēdējais burts ir -2
print(f"Vārda {name} priekšpēdējais burts ir {name[-2]}")

# kā būtu ar apakšvirknēm?
# mēs izmantojam tā sauktu slice sintaksi
# slice sintakse ir [START:STOP:STEP] STOP nav iekļauts
print(f"Vārda {name} pirmās trīs burti ir {name[0:3]}")
# 0 nav obligāts, ja sākam no sākuma tad var izlaist
print(f"Vārda {name} pirmās trīs burti ir {name[:3]}") # ievērojam : tātad 0 ir pirms:
print(f"Vārda {name} pēdējie divi burti ir {name[-2:]}") # beigas nav jānorādīt, ja gribam līdz beigām
# print(f"Vārda {name} otrā līdz ceturtajam burtam ir {name[1:4]}")

# interesanti ka slice indekss kļūdas nav iespējamas pat ja pārsniedzam indeksus
print(f"Vārda {name} slice no -5000 līdz 100 ir {name[-5000:100]}") # slice sintakse neizmet kļūdu

# ir viens triks ar negatīvo slice sintaksi
# šādi varam apgriezt virkni
print(f"Vārda {name} apgrieztā secībā ir {name[::-1]}") # slice sintakse neizmet kļūdu
name_reversed = name[::-1]
print(f"Vārda {name} apgrieztā secībā ir {name_reversed}")

# jāatceras ka paši stringi netiek modificēti, ja gribam kaut ko mainīt tad jāizveido jauns string
# vai jāraksta virsu vecajam

food = "Auzu putra ar ievārījumu"
print(f"Food sākotnēji ir {food}")
# ja vēlamies mainīt food vērtību, tad jāizveido jauns string
food = "Auzu putra ar ievārījumu un sāli"
print(f"Food tagad ir {food}")
# mums ir replace metode arī
food = food.replace("sāli", "rozīnēm") # es pārrakstu pāri food ar jaunu vērtību
print(f"Food tagad ir {food}")
# es protams varēju izmantot jaunu mainīgo
food_experiment = food.replace("rozīnēm", "ķimenēm")
print(f"Food experiment tagad ir {food_experiment}")

# lai replace strādātu mainīgam jābut str tipam! tas nestrādas ar int tipa mainīgajiem vai float vai bool

# līdzi ir citas metodes, piemēram upper() un lower()
print(f"Food augstajā reģistrā ir {food.upper()}")
print(f"Food zemajā reģistrā ir {food.lower()}")
# bet food joprojām ir tāds pats kā sākumā jo str netiek modificēts
print(f"Food joprojām ir {food}")
food_uppercase = food.upper()
print(f"Food uppercase tagad ir {food_uppercase}")
# food joprojām ir tāds pats kā sākumā jo str netiek modificēts
print(f"Food joprojām ir {food}")
