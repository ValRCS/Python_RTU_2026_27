# bieži vien mēs strādajam ar vienu sarakstu bet gribam izveidot jaunu sarakstu, kas satur tikai daļu no sākotnējā saraksta. To mēs varam izdarīt ar slice operatoru.
# piemēram, ja mēs gribam izveidot jaunu sarakstu tikai kuri sākas burtu "B"
foods = ["Kefīrs", "Maize", "Siers", 
         "Piens", "Biezpiens", "Bumbieris", 
         "Mango","Saldējums", "sulas", "banāns"]

print("sākotnējais saraksts:", foods) # izdrukā sākotnējo sarakstu

processed_foods = [] # sākam ar jaunu tukšu sarakstu

for food in foods: # ejam cauri visiem ēdieniem sarakstā foods
    if food.startswith("B"): # ja ēdiens sākas ar burtu "B", te var likt arī sarežītākus nosacījumus, piemēram, food.startswith("B") and len(food) > 5
        print("atrasts ēdiens, kas sākas ar B:", food) # izdrukā atrasto ēdienu
        processed_foods.append(food) # pievienojam to sarakstam processed_foods

print("apstrādātais saraksts:", processed_foods)

# šāda filtrēšana ir ļoti bieži sastopama programmēšanā, un to var izdarīt arī ar list comprehension, kas ir īsāks un efektīvāks veids, kā izveidot jaunu sarakstu no esošā saraksta. Piemēram, mēs varam izveidot jaunu sarakstu ar ēdieniem, kas sākas ar burtu "B", šādi:
s_foods = [food for food in foods if food.startswith("S")] # izveido jaunu sarakstu ar ēdieniem, kas sākas ar burtu "S"
print("ēdieni, kas sākas ar S:", s_foods) # izdrukā jauno sarakstu ar ēdieniem, kas sākas ar burtu "S"

# ja gribām būt elastīgaki tad varam meklējot pārveidot to ko meklējam uz mazo burtu, lai nebūtu svarīgi vai ēdiens sākas ar lielo vai mazo burtu. Piemēram, mēs varam izveidot jaunu sarakstu ar ēdieniem, kas sākas ar burtu "b" vai "B", šādi:
b_foods = []
for food in foods: # ejam cauri visiem ēdieniem sarakstā foods
    if food.lower().startswith("b"): # ja ēdiens sākas ar burtu "b" vai "B"
        print("atrasts ēdiens, kas sākas ar burtu B:", food) # izdrukā atrasto ēdienu
        b_foods.append(food) # pievienojam to sarakstam b_foods

print("ēdieni, kas sākas ar B:", b_foods) # izdrukā jauno sarakstu ar ēdieniem, kas sākas ar burtu "B"

# mēs varam arī vispārināt uz adatu kaut ko iekšā
needle = "ie"
ie_foods = []

for food in foods: # ejam cauri visiem ēdieniem sarakstā foods
    if needle in food: # ja ēdiens satur adatu "ie"
        print("atrasts ēdiens, kas satur adatu 'ie':", food) # izdrukā atrasto ēdienu
        ie_foods.append(food) # pievienojam to sarakstam ie_foods

print("ēdieni, kas satur adatu 'ie':", ie_foods) # izdrukā jauno sarakstu ar ēdieniem, kas satur adatu "ie"