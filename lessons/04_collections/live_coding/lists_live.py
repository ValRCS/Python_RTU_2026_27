food1 = "Kefīrs"
food2 = "Maize"
food3 = "Siers"
# bet ko darīt ja mums vajag apstrādāt vairākus pārtikas produktus? 
# Mēs varam izmantot sarakstu (list) un saglabāt visus produktus vienā vietā.
foods = ["Kefīrs", "Maize", "Siers"]
# teorētiski mēs varētu glabāt visādu miksli sarakstā
mikslis = ["Kefīrs", 1, True, 3.14] # bet parasti jāpadoma vai tam ir jēga, jo tas var radīt problēmas,
#ja mēs vēlāk gribam apstrādāt šos datus

# izdrukāsim visu sarakstu
print(foods)
print(mikslis)
empty_list = [] # tas ir tukšs saraksts, kurā vēlāk varam pievienot elementus
print(empty_list)

# apskatīsim saraksta elementu skaitu
print(f"Mums ir {len(foods)} ēdiena elementi.") # izdrukā saraksta foods elementu skaitu
print(f"Mums ir {len(mikslis)} jauktie elementi.") # izdrukā saraksta mikslis elementu skaitu
print(f"Mums ir {len(empty_list)} tukšie elementi.") # izdrukā saraksta empty_list elementu skaitu

# varam pārbaudīt vai kāds elements ir precīzi sarakstā
print("vai mums ir kefīrs?", "Kefīrs" in foods) # izdrukā True, jo "Kefīrs" ir sarakstā foods
print("vai mums ir siers?", "Siers" in foods) # izdrukā True, jo "Siers" ir sarakstā foods
print("vai mums ir maize?", "Maize" in foods) # izdrukā True, jo "Maize" ir sarakstā foods
print("vai mums ir piens?", "Piens" in foods) # izdrukā False, jo "Piens" nav sarakstā foods

# tikai jāatcerās ka šeit in pārbaude ir precīza, tātad "kefīrs" nav tas pats kas "Kefīrs"
# ja gribēsim tādu neprecīzu pārbaudi(fuzzy match), tad mums būs jāizmanto citas metodes, piemēram, regex vai jāsalīdzina ar lower() metodi

# līdzīg stringiem meš varam izmanto indeksus
# atšķirība būs ka stringiem būtu simboli
# bet list būs elementi, kas var būt jebkāda tipa, ne tikai simboli

# pirmais foods
print("pirmais ēdiens:", foods[0]) # izdrukā "Kefīrs"
# otrais foods
print("otrais ēdiens:", foods[1]) # izdrukā "Maize"
# trešais foods
print("trešais ēdiens:", foods[2]) # izdrukā "Siers"
# varam iet atkal otrādi
print("pēdējais ēdiens:", foods[-1]) # izdrukā "Siers"
# priekšpēdējais ēdiens
print("priekšpēdējais ēdiens:", foods[-2]) # izdrukā "Maize"
# pirms priekšpēdējais ēdiens
print("pirms priekšpēdējais ēdiens:", foods[-3]) # izdrukā "Kefīrs"
# ja iesim pāri indeksam, tad tiks izmests IndexError
try:
    print(foods[3]) # šeit tiks izmests IndexError, jo sarakstā foods ir tikai 3 elementi
except IndexError:
    print("IndexError: sarakstā foods ir tikai 3 elementi, bet mēs mēģinājām piekļūt 4. elementam.")

# mēs varam arī pievienot elementus sarakstam
foods.append("Piens") # pievieno "Piens" saraksta foods beigās
# būtiski ka append ir pirmā reize kad redzam tā saukto IN PLACE metodi,
#  kas maina sarakstu, nevis atgriež jaunu sarakstu. Tātad foods.append("Piens") maina foods sarakstu, bet neizveido jaunu sarakstu.
# ar IN PLACE mums nevejag = piešķirt, jo saraksts jau ir mainīts, bet ja mēs gribētu izveidot jaunu sarakstu, tad mums vajadzētu izmantot = piešķiršanu.
print(foods) # izdrukā ["Kefīrs", "Maize", "Siers", "Piens"]

# lidzi strings mēs varam izmantot slice operatoru, lai iegūtu daļu no saraksta
print("pirmie divi ēdieni:", foods[0:2]) # izdrukā ["Kefīrs", "Maize"]
# vēl labāk bez 0
print("pirmie divi ēdieni:", foods[:2]) # izdrukā ["Kefīrs", "Maize"]
# pēdejie divi
print("pēdējie divi ēdieni:", foods[-2:]) # izdrukā ["Siers", "Piens"]
# no otrā līdz trešam ieskaitot
print("no otrā līdz trešam ēdienam:", foods[1:3]) # izdrukā ["Maize", "Siers"]
# ja man nebūtu 3 beigās tad būtu visi ēdieni sākot no otra līdz beigām
print("no otrā līdz beigām ēdienam:", foods[1:]) # izdrukā ["Maize", "Siers", "Piens"]

# un protams varam arī apgriezti drukāt sarakstu
print("apgriezti saraksts:", foods[::-1]) # izdrukā ["Piens", "Siers", "Maize", "Kefīrs"]

# līdzīg kā stringiem mēs varam izdrukat pa vienam
for food in foods:
    print(food) # izdrukā katru ēdienu atsevišķi

# starp citu es varu arī izveidot sarakstu ar ar list no range
numbers = list(range(10)) # izveido sarakstu ar skaitļiem no 0 līdz 9
print(numbers) # izdrukā [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# mēs varam arī mainīt kādu vērtību sarakstā, jo saraksts ir mutable (maināms)
foods[0] = "Jogurts" # maina pirmo ēdienu no "Kefīrs" uz "Jogurts"
print(foods) # izdrukā ["Jogurts", "Maize", "Siers", "Piens"]

# varam nomainīt arī pēdejo ēdienu
foods[-1] = "Olas" # maina pēdejo ēdienu no "Piens" uz "Olas"
print(foods) # izdrukā ["Jogurts", "Maize", "Siers", "Olas"]

# savukārt ar append mēs pievienojam jaunu ēdienu saraksta beigās
foods.append("Piens") # pievieno "Piens" saraksta foods beigās
# tagad mums ir 5 ēdieni sarakstā
print(foods) # izdrukā ["Jogurts", "Maize", "Siers", "Olas", "Piens"]
print("Mums ir", len(foods), "ēdiena elementi.") # izdrukā saraksta foods elementu skaitu

# paskatīsimies kas notiksies ja es izmantošu append pievienojot sarakstam sarakstu
foods.append(["Augļi", "Dārzeņi"]) # pievieno sarakstu ["Augļi", "Dārzeņi"] saraksta foods beigās
print(foods) # izdrukā ["Jogurts", "Maize", "Siers", "Olas", "Piens", ["Augļi", "Dārzeņi"]]
# tas varētu nebūt tas ko gribējām, jo tagad mums ir saraksts sarakstā, nevis divi atsevišķi elementi. Ja mēs gribam pievienot vairākus elementus sarakstam, tad mums vajadzētu izmantot extend metodi.

# izmetīsim aŗa šo pēdejo elementu bet saglabāsim to mainīgajā
pedejais = foods.pop() # izmet pēdejo elementu no saraksta foods un saglabā to mainīgajā pedejais
print("Pēdejo elementu izmetām no saraksta foods un saglabājām to mainīgajā pedejais:", pedejais) # izdrukā pēdejo elementu
print(foods) # izdrukā ["Jogurts", "Maize", "Siers  ", "Olas", "Piens"]

# ja gribam "plakani" tad izmantojam extend metodi
foods.extend(["Augļi", "Dārzeņi"]) # pievieno sarakstu ["Augļi", "Dārzeņi"] saraksta foods beigās
# tagad būs plakans saraksts, nevis saraksts sarakstā
print(foods) # izdrukā ["Jogurts", "Maize", "Siers", "Olas", "Piens", "Augļi", "Dārzeņi"]

# ieliksim 9000 mūsu numbers pa vidu kā 4 elementu
numbers[4] = 9000 # maina 4 elementu no 4 uz 9000
print(numbers) # izdrukā [0, 1, 2, 3, 9000, 5, 6, 7, 8, 9]

# kā kārtot te parādas divi varianti viens ir sorted() un otrs ir sort() metodes
# sorted() atgriež jaunu sarakstu, bet sort() maina esošo sarakstu
sorted_numbers = sorted(numbers) # izveido jaunu sarakstu ar kārtotiem skaitļiem
print("Kārtots saraksts ar sorted():", sorted_numbers) # izdrukā [0, 1, 2, 3, 5, 6, 7, 8, 9, 9000]
# vecais saraksts paliek nemainīts
print("Vecais saraksts paliek nemainīts:", numbers) # izdrukā [0, 1, 2, 3, 9000, 5, 6, 7, 8, 9]
# kas notiks ja izmantosim sort uz numbers saraksta?
# tas pats sakārtosies nomainot sevi
numbers.sort() # kārto sarakstu numbers - atkal tā sauktā IN PLACE metode, kas maina sarakstu, nevis atgriež jaunu sarakstu
print("Kārtots saraksts ar sort():", numbers) # izdrukā [0, 1, 2, 3, 5, 6, 7, 8, 9, 9000]

# tagad parunāsim par copy un alias
# sarakstiem = izveidojo alias, jeb shortcut, jeb atsauci uz to pašu sarakstu, datus nekopējot
alias_foods = foods # izveido alias uz sarakstu foods
print(alias_foods) # izdrukā ["Jogurts", "Maize", "Siers", "Olas", "Piens", "Augļi", "Dārzeņi"]
# mainīsim alias_foods sarakstu
alias_foods.append("Vīns")
print("Mainīts alias_foods saraksts:", alias_foods) # izdrukā ["Jogurts", "Maize", "Siers", "Olas", "Piens", "Augļi", "Dārzeņi", "Vīns"]
print("Esošais foods saraksts:", foods) # izdrukā ["Jogurts", "Maize", "Siers", "Olas", "Piens", "Augļi", "Dārzeņi", "Vīns"]

# ja mēs gribam izveidot jaunu sarakstu, kas ir kopija esošā saraksta, tad mums jāizmanto copy() metode
copy_foods = foods.copy() # izveido jaunu sarakstu, kas ir kopija saraksta foods
print("Kopija copy_foods saraksts:", copy_foods) # izdrukā ["Jogurts", "Maize", "Siers", "Olas", "Piens", "Augļi", "Dārzeņi", "Vīns"]
# pieliks klāt viskiju
copy_foods.append("Viskijs") # pievieno "Viskijs" saraksta copy_foods beigās
print("Mainīts copy_foods saraksts:", copy_foods) # izdrukā ["Jogurts", "Maize", "Siers", "Olas", "Piens", "Augļi", "Dārzeņi", "Vīns", "Viskijs"]
# bet esošais saraksts foods paliek nemainīts
print("Esošais foods saraksts paliek nemainīts:", foods) # izdrukā ["Jogurts", "Maize", "Siers", "Olas", "Piens", "Augļi", "Dārzeņi", "Vīns"]

print("Programma beidzās.")