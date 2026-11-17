# Pasniedzēja plāns — 2. nodarbība: nosacījumi un Būla loģika

**Datums:** 2026-11-17 (otrdiena)  
**Laiks:** 17:45–21:40, MS Teams, 12 nodarbību Python kurss pieaugušajiem  
**Interaktīvā vietne:** [docs/lessons/02-types-conditions/index.html](../docs/lessons/02-types-conditions/index.html)  
**Izpildāmie piemēri:** [lessons/02_types_conditions](../lessons/02_types_conditions/README.md)  
**Patstāvīgā prakse:** [exercises/02_types_conditions](../exercises/02_types_conditions/README.md)  
**Priekšzināšanas:** `print`, `input`, mainīgie, skaitļi, virknes, pamata aritmētika.

## Galvenā didaktiskā izvēle

Pēc īsa tipu un `input()` atkārtojuma pāriet uz **programmas vadības plūsmu**: vispirms salīdzinājums dod `bool`, pēc tam `and/or/not` kombinē nosacījumus, un `if/elif/else` izvēlas izpildāmo zaru. HTML lapas viktorīnas un patiesumtabulas palīdz **paredzēt rezultātu**; `.py` faili liek to **pārbaudīt lokālā interpretatorā**. Nepārvērst šo nodarbību par otro pilna apjoma datu tipu lekciju.

Šajā nodarbībā **nav obligāti** `for`, `while`, funkciju definīcijas, vispārīga `try/except` ieviešana vai izvērsts `match/case`. Bonusā var īsi parādīt De Morgana likumus un īssavienojuma izpildi. `match/case` tikai ar Python 3.10+.

## Sasniedzamie rezultāti un diagnosticēšana

| Prasme | Īsa pārbaude |
| --- | --- |
| Konvertē `input()` | Izskaidro, kāpēc `"2.50" * 2` atšķiras no `float("2.50") * 2` |
| Lieto salīdzināšanu | Paredz rezultātu `18 <= vecums < 65` pie `vecums = 18, 65` |
| Saprot Būla loģiku | Nosauc `True and False`, `True or False`, `not True` |
| Saprot zaru secību | Izskaidro, kāpēc `elif punkti >= 90` nestrādā pēc `if punkti >= 60` |
| Lieto saliktus nosacījumus | Izveido intervāla un divu pazīmju pārbaudi |
| Testē robežvērtības | Pārbauda `17/18`, `59/60`, `89/90` un dalītāju `0` |

## Nodarbības norise

### 17:45–18:00 — 1. nodarbības atkārtojums (15 min)

- Atvērt HTML 1. sadaļu un pārbaudīt pamatjēdzienus.
- Atgādināt: `input()` vienmēr atgriež `str`; `int()` un `float()` apstrādā konkrēta formāta tekstu.
- Īss diagnostikas jautājums: `"3" * 2` vai `int("3") * 2`? Kāpēc rezultāti atšķiras?

### 18:00–18:25 — tipu pārveidošana un operatori (25 min)

- Palaist `01_types_conversion.py`; students pirms palaišanas paredz rezultātu.
- Parādīt `int(-3.7) == -3`, kas **nav** matemātiska noapaļošana.
- Uzsvērt: `bool("False")` ir `True`, jo virkne nav tukša.
- `int("divi")` demonstrēt tikai apzināti: pārrunāt `ValueError`, neieviešot `try/except`.

### 18:25–18:55 — salīdzināšana (30 min)

- Palaist `02_comparisons.py`; atšķirt `=` no `==`, izskaidrot `!=`.
- Paredzēt rezultātu pie sliekšņa `60`: `punkti > 60` pret `punkti >= 60`.
- Demonstrēt salīdzinājumu ķēdi `18 <= vecums < 65`; pie `65` rezultāts ir `False`.
- HTML lapas jautājumi kā ātra pašpārbaude.

### 18:55–19:20 — Būla algebra (25 min)

- Izmantot interaktīvo patiesumtabulu un loģikas laboratoriju.
- Palaist `03_boolean_logic.py`; studentiem vispirms paredzēt četrus `and` un `or` rezultātus.
- `not` ar lietus/lietussarga piemēru; precizēt atšķirību starp dabisko valodu un precīzu nosacījumu.

### 19:20–19:30 — pārtraukums (10 min)

### 19:30–20:00 — `if/elif/else` (30 min)

- HTML 4. sadaļa un `04_if_elif_else.py`.
- Kopīgi noteikt, kādu zaru izpildīs temperatūras `-5`, `0`, `16` un `25`.
- Parādīt atkāpes, kolu, izpildes turpināšanos aiz visa bloka.
- Izskaidrot, kāpēc pirmais patiesais `elif` zars aptur atlikušo ķēdi.
- Atsevišķs `if` sāk jaunu, neatkarīgu pārbaudi — neatšķirt to no `elif` ir bieža kļūda.

### 20:00–20:25 — salikti nosacījumi, darba piemērs (25 min)

- `05_compound_conditions.py`: darba laika robežas un ligzdots `if`.
- `06_temperature_advisor.py`: ievadīt temperatūru un `j/n`; izskaidrot programmas secīgās daļas.
- Pārbaudes pāri: `-5/n`, `12/j`, `26/j`, `26/n`, `12/x`.
- Atgādināt, ka `.strip().lower()` ir tikai ērts teksta salīdzināšanas paņēmiens — virkņu metodes padziļināti mācīsimies 3. nodarbībā.

### 20:25–21:05 — patstāvīgā prakse (40 min)

- Visi sāk 1.–3. uzdevumu (skaitļa zīme, pilngadība, vērtējums).
- Ātrākie turpina biļetes cenu un kalkulatoru.
- Aicināt izpildīt testus pie robežām: `-1/0/1`, `17/18`, `59/60`, `74/75`, `89/90`.
- Risinājumus interaktīvajā lapā atvērt tikai pēc patstāvīga mēģinājuma.
- Palīdzības secība: prasīt paredzēto rezultātu → apskatīt ievadi → izsekot pirmajam patiesajam nosacījumam → palaist.

### 21:05–21:30 — apspriede un atkļūdošana (25 min)

- Pārrunāt 1.–3. uzdevuma vienu skaidru risinājumu; uzsvērt korektus robežgadījumus.
- Rādīt kļūdainu `if x == 5 or 10:` un jautāt, kāpēc tas faktiski ir patiess arī, piemēram, pie `x = 3`.
- Kalkulatora gadījumā `b == 0` jāpārbauda pirms `a / b`.
- Ja laiks: salīdzināt divas biļešu atlaides, kas vienlaikus varētu attiekties uz vienu cilvēku; secībai jābūt definētai.

### 21:30–21:40 — noslēgums (10 min)

- Studenti paskaidro, kā `if` atšķiras no atkārtotas izpildes.
- Īss bonusa priekšskatījums: De Morgana likumi un `match/case`, bez obligātiem papildu uzdevumiem.
- Pāreja uz 3. nodarbību 19.11.2026: `if` nosaka **vai**, `for/while` — **cik reižu**.

## Tipiskie jautājumi un kļūdu skaidrojumi

- **Kāpēc `if x = 5:` nedarbojas?** Izteiksmē salīdzināšanai lieto `==`; `=` ir piesaiste.
- **Kāpēc `if x == 5 or 10:` ir nepareizs?** `or` pa labi saņem `10`, kas ir loģiski patiess. Lieto `x == 5 or x == 10`.
- **Vai `bool("False")` atgriež `False`?** Nē, netukša virkne ir patiesa.
- **Kāpēc `elif` zars netika izpildīts?** Tas tiek pārbaudīts tikai tad, ja iepriekšējie nosacījumi bijuši aplami.
- **Vai `15 <= x <= 25` ietver 25?** Jā. `15 <= x < 25` to neietver.
- **Kas notiek, ja `int(input(...))` ievada `abc`?** `ValueError`; strukturētu ievades kļūdu apstrādi vēlāk.
- **Kāpēc `and` un `or` jāsalīdzina ar konkrētām vērtībām?** Dabiskās valodas formulējumi var būt neskaidri; patiesumtabula precizē nozīmi.
- **Kad izmantot ligzdotu `if`?** Ja nākamā pārbaude ir jēgpilna tikai pēc pirmā nosacījuma; izvairīties no nevajadzīgas dziļas ligzdošanas.

## Materiālu pārbaude pirms nodarbības

1. Atvērt 2. nodarbības HTML un pārliecināties, ka patiesumtabula, jautājumu atgriezeniskā saite un papildu sadaļu izvēršana darbojas.
2. Palaist visus sešus pamata `.py` failus ar lokālo Python 3.
3. Izmēģināt temperatūras programmu ar `12/j`, `26/n` un nederīgu `12/x`.
4. Pārbaudīt `07_bonus_logic.py` tikai Python 3.10+ vidē; nekļūdaini izvēlēties `case _`.
5. Pārskatīt 5 uzdevumu testus; tiem jāsakrīt ar HTML 6. sadaļas noteikumiem.
6. Pārliecināties, ka saites uz studenta materiāliem un vingrinājumiem atveras; pārbaudīt Teams demonstrāciju un ierakstīšanu.

## Pedagoģiskā robeža

Šis ir pieaugušo iesācēju kurss ar ierobežotu laiku. Nelietot arhīva 2024/25 skriptus kā obligātu papildu uzdevumu komplektu: to saturs un variants var pārklāties. Ja demonstrē `match/case`, paskaidrot, ka tā ir strukturālā paraugu atbilstība, nevis universāls `if` aizstājējs.

**Pāreja uz 3. nodarbību:** nākamajā lekcijā `if` būs pazīstamais rīks, ar kuru kombinēt `for`, `while`, `range()` un virkņu apstrādi.
