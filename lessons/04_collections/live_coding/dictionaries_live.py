# kāpēc saraksts nav ideāla struktūra visam
# pieņemsim ka gribam glabāt ēdienus un to cenas
# tad varam veidot tā sauktu 2D sarakstu
foods_prices = [["Kefīrs", 1.5], ["Maize", 0.8], ["Siers", 2.5], ["Piens", 1.2]]
print("ēdieni un to cenas:", foods_prices) # izdrukā ēdienus

# cik maksā piens?
print("Piens maksā:", foods_prices[3][1]) # šeit mēs zinājām indeksus

# savukārt vispārīgi ja nezinātu būtu jādara šādi
food = "Piens"
for food_price in foods_prices: # ejam cauri visiem ēdieniem un to cenām
    print("pārbaudām ēdienu:", food_price) # izdrukā pārbaudāmo ēdienu un tā cenu
    if food_price[0] == food: # ja ēdiens ir "Piens"
        print(food, "maksā:", food_price[1]) # izdrukā cenu
        break # pārtraucam ciklu, jo atradām ko meklējām

# ar vārdnīcu viss ir daudz vienkāršāk, jo mēs varam glabāt ēdienus kā atslēgas un to cenas kā vērtības. Piemēram, mēs varam veidot vārdnīcu ar ēdieniem un to cenām šādi:
foods_prices_dict = {"Kefīrs": 1.5, "Maize": 0.8, "Siers": 2.5, "Piens": 1.2}
print("ēdieni un to cenas vārdnīcā:", foods_prices_dict)

# cik maksā piens vārdnīcā?
print("Piens maksā:", foods_prices_dict["Piens"]) # šis pieprasījums strādās arī ļoti ātri
# pat ja vārdnīca ir milzīga, jo vārdnīcas ir optimizētas meklēšanai pēc atslēgām

# kā būt ja meklēju cenu kaut kam kas nav vārdnīca'tad ir divi varianit

# es varu pārbaudīt vai atslēga ir vārdnīcā, pirms mēģinu piekļūt tās vērtībai. Piemēram, ja gribu uzzināt cik maksā "Bumbieris", tad varu darīt šādi:
food = "Bumbieris"
if food in foods_prices_dict: # pārbaudām vai ēdiens ir vārdnīcā PĒC atslēgām
    print(food, "maksā:", foods_prices_dict[food]) # izdrukā cenu
else:
    print(food, "nav vārdnīcā") # izdrukā ka ēdiens nav vārdnīcā

# alternatīvi es varu izmantot get() metodi, kas atgriež None, ja atslēga nav vārdnīcā. Piemēram, ja gribu uzzināt cik maksā "Bumbieris", tad varu darīt šādi:
cena = foods_prices_dict.get("Bumbieris") # mēģinām iegūt cenu vārdnīcā
if cena is not None: # pārbaudām vai cena nav None
    print("Bumbieris maksā:", cena) # izdrukā cenu  
else:
    print("Bumbieris nav vārdnīcā") # izdrukā ka ēdiens nav vārdnīcā

# es varēju arī padot get noklusēto vērtību, ja atslēga nav vārdnīcā. Piemēram, ja gribu uzzināt cik maksā "Bumbieris", tad varu darīt šādi:
cena = foods_prices_dict.get("Bumbieris", "neko jo nav mums") # mēģinām iegūt cenu vārdnīcā, ja nav tad atgriež "nav vārdnīcā"
print("Bumbieris maksā:", cena) # izdrukā cenu vai neko jo nav mums

# ar vārdnīcu es iegūst vairāk variantu aprakstīt datus

# es varu izdrukāt arī visus elementus vārdnīcā, gan atslēgas, gan vērtības, gan pārus. Piemēram, es varu izdrukāt visus ēdienus un to cenas šādi:
print("ēdieni un to cenas vārdnīcā:")
for food, price in foods_prices_dict.items(): # ejam cauri visiem ēdieniem un to cenām vārdnīcā
    print(food, "maksā:", price) # izdrukā ēdienu un tā cenu

# es varu iet cauri tikai atslēgām vārdnīcā, piemēram, ja gribu izdrukāt visus ēdienus vārdnīcā:
print("ēdieni vārdnīcā:")
for food in foods_prices_dict.keys(): # ejam cauri visiem ēdieniem vārdnīcā
    print(food) # izdrukā ēdienu

# vēl īsāk būtu bez keys
for food in foods_prices_dict: # ejam cauri visiem ēdieniem vārdnīcā
    print(food, "cena", foods_prices_dict[food]) # izdrukā ēdienu un tā cenu pēc atslēga
    # ievērojam ka šeit get ir lieks jo mums ir garantija ka atslēga ir vārdnīcā, jo mēs ejam cauri visām atslēgām

# varam izdrukāt items()
print("ēdieni un to cenas vārdnīcā:")
print(foods_prices_dict.items())
# varējo to pārverst par sarakstu ar list() metodi
print("ēdieni un to cenas vārdnīcā sarakstā:")
print(list(foods_prices_dict.items())) # izdrukā sarakstu ar pāriem (ēdiens, cena)
# salīdzinam ar vārdnīcu
print(foods_prices_dict) # izdrukā vārdnīcu ar pāriem (ēdiens, cena)

# vārdnīcas garums
print("vārdnīcas garums:", len(foods_prices_dict)) # izdrukā vārdnīcas garumu

# pielikt ir pavisam vienkārši, jo mēs varam pievienot jaunu pāri (atslēga, vērtība) vārdnīcai šādi:
foods_prices_dict["Bumbieris"] = 1.8 # pievienojam jaunu pāri (atslēga, vērtība) vārdnīcai
print("ēdieni un to cenas vārdnīcā pēc pievienošanas:", foods_prices_dict) # izdrukā vārdnīcu ar pāriem (ēdiens, cena)
# ja kefīram mainās cena varu to nomainīt šādi:
foods_prices_dict["Kefīrs"] = 1.3 # mainām pāra (atslēga, vērtība) vērtību vārdnīcā
print("ēdieni un to cenas vārdnīcā pēc cenas maiņas:", foods_prices_dict) # izdrukā vārdnīcu ar pāriem (ēdiens, cena)
# tas nozīme ka vārdnīcā atslēgas ir unikālas, ja pievienojam jaunu pāri ar jau esošu atslēgu, tad vērtība tiek pārrakstīta

# apskatīsim vēl pāris metodes, kas ir noderīgas vārdnīcām. Piemēram, mēs varam izmantot pop() metodi, lai izdzēstu pāri (atslēga, vērtība) vārdnīcā. Piemēram, ja gribu izdzēst "Bumbieris" pāri, tad varu darīt šādi:
izmestais = foods_prices_dict.pop("Bumbieris") # izdzēšam pāri (atslēga, vērtība) vārdnīcā
print("izdzēstā vērtiba:", izmestais) # izdrukā izdzēsto pāri (atslēga, vērtība)
print("ēdieni un to cenas vārdnīcā pēc izdzēšanas:", foods_prices_dict) # izdrukā vārdnīcu ar pāriem (ēdiens, cena)

# ar dictionary ir līdzi kā ar list ja iet runa par alias un kopy

foods_prices_alias = foods_prices_dict # alias, abas mainīgās norāda uz to pašu vārdnīcu
print("ēdieni un to cenas vārdnīcā pēc alias:", foods_prices_alias) # izdrukā vārdnīcu ar pāriem (ēdiens, cena)
# ja mēs pieliksim vai noņemis pāri alias tas mainīs arī foods_prices_dict, jo abas mainīgās norāda uz to pašu vārdnīcu
foods_prices_alias["Šokolāde"] = 2.0 # pievienojam jaunu pāri (atslēga, vērtība) vārdnīcai
print("ēdieni un to cenas vārdnīcā pēc alias pievienošanas:", foods_prices_alias) # izdrukā vārdnīcu ar pāriem (ēdiens, cena)
# arī original mainīgais ir mainījies
print("ēdieni un to cenas vārdnīcā pēc alias pievienošanas:", foods_prices_dict) # izdrukā vārdnīcu ar pāriem (ēdiens, cena)  

# ja gribam kopēt tad kopējam vārdnīcu ar copy() metodi, kas izveido jaunu vārdnīcu ar tiem pašiem pāriem (atslēga, vērtība). Piemēram, ja gribu kopēt foods_prices_dict, tad varu darīt šādi:
foods_prices_copy = foods_prices_dict.copy() # kopējam vārdnīcu
print("ēdieni un to cenas vārdnīcā pēc kopēšanas:", foods_prices_copy) # izdrukā vārdnīcu ar pāriem (ēdiens, cena)
# pieliek klāt vēl pāri (atslēga, vērtība) vārdnīcai
foods_prices_copy["Bumbieris"] = 1.8 # pievienojam jaunu pāri (atslēga, vērtība) vārdnīcai
print("ēdieni un to cenas vārdnīcā pēc kopēšanas un pievienošanas:", foods_prices_copy) # izdrukā vārdnīcu ar pāriem (ēdiens, cena)
# original vārdnīca nav mainījusies
print("ēdieni un to cenas vārdnīcā pēc kopēšanas un pievienošanas:", foods_prices_dict) # izdrukā vārdnīcu ar pāriem (ēdiens, cena)

# es varu arī iztīrīt vārdnīcu ar clear() metodi, kas izdzēš visus pārus (atslēga, vērtība) vārdnīcā. Piemēram, ja gribu iztīrīt foods_prices_copy, tad varu darīt šādi:
# iztīriam original vārdnīcu
foods_prices_dict.clear() # izdzēšam visus pārus (atslēga, vērtība) vārdnīcā IN PLACE
print("ēdieni un to cenas vārdnīcā pēc iztīrīšanas:", foods_prices_dict) # izdrukā vārdnīcu ar pāriem (ēdiens, cena)
# alias ?
print("ēdieni un to cenas alias vārdnīcā pēc iztīrīšanas:", foods_prices_alias) # izdrukā vārdnīcu ar pāriem (ēdiens, cena)
print("ēdieni un to cenas kopētā vārdnīcā pēc iztīrīšanas:", foods_prices_copy) # izdrukā vārdnīcu ar pāriem (ēdiens, cena)

# atgriežām origināl vārdnīcu ar copy
foods_prices_dict = foods_prices_copy.copy() # kopējam vārdnīcu atpakaļ
print("esam atgriezuši ēdienus un to cenas vārdnīcā:", foods_prices_dict) # izdrukā vārdnīcu ar pāriem (ēdiens, cena)

# bieži vajag iziet cauri vārdnīca un atrast kaut ko, piemēram, ja gribu atrast visus ēdienus, kas maksā vairāk par 1.5, tad varu darīt šādi:
print("ēdieni, kas maksā vairāk par 1.5:")
luxury_foods = {} # izveidojam jaunu vārdnīcu
for food, price in foods_prices_dict.items(): # ejam cauri visiem ēdieniem un to cenām vārdnīcā
    if price > 1.5: # ja cena ir lielāka par 1.5
        print(food, "maksā:", price) # izdrukā ēdienu un tā cenu
        luxury_foods[food] = price # pievienojam pāri (atslēga, vērtība) jaunajai vārdnīcai

print("ēdieni, kas maksā vairāk par 1.5 vārdnīcā:", luxury_foods) # izdrukā jauno vārdnīcu ar pāriem (ēdiens, cena)

# BONUS: var papētīt arī dictionary comprehension, kas ir līdzīgs list comprehension, bet izveido vārdnīcu. Piemēram, ja gribu izveidot jaunu vārdnīcu ar ēdieniem, kas maksā vairāk par 1.5, tad varu darīt šādi:
luxury_foods_dict = {food: price for food, price in foods_prices_dict.items() if price > 1.5} # izveidojam jaunu vārdnīcu ar ēdieniem, kas maksā vairāk par 1.5
print("ēdieni, kas maksā vairāk par 1.5 vārdnīcā ar dictionary comprehension:", luxury_foods_dict) # izdrukā jauno vārdnīcu ar pāriem (ēdiens, cena)