# bieži strādājot ar datiem var būt ērti salikt kopā vairākas vārdnīcas sarakstā, 
# lai varētu viegli piekļūt datiem. Piemēram, ja mums ir saraksts ar cilvēkiem 
# un viņu vecumu, mēs varam izveidot sarakstu ar vārdnīcām, kur katra vārdnīca satur cilvēka vārdu un vecumu.
# un arī viņa hobiju
people = [
    {"name": "Jānis", "age": 25, "hobby": "futbols"},
    {"name": "Anna", "age": 30, "hobby": "lasīšana"},
    {"name": "Pēteris", "age": 20, "hobby": "zīmēšana"},
    {"name": "Līga", "age": 35, "hobby": "ceļošana"}
]
print("saraksts ar cilvēkiem:", people) # izdrukā sarakstu ar cilvēkiem

# šāds formāts ir ļoti ērts, jo mēs varam viegli piekļūt datiem, piemēram, ja gribam izdrukāt visus cilvēkus un viņu hobijus, mēs varam darīt šādi:
for person in people: # ejam cauri visiem cilvēkiem sarakstā people
    print(person["name"], "hobijs ir:", person["hobby"]) # izdrukā cilvēka vārdu un hobiju

# mēs varam pievienot cilvēku ar citām atlslēgam piemēram auto un teiksim maksimālo ātrumu
people.append({"name": "Mārtiņš", "age": 28, "hobby": "skriešana", "car": "BMW", "max_speed": 250}) # pievienojam jaunu cilvēku sarakstam people
print("saraksts ar cilvēkiem pēc pievienošanas:", people) # izdruk
# pieliksim vēl vienu cilvēku ar auto
people.append({"name": "Liene", "age": 22, "hobby": "peldēšana", "car": "Audi", "max_speed": 240}) # pievienojam jaunu cilvēku sarakstam people
print("saraksts ar cilvēkiem pēc pievienošanas:", people) # izdruk

# ja gribam saglabat jaunā sarakstā cilvēkus kuriem ir auto, mēs varam darīt šādi:
people_with_cars = [] # sākam ar jaunu tukšu sarakstu
for person in people: # cikls cauri visiem cilvēkiem sarakstā people
    if "car" in person: #mēs meklējam katra cilveka vārdnīcā atslēgu "car", ja tāda ir, tad tas nozīmē, ka cilvēkam ir auto
        people_with_cars.append(person) # pievienojam sarakstam jaunu cilvēka vārdnīcu, ja viņam ir auto
print("saraksts ar cilvēkiem ar auto:", people_with_cars)


# var būt arī sarežģitākas daudz līmeņu strūktūras
# piemeram vārdnīca kas reprezentā dokumentu
# pēc tam vārdnīca kas reprezentē dokumenta autoru
document = {
    "title": "Mans dokuments",
    "author": {
        "name": "Jānis",
        "age": 25,
        "hobbies": ["futbols", "lasīšana", "zīmēšana"]
    },
    "content": "Šis ir mans dokuments. Tas satur informāciju par mani un manu hobiju."
}

# kā atrast autora pēdejo hobiju?
last_hobby = document["author"]["hobbies"][-1] # piekļūstam autora hobiju sarakstam un paņemam pēdējo hobiju
print("autora pēdējais hobijs ir:", last_hobby) # izdruk
# protams mums ir jāzina šī struktūra, lai varētu piekļūt datiem, bet ja mēs zinām, ka dokumenta struktūra ir šāda, tad mēs varam viegli piekļūt datiem.