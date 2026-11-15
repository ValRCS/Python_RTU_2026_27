# 4. nodarbība — Kolekcijas: saraksti, vārdnīcas, korteži un kopas

**Datums:** otrdiena, 2026. gada 24. novembris, 17:45–21:40.  
**Mācību vietne:** [Interaktīvā 4. nodarbība](../../docs/lessons/04-collections/index.html)  
**Patstāvīgā prakse:** [5 uzdevumi un testi](../../exercises/04_collections/README.md)  
**Iepriekš:** [3. nodarbība — cikli un virknes](../03_loops_strings/README.md).

## Sasniedzamie rezultāti

Pēc nodarbības students spēj:
1. Veidot `list`, izmantot `len()`, indeksus, negatīvus indeksus un šķēlumus, papildināt un mainīt elementus.
2. Apstrādāt sarakstu ar `for`; saprast, kāpēc `append()` modificē sarakstu un atgriež `None`.
3. Pārveidot tekstu par vārdu sarakstu ar `split()` un salikt tekstu ar `join()`.
4. Veidot `dict`, piekļūt vērtībām pēc atslēgas, atjaunināt, pārbaudīt `in` un iterēt ar `items()`.
5. Saskaitīt vārdu biežumu ar ciklu un vārdnīcu, paskaidrot `get(key, default)` lietojumu.
6. Atšķirt `tuple` no `list` pēc nemaināmības un indeksa piekļuves.
7. Papildus: izmantot `set` unikālu elementu iegūšanai un dalības pārbaudei.

## Četri kolekciju veidi

| Tips | Piemērs | Secība un piekļuve | Maināms | Galvenais pielietojums |
| --- | --- | --- | --- | --- |
| `list` | `["ābols", "piens"]` | Saglabā secību; piekļuve pēc indeksa | Jā | Secīgi elementi, kas var mainīties |
| `tuple` | `(56.95, 24.10)` | Saglabā secību; piekļuve pēc indeksa | Nē* | Fiksēta vērtību secība |
| `dict` | `{"ābols": 3}` | Saglabā ievietošanas secību; piekļuve pēc atslēgas | Jā | Atslēga un tai piesaistīta vērtība |
| `set` | `{"ābols", "piens"}` | Nav pozicionālas indeksācijas; secība nav garantēta | Jā | Unikāli elementi un piederība |

* Korteža elementu piesaistes nav maināmas; īsajā kursā lietojam kortežus ar vienkāršām nemaināmām vērtībām.

## Nodarbības grafiks

| Laiks | Temats |
| --- | --- |
| 17:45–18:00 | Atkārtojums: `str`, `for`, indeksi un šķēlumi |
| 18:00–18:50 | Saraksti: izveide, piekļuve, `append`, maiņa, iterācija |
| 18:50–19:10 | Teksta un saraksta saistība: `split` un `join` |
| 19:10–19:25 | Vārdnīcas: atslēgas un vērtības |
| 19:25–19:35 | Pārtraukums |
| 19:35–20:10 | Vārdnīcas: `items`, `get`, biežumu skaitīšana |
| 20:10–20:25 | Korteži: fiksēta secība un nemaināmība |
| 20:25–21:05 | Patstāvīgā prakse: 3 pamata un 2 papildu uzdevumi |
| 21:05–21:25 | Uzdevumu apspriede un atkļūdošana |
| 21:25–21:35 | Kopas: izvēles demonstrācija |
| 21:35–21:40 | Noslēgums un pāreja uz funkcijām |

## Python piemēru palaišana

Pietiek ar Python 3; ārējas pakotnes nav vajadzīgas. Terminālī no repozitorija saknes:

~~~powershell
python lessons/04_collections/01_lists.py
python lessons/04_collections/02_split_join.py
python lessons/04_collections/03_dictionaries.py
python lessons/04_collections/04_tuples_sets.py
python lessons/04_collections/05_combined.py
~~~

Mac/Linux lieto `python3`, ja `python` nav pieejams. Piemēri ir neinteraktīvi un bez failu lasīšanas/rakstīšanas, lai tos var droši palaist un mainīt.

## Būtiskais un papildu saturs

**Obligāti:** `list` un `dict`; `len`, `for`, piekļuve, modificēšana, `append`, `split`/`join`, `dict.get` un `items`; īss `tuple` ievads.  
**Pēc iespējas:** `remove`, `pop`, `sum`/`min`/`max`, `sorted`, `set` un dublikātu noņemšana.  
**Vēlāk:** comprehensions, `Counter`, dziļi iegultas kolekcijas, paplašināta kopu algebra, sarežģīta kļūdu apstrāde un funkciju definēšana.

## Prakses piezīmes

- `append()` maina sākotnējo sarakstu; `new_list = old_list.append(x)` **nav** jauna saraksta veidošana.
- `words = text.split()` dod `list`; `" ".join(words)` atgriež `str`.
- `"vārds" in student` meklē vārdnīcas **atslēgu**, nevis vērtību.
- `dict[key]` var izraisīt `KeyError`; `dict.get(key, default)` ļauj sniegt noklusējumu.
- `{ }` jeb `{}` ir tukša vārdnīca; tukša kopa ir `set()`.
- `list` un `tuple` saglabā secību; `set` elementiem nav garantēta iterācijas secība.
- `split()` bez argumenta sadala pēc atstarpēm un citiem whitespace; tas neatdala pieturzīmes no vārdiem.

## Saites

- [Oficiālā Python pamācība par datu struktūrām](https://docs.python.org/3/tutorial/datastructures.html)
- [2024/25 sarakstu piemēri](https://github.com/ValRCS/Python_RTU_2024_25/tree/main/topic_6_lists)
- [2024/25 vārdnīcu piemēri](https://github.com/ValRCS/Python_RTU_2024_25/tree/main/topic_8_dictionary)
- [2024/25 kortežu un kopu piemēri](https://github.com/ValRCS/Python_RTU_2024_25/tree/main/topic_9_tuples_sets)

**Nākamreiz (26. novembrī):** funkcijas, moduļi un pirmie testi. Pazīstamo vārdu biežuma kodu pārveidosim par `def count_words(text)` funkciju.
