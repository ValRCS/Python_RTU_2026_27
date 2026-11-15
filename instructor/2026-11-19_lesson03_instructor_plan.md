# Pasniedzēja plāns — 3. nodarbība: cikli un virknes

**Datums:** 2026-11-19 (ceturtdiena)  
**Laiks:** 17:45–21:40, MS Teams, 12 nodarbību Python kurss pieaugušajiem  
**Pamata lapa:** [docs/lessons/03-loops-strings/index.html](../docs/lessons/03-loops-strings/index.html)  
**Studentu kods:** [lessons/03_loops_strings](../lessons/03_loops_strings/README.md)  
**Prakse:** [exercises/03_loops_strings](../exercises/03_loops_strings/README.md)  
**Priekšzināšanas:** mainīgie, `int/float/str/bool`, `input`, salīdzināšana, `if/elif/else`, `and/or/not`.

## Galvenā didaktiskā izvēle

Apvienot **ciklus un virknes** vienā nodarbībā. Virkne ir nemaināma secība, tāpēc ļauj dabiski demonstrēt `for`, `len`, indeksus un šķēlumus. 4. nodarbībā šie paši mehānismi pāriet uz `list` un `tuple`; `split` un `join` apzināti atlikt līdz tam, jo `split()` atgriež sarakstu.

**Nepārslogot:** neievadīt funkciju definīcijas, list comprehensions, regulārās izteiksmes, izvērstu Unicode normalizāciju vai vispārīgu kļūdu apstrādes arhitektūru. `break` demonstrēt, `continue` īsi, detalizētāk — ja laiks atļauj.

## Sasniedzamie rezultāti un novērtēšana

| Rezultāts | Kā pārbaudīt |
| --- | --- |
| `for` ar `range`, stop ir ekskluzīvs | students paredz iterāciju skaitu un summu |
| `while` ar garantētu apstāšanos | students izskaidro, kas mainās katrā iterācijā |
| `if` kopā ar cikliem | students skaita tikai atlasītas vērtības |
| Iterācija pār `str` | students saskaita patskaņus |
| Indeksi/šķēlumi/nemaināmība | students nosaka `text[-1]`, `[1:4]` un kļūdas gadījumus |
| Praktiskas `str` metodes | students ievadi normalizē ar `strip().lower()` |

## Detalizēts pasniegšanas grafiks

### 17:45–18:05 — atkārtojums (20 min)
- Atgādināt `input()` vienmēr ir `str`; `int("abc")` izraisa `ValueError`.
- Pieci automātiski pārbaudāmi jautājumi tīmekļa lapā.
- Īss iesildīšanās piemērs: `if n % 2 == 0`.
- Pāreja: `if` izvēlas **vai**, cikls — **cik reižu**.

### 18:05–18:50 — `for` / `range()` (45 min)
- Vispirms `for n in range(5)`; pēc tam `range(1, 6)` un `range(2, 10, 2)`.
- Modelēt pa vienam solim tīmekļa laboratorijā. Uzsvērt ekskluzīvu `stop`.
- Atvērt `01_for_range.py`: `total = 0` un `total += n`; izskaidrot akumulatoru.
- Kontroljautājumi: `range(0)`, `range(5,5)`, `range(10,0,-2)`.
- Ātra pašpārbaude un viena minūte studentu prognozēm pirms izpildes.

### 18:50–19:25 — `while` un vadība (35 min)
- `i=0; while i<4: i+=1`. Pēc katras iterācijas nosaukt `i`.
- Parādīt bezgalīgas cilpas **koda fragmentu**, nepalaižot to bez uzraudzības; demonstrēt Ctrl+C.
- Ieviest signālvārdu `beigt` ar `strip().lower()` un `break`.
- Īsi salīdzināt `break` (iziet no cikla) un `continue` (izlaiž atlikušo iterāciju).
- Atvērt `02_while.py`; uzdot jautājumu: kādi ievades varianti pārtrauc ciklu?

### 19:25–19:35 — pārtraukums (10 min)

### 19:35–20:05 — virkņu secības (30 min)
- `for char in "Rīga"`, `len("Rīga") == 4`, `in` operatora nozīme.
- `text[0]`, `text[-1]`, `text[1:3]`, `text[::-1]`, ārpus robežām un tukša virkne.
- Izmantot indeksa laboratoriju ar reālajiem latviešu burtiem.
- Nemaināmība: `text[0]="L"` izraisa `TypeError`; `"L" + text[1:]` izveido jaunu virkni.
- Pieminēt Unicode koda punktus, neiedziļinoties normalizācijā.

### 20:05–20:25 — virkņu metodes (20 min)
- Parādīt `strip`, `lower`, `upper`, `replace`, `count`, `startswith`, `endswith`.
- Salīdzināt sākotnējo un atgriezto virkni; nenozīmēt metodi kā inplace izmaiņu.
- Laboratorijā izmēģināt virkni ar atstarpēm, lielajiem burtiem, atkārtojumiem.
- `split/join` atlikt uz nākamo reizi (saraksti).

### 20:25–21:05 — patstāvīgie uzdevumi (40 min)
- Visi sāk 1.–3. uzdevumu; ātrākie turpina 4.–5.
- Atgādināt testus: n=0/1/10; `beigt` ar reģistru/atstarpēm; `Rīga` un `Ābols`.
- Iesācējiem palīdzēt ar atkāpēm, datu tipu un cikla beigu nosacījumu.
- Risinājumi lapā ir paslēpti zem `details` — atverami **pēc sava mēģinājuma**.
- Nenorādīt risinājumu priekšlaikus; sniegt vienu padomu, tad prasīt studentam palaist savu kodu.

### 21:05–21:30 — kopīga izvērtēšana (25 min)
- Izvēlēties 1.–3. uzdevumu; analizēt biežas kļūdas: `range(1,n)` bez n, `i += 1` trūkums, `text.lower` bez iekavām, `IndexError`.
- Salīdzināt `for char in text` un `for i in range(len(text))`; otrs vajadzīgs tikai tad, ja svarīgs indekss.
- Ja laiks: minēšanas spēle un alternatīva palindroma pārbaude.

### 21:30–21:40 — noslēgums (10 min)
- Vaicāt, kāpēc gan virkni, gan `range` var lietot ar `for`.
- Parādīt 4. nodarbības solījumu: `languages = ["Python", "Java"]` un `languages[0]`.
- Norādīt studentu materiālu lapu un nākamās nodarbības datumu 24.11.2026.

## Iepriekš sagatavojamie materiāli un pārbaudes

1. Atvērt 3. nodarbības GitHub Pages lapu; pārliecināties, ka izvēlne un navigācija darbojas.
2. Pārbaudīt 25 viktorīnas jautājumus; īpaši `range` robežas, `while` beigu nosacījumus, negatīvos indeksus.
3. Pārbaudīt JavaScript modeļus: `range(1,6)`; `range(10,0,-2)`; solis 0; tukša virkne; ārpus robežām esošs indekss; visu virkņu metožu rezultāti.
4. Palaist visus četrus `.py` failus; interaktīvajiem ievadīt `beigt` un `7`.
5. Pārbaudīt MS Teams ekrāna kopīgošanu, koda fonta palielināšanu, ierakstīšanu.
6. Atvērt 4. nodarbības lapu tikai kā priekšskatījumu; nepārnest tajā apgūstamos sarakstus uz 3. nodarbību.

## Tipiskas kļūdas un atbildes

- **`range(1, 5)` ietver 5?** Nē; ietver 1,2,3,4.
- **`while` vienmēr beigsies?** Nē; jāmaina nosacījumu ietekmējošais stāvoklis vai jāizpilda `break`.
- **`continue` un `break` vienādi?** Nē; pirmais pārlec uz nākamo iterāciju, otrais iziet no cikla.
- **`text[-1]` vienmēr der?** Neder tukšai virknei.
- **`text[1:100]` kļūdains?** Šķēluma robeža var pārsniegt garumu; rezultāts būs saīsināts.
- **`text.replace("a", "b")` modificē text?** Nē; atgriež jaunu `str`.
- **`len` ir baitu vai vizuālo burtu skaits?** Python `str` garums koda punktos; grafēmu klasteri var atšķirties.
- **`isdigit()` droša skaitļu ievadei?** Ne vispārīgi; negatīvus skaitļus un vairākus citus pierakstus tā neatrisina.

## Pāreja uz 4. nodarbību

Atkārtot `len()`, `for`, `[0]`, `[-1]`, `[start:stop]` uz `list`; atšķirība: saraksti ir maināmi, virknes — ne. Vārdnīcās piekļuve notiek pēc atslēgas, nevis pozicionāla indeksa. `split()` un `join()` kā dabisks tilts no `str` uz `list`.
