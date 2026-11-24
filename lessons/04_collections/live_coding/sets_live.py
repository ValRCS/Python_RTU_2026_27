# kopas - sets dod mums iespēju saglabāt unikālas vērtības. 
# Tas nozīmē, ka, ja mēs pievienojam vienu un to pašu vērtību vairākas reizes, tā tiks saglabāta tikai vienreiz.
# mēs varam veikt arī tā sauktās kopu operācijas, piemēram, apvienošanu, krustpunktu, atšķirību un simetrisko atšķirību.

# teiksim mums ir ēdienu saraksts
foods = ["Kefīrs", "Maize", "Siers",
         "Piens", "Biezpiens", "Bumbieris",
         "Biezpiens", "Maize", "Bumbieris"]
# visi ēdieni
print("saraksts ar ēdieniem:", foods) # izdrukā sarakstu ar ēdieniem
# kā atrast unikālos ēdienus sarakstā? Mēs varam izmantot kopu, lai iegūtu unikālās vērtības. Piemēram:
unique_foods = set(foods) # izveidojam kopu no saraksta
print("unikālie ēdieni:", unique_foods) # izdrukā unikālos ēdienus
# vienīgais jāatceras ka kopa ir nesakārtota, tas nozīmē, ka mēs nevaram garantēt, ka ēdieni tiks izdrukāti tādā pašā secībā kā sarakstā. 
# Ja mums ir svarīgi saglabāt secību, tad mēs varam izmantot sarakstu un pārbaudīt vai ēdiens jau ir sarakstā pirms pievienošanas.
# tipisku būtu to pārveidot atpakaļ par sarakstu, ja mums ir nepieciešams saglabāt secību. Piemēram:
unique_foods_list = list(unique_foods) # pārveidojam kopu atpakaļ par sarakstu
print("unikālie ēdieni sarakstā:", unique_foods_list) # izdrukā unikālos ēdienus sarakstā
# varam arī sakārtot alfabētiski - tiesa pēc Unicode, bet tas ir labāk nekā nekas
unique_foods_list.sort() # sakārtojam sarakstu alfabētiski
print("unikālie ēdieni sakārtoti alfabētiski:", unique_foods_list) # izdrukā unikālos ēdienus sakārtotus alfabētiski

# tātad ļoti tipiski ir tātad
# list -> set -> list -> sort un ir sakārtotas unikālās vērtības sarakstā

# kopas arī piedāva ļoti ārtru pārbaudi vai kāda vērtība ir kopā. Piemēram, ja gribam pārbaudīt vai "Piens" ir ēdienu sarakstā, tad varam darīt šādi:
if "Piens" in unique_foods: # pārbaudām vai "Piens" ir kopā
    print("Piens ir ēdienu kopā") # izdrukā ka "Piens" ir ēdienu kopā
else:
    print("Piens nav ēdienu kopā") # izdrukā ka "Piens" nav ēdienu sarakstā

# Te jāatceras, ka kopās atrast eksistenci kautk kam kaut ko būs ātrāk nekā sarakstā, jo kopas ir optimizētas meklēšanai pēc vērtībām.

# ar kopam var veikt arī kopu operācijas

# izveidosim kopas no range
numbers = set(range(1, 11)) # izveidojam kopu ar skaitļiem no 1 līdz 10
print("kopā ar skaitļiem no 1 līdz 10:", numbers) #

n_3_5 = set(range(3, 6)) # izveidojam kopu ar skaitļiem no 3 līdz 5
print("kopā ar skaitļiem no 3 līdz 5:", n_3_5) # izdrukā kopu ar skaitļiem no 3 līdz 5

n_4_7 = set(range(4, 8)) # izveidojam kopu ar skaitļiem no 4 līdz 7
print("kopā ar skaitļiem no 4 līdz 7:", n_4_7) # izdrukā kopu ar skaitļiem no 4 līdz 7

# mēs varam pārbaudīt va kāda kopa ir apakš vai virskopa citai kopai. Piemēram, vai kopa n_3_5 ir apakškopa kopai numbers:
if n_3_5.issubset(numbers): # pārbaudām vai n_3_5 ir apakškopa kopai numbers
    print("kopa n_3_5 ir apakškopa kopai numbers") # izdrukā ka n_3_5 ir apakškopa kopai numbers

# varam arī apvienot grupas
n_3_7 = n_3_5.union(n_4_7) # apvienojam kopas n_3_5 un n_4_7
print("apvienojam kopas n_3_5 un n_4_7:", n_3_7) # izdrukā apvienoto kopu

# kā būt ar šķēlumu - tas kas ir kopu krustpunkts. Piemēram, ja gribam atrast kopīgos elementus starp n_3_5 un n_4_7, tad varam darīt šādi:
n_3_5_n_4_7_intersection = n_3_5.intersection(n_4_7) # atrodam kopīgos elementus starp n_3_5 un n_4_7
print("kopīgie elementi starp n_3_5 un n_4_7:", n_3_5_n_4_7_intersection) # izdrukā kopīgos elementus starp n_3_5 un n_4_7

# python piedāva arī īsāku sintaksi kopu operācijām, piemēram, apvienošanai, krustpunktam, atšķirībai un simetriskajai atšķirībai. Piemēram:
# apvienošana
n_3_7_short = n_3_5 | n_4_7 # apvienojam kopas n_3_5 un n_4_7 ar īsāku sintaksi
print("apvienojam kopas n_3_5 un n_4_7 ar īsāku sintaksi:", n_3_7_short) # izdrukā apvienoto kopu ar īsāku sintaksi
# krustpunkts
n_3_5_n_4_7_intersection_short = n_3_5 & n_4_7 # atrodam kopīgos elementus starp n_3_5 un n_4_7 ar īsāku sintaksi
print("kopīgie elementi starp n_3_5 un n_4_7 ar īsāku sintaksi:", n_3_5_n_4_7_intersection_short) # izdrukā kopīgos elementus starp n_3_5 un n_4_7 ar īsāku sintaksi


# ir arī atšķirība un simetriskā atšķirība,
n_3_5_n_4_7_difference = n_3_5.difference(n_4_7) # atrodam elementus, kas ir n_3_5, bet nav n_4_7
print("elementi, kas ir n_3_5, bet nav n_4_7:", n_3_5_n_4_7_difference) # izdrukā elementus, kas ir n_3_5, bet nav n_4_7
# atšķirība nav simetriska
n_4_7_n_3_5_difference = n_4_7.difference(n_3_5) # atrodam elementus, kas ir n_4_7, bet nav n_3_5
print("elementi, kas ir n_4_7, bet nav n_3_5:", n_4_7_n_3_5_difference) # izdrukā elementus, kas ir n_4_7, bet nav n_3_5
# ja vajag visus elementus kas ir nav kopīgi, tad varam izmantot simetrisko atšķirību
n_3_5_n_4_7_symmetric_difference = n_3_5.symmetric_difference(n_4_7) # atrodam elementus, kas ir vai nu n_3_5 vai n_4_7, bet ne abos
print("elementi, kas ir vai nu n_3_5 vai n_4_7, bet ne abos:", n_3_5_n_4_7_symmetric_difference) # izdrukā elementus, kas ir vai nu n_3_5 vai n_4_7, bet ne abos

# atšķirība
n_3_5_n_4_7_difference_short = n_3_5 - n_4_7 # atrodam elementus, kas ir n_3_5, bet nav n_4_7, ar īsāku sintaksi
print("elementi, kas ir n_3_5, bet nav n_4_7 ar īsāku sintaksi:", n_3_5_n_4_7_difference_short) # izdrukā elementus, kas ir n_3_5, bet nav n_4_7, ar īsāku sintaksi
# simetriskā atšķirība
n_3_5_n_4_7_symmetric_difference_short = n_3_5 ^ n_4_7 # atrodam elementus, kas ir vai nu n_3_5 vai n_4_7, bet ne abos, ar īsāku sintaksi
print("elementi, kas ir vai nu n_3_5 vai n_4_7, bet ne abos ar īsāku sintaksi:", n_3_5_n_4_7_symmetric_difference_short) # izdrukā elementus, kas ir vai nu n_3-5 vai n-4-7, bet ne abos, ar īsāku sintaksi