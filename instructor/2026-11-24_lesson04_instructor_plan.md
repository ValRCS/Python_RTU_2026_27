# Pasniedzēja plāns — 4. nodarbība: kolekcijas

**Datums:** 2026-11-24 (otrdiena), **17:45–21:40**, MS Teams  
**Mācību lapa:** [docs/lessons/04-collections/index.html](../docs/lessons/04-collections/index.html)  
**Izvērstie dzīvās programmēšanas piemēri:** [live_coding](../lessons/04_collections/live_coding/README.md) · [Papildu uzdevumi](../exercises/04_collections/bonus.md)

**Python piemēri:** [lessons/04_collections](../lessons/04_collections/README.md)  
**Patstāvīgā prakse:** [exercises/04_collections](../exercises/04_collections/README.md)

## Galvenā didaktiskā izvēle

Vienā nodarbībā parādīt **visus četrus** Python kolekciju veidus, bet **75–80% satura uzmanības atvēlēt `list` un `dict`**. `tuple` ir īsa jau zināmas indeksējamas secības nemaināma alternatīva. `set` pamati (unikālums, piederība, `set()`) jāparāda visiem; kopu algebra ir izvēles tēma pēc pamatprakses. Sāc ar problēmu: trīs mainīgie nav ērts veids, kā glabāt 30 produktu nosaukumus. Nākamais jautājums: ja produktam jāpiesaista cena vai skaits, kāpēc ar vienu sarakstu nepietiek?

## Priekšzināšanas un sasniedzamie rezultāti

Studenti jau pazīst mainīgos, `str`, `for` un `while`, `if`, `len`, indeksus, šķēlumus, `strip` un `lower`. `split` un `join` apzināti atlikti no 3. nodarbības uz 4. nodarbību.

| Sasniedzamais rezultāts | Īsā pārbaude |
| --- | --- |
| `list` veidošana, indeksi, mutācija, `append`, `for` | Students izskaidro gala sarakstu pēc trim darbībām |
| `str.split` un `str.join` | Students pārveido teikuma otro/trešo vārdu un atjauno tekstu |
| `dict` atslēgas, atjaunināšana, `items` | Students no vārdnīcas izdrukā konkrētu vērtību un visas pāru attiecības |
| `get` un vārdu biežums | Students saskaita vārdus `"rīga rīga python"` |
| `tuple` nemaināmība | Students paredz `TypeError`, mēģinot aizstāt elementu |
| Papildus: `set` unikālums | Students pasaka, cik unikālu vārdu ir sarakstā |

## Detalizētais nodarbības grafiks

### 17:45–18:00 — atkārtojums (15 min)

- 4 jautājumi par `for`, `str` indeksāciju un šķēlumiem; studenti prognozē pirms pārbaudes.
- Uz ekrāna `text = "Rīga"`; `text[0]`, `text[-1]`, `len(text)`; atgādināt, ka `str` nemainās.
- Demonstrē: `products = ["ābols", "piens", "maize"]`, `products[0]` — tā pati indeksācijas ideja, cits datu tips.

### 18:00–18:50 — saraksti (50 min)

- Izveide, `[]`, `len`, indeksi, negatīvie indeksi, šķēlumi: kopīga terminoloģija ar 3. nodarbību.
- Palaist [01_lists_live.py](../lessons/04_collections/live_coding/01_lists_live.py) pa blokiem: prognoze → izpilde → viena datu izmaiņa. Īsais `01_lists.py` paliek atkārtojumam.
- [02_list_processing_live.py](../lessons/04_collections/live_coding/02_list_processing_live.py): atlase ar `if` un `append`, vidējais un tukšs saraksts; `--input` tikai pēc vajadzības. `sorted` pret `sort`, `extend` un `enumerate` pēc laika; aliasing un comprehension tikai papildus.
- Parādīt `append`, aizstāšanu ar `fruits[1] = ...`, `remove`, `pop`, `for fruit in fruits`.
- Uzsvērt `append()` atgriež `None`. Demonstrēt kļūdu `fruits = fruits.append("x")` tikai ar rezerves kopiju/jaunu sarakstu.
- `sum`, `min`, `max` ar skaitļu sarakstu; neuzkraut visu metožu katalogu.
- Interaktīvais List Explorer: pievienot, aizstāt, izņemt; pamanīt, kur mainās indeksi.

### 18:50–19:10 — `split` un `join` (20 min)

- [03_split_join_live.py](../lessons/04_collections/live_coding/03_split_join_live.py): whitespace, komats, `strip`, tukšas daļas un `join` ar skaitļiem. Īsais `02_split_join.py`: teikums → vārdu saraksts → viena elementa maiņa → teikums.
- `split()` bez argumentiem sadala pēc tukšuma rakstzīmēm; `split(",")` izmanto norādītu atdalītāju.
- `" ".join(words)` **ir virknes metode**, kas savieno virkņu elementus; ne `words.join(" ")`.
- Interaktīvajā laboratorijā nomainīt vidējo vārdu, salīdzināt sākotnējo un gala tekstu.

### 19:10–19:25 — vārdnīcas pamati (15 min)

- [04_dictionaries_live.py](../lessons/04_collections/live_coding/04_dictionaries_live.py): pirmais bloks pirms pārtraukuma, iterācija un atjaunināšana pēc tā.
- `{"vārds": "Anna", "vecums": 28}`: atslēga → vērtība; nevis pozīcija → vērtība.
- Piekļuve `student["vārds"]`; izmaiņas un jaunas atslēgas.
- Kontrasts starp `[]` un `{}`; tukša `dict` ir `{}`.
- Nezināma atslēga izraisa `KeyError`: parādīt `get("e-pasts", "nav norādīts")`.

### 19:25–19:35 — pārtraukums (10 min)

### 19:35–20:10 — vārdnīcas darbībā (35 min)

- [04_dictionaries_live.py](../lessons/04_collections/live_coding/04_dictionaries_live.py): turpināt ar `keys` (vai tiešu iterāciju), `values`, `items`. Īsais `03_dictionaries.py`: `in` pārbauda **atslēgu**; `items()` dod atslēgas un vērtības.
- [05_frequency_analysis_live.py](../lessons/04_collections/live_coding/05_frequency_analysis_live.py): vārdu skaitītājs: `text.lower().split()`, tukša vārdnīca, `for word`, `if word in counts`; pa soļiem vērot izmaiņas.
- Tikai pēc izskaidrošanas demonstrēt `counts[word] = counts.get(word, 0) + 1`.
- Dictionary Explorer un Frequency Counter: `rīga python rīga` → `{"rīga": 2, "python": 1}`.
- Pieminēt, ka vārdnīcas saglabā ievietošanas secību, bet tās **nav** saraksti un nepieprasa secīgus skaitļu indeksus.

- Pēdējās 5–7 minūtes: [06_shopping_basket_live.py](../lessons/04_collections/live_coding/06_shopping_basket_live.py), daudzumi un zināmo cenu summa. Ja nepietiek laika, atstāt apspriedei; neatrisināt precīzi prakses uzdevumu.

### 20:10–20:20 — korteži un kopu minimums (10 min)

- Pirmās 7 minūtes: [07_tuples_live.py](../lessons/04_collections/live_coding/07_tuples_live.py), īsi arī izpakošana `latitude, longitude = coordinates`.
- `coordinates = (56.95, 24.10)`; `coordinates[0]` un `len(coordinates)`.
- Salīdzināt ar sarakstu; parādīt, kāpēc `coordinates[0] = 57.0` izraisa `TypeError`.
- `single = (5,)` pret `(5)`; skaidrot īsi; nākamajā nodarbībā lietosim izpakošanu funkciju piemēros.
- Nesākt dziļu diskusiju par hashability, mutējamām vērtībām kortežos vai ligzdotām kolekcijām.

- Pēdējās 3 minūtes: [08_sets_bonus.py](../lessons/04_collections/live_coding/08_sets_bonus.py) pirmais bloks — `set()`, unikālums, `in`, `add`. Pilnu kopu algebru atstāt noslēgumam.

### 20:20–21:05 — patstāvīgais darbs (45 min)

- Visi mēģina 1.–3. uzdevumu: ievades saraksts; vārdu biežums; cena no saraksta un vārdnīcas.
- Ātrākie pilda 4. un 5. (korteži un kopas), pēc tam [A–G papildu uzdevumus](../exercises/04_collections/bonus.md).
- Vispirms piedāvāt vienu padomu, nevis atrisināt studentu vietā.
- Testi: tukšs saraksts; `BEIGT`; atkārtoti vārdi; tukša virkne; atkārtots produkts; nezināma cena papilduzdevumā.
- Kad risinājums nostrādā vienam testam, pieprasīt citu testu; neizvērtēt tikai ekrānā izdrukātu laimīgu gadījumu.

### 21:05–21:25 — risinājumu apspriede (20 min)

- Izmantot [09_debugging_collections.py](../lessons/04_collections/live_coding/09_debugging_collections.py) izvēlētus blokus; kļūdu tipi, tukša saraksta vidējais, aliasing vai dzēšana iterācijas laikā.
- Izvērtēt vismaz vienu dažādu risinājumu 1.–3. uzdevumam.
- Pārrunāt, vai `append` dod jaunu sarakstu; kāpēc `get` palīdz; kāpēc grozā jāskaita atkārtoti elementi.
- Ja pamatuzdevumi neietilpst laikā, atvēlēt vairāk minūšu diskusijai un izlaist kopu demonstrāciju.

### 21:25–21:35 — kopu algebra un papildu demonstrācijas (10 min, pēc vajadzības)

- `set(["Anna", "Jānis", "Anna"])` atgriež unikālus elementus.
- `set()` pret `{}`; `in`; indeksa trūkums un negarantēta iterācijas secība.
- [08_sets_bonus.py](../lessons/04_collections/live_coding/08_sets_bonus.py) turpinājums: `&`, `|`, `-`, `^`; pangramma tikai ātrākajiem. Papildus `group_a & group_b`. Demonstrācijā izdrukāt `sorted(unique_names)`, nepaļauties uz nejaušu kopas attēlošanas secību.

### 21:35–21:40 — noslēgums (5 min)

- Jautājums: kuru datu struktūru izvēlēties produktu sarakstam, cenrādim, koordinātām, unikāliem vārdiem?
- 5. nodarbībā pazīstamais vārdu biežuma cikls kļūs par `def count_words(text)` funkciju.

## Tipiskās kļūdas un labojumi

| Kļūda | Ko demonstrēt |
| --- | --- |
| `fruits = fruits.append("x")` | `append` maina list un atgriež `None` |
| `fruits[3]` trīs elementu sarakstā | `IndexError`; pēdējais indekss ir 2 |
| `words.join(" ")` | Pareizi `" ".join(words)` |
| `student["nezināms"]` | `KeyError`; `get` un droša noklusējuma vērtība |
| `"Anna" in student` | Vārdnīcā `in` meklē atslēgu, ne vērtību |
| `tuple.append(...)` vai `tuple[0] = ...` | Korteža nemaināmība |
| `{}` kā tukša kopa | `{}` ir dict; jālieto `set()` |
| Pieņēmums, ka `set` izdrukas secība ir garantēta | `sorted(set(...))` reproducējamam attēlojumam |

## Sagatavošanās un tehniskā pārbaude

1. Palaist piecus īsos un deviņus `live_coding/*.py` skriptus, kā arī `exercises/04_collections/bonus_solutions.py` ar Python 3. Papildus `--input`: pārbaudīt nederīgu skaitli, tukšu ievadi un BEIGT.
2. Pārbaudīt mācību vietni datorā un telefonā; navigāciju, kopēšanas pogas un sadaļu progresu.
3. Pārbaudīt 25 viktorīnas jautājumus, īpaši `append`, `join`, `get` un `set()`.
4. Pārbaudīt List Explorer robežas un darbības ar tukšu sarakstu, Dictionary Explorer neesošu atslēgu, Frequency Counter tukšu ievadi.
5. Pārbaudīt, ka pārlūka demonstrācijas **modelē** Python un neizpilda ievadītu Python kodu.
6. Pārbaudīt uzdevumu 3 kopējo cenu: 1.50 + 0.60 + 0.60 + 1.20 = **3.90 EUR**.
7. Atvērt Teams, koda redaktoru un vietni; apskatīt ierakstīšanu un ekrāna kopīgošanu.
8. Pārbaudīt atpakaļ/sākums/nākamā nodarbība saites.

## Materiālu robežas un turpinājums

Neievadīt `def`, `Counter`, ligzdotu struktūru apstrādi vai smalku hashability teoriju kā pamatsaturu. `try/except` atkārtojam jau zināmā formā; list comprehension un aliasing tikai pēc pamatprasmēm. Īsi paskaidrot, ka `list` ir vispārīga secība, nevis specializēts skaitliskais masīvs (NumPy vēlāk). Iepriekšējo gadu `topic_6_lists`, `topic_8_dictionary` un `topic_9_tuples_sets` piemēri lietojami kā atsauce, nevis kā obligāta 12 nodarbību kursa papildslodze.
