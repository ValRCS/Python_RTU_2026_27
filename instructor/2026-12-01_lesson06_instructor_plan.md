# Pasniedzēja plāns — 6. nodarbība: faili, ceļi un CSV

**Datums:** 2026-12-01, 17:45–21:40, MS Teams  
[Studentu lapa](../docs/lessons/06-files-csv/index.html) · [Īsie piemēri](../lessons/06_files_csv/README.md) · [Live coding](../lessons/06_files_csv/live_coding/README.md) · [Uzdevumi](../exercises/06_files_csv/README.md) · [Dati](../datasets/README.md)

## Didaktiskais pamatojums
Pāreja no input/print uz ilglaicīgu glabāšanu. Saglabāt 5. nodarbības funkciju, kolekciju, importu un assert idejas. Datu plūsma: lasīšana → apstrāde → saglabāšana. Failu ceļi ir galvenais tehniskais risks. Ārējās pakotnes, JSON un notebooks atstāt 7. nodarbībai.

## Sasniedzamie rezultāti
| Mērķis | Pārbaude |
|---|---|
| Atšķir darba mapi un skripta mapi | Paredz Path.cwd un __file__ |
| Nolasa UTF-8 tekstu | 5 rindas, 5 vārdi |
| Raksta ar w un a | Atsevišķas palaišanas, 2 rindas |
| Atšķir str no bytes | Rīga: 4 rakstzīmes, 5 baiti |
| Lieto DictReader un float | 10 ieraksti, 35.00 EUR |
| Apkopo un eksportē | 4 kategorijas, 5 food ieraksti |
| Apstrādā paredzamas kļūdas | Nepareizs ceļš, nederīga summa |

## Stundas gaita

### 17:45–18:00 — atkārtojums
- Atvērt 5. nodarbības count_words un standarta bibliotēkas piemērus. Kas notiek ar mainīgajiem pēc programmas beigām?
- Atjaunināt repozitoriju, atvērt sakni VS Code; terminālī pārbaudīt python --version un darba mapi. ZIP lietotājiem Git nav obligāts.

### 18:00–18:20 — ceļi
- 01_paths.py un live_coding/01_paths_live.py: palaist no saknes, tad no lessons/06_files_csv ar python live_coding/01_paths_live.py; salīdzināt cwd, resolve, is_file.
- Atgriezties saknē. Windows disku burti, / un raw string. 02_directory_exploration.py: name, stem, suffix, glob; rglob izvēles.
- Pajautāt: kāpēc fails eksistē, bet open to neatrod?

### 18:20–18:40 — lasīšana
- 03_reading_text_live.py: read → str, readline, readlines → list, for line in file; repr un otrais read faila beigās.
- strip vs rstrip("\n"), atmiņa. 05_encoding_live.py: Rīga 4 rakstzīmes/5 baiti. 12_binary_files_bonus.py īss rb/wb piemērs visiem (5 min).
- Ja kavējas, izlaist detalizētu readlines salīdzinājumu, nevis bināro demonstrāciju.

### 18:40–18:50 — pārtraukums

### 18:50–19:10 — rakstīšana
- 04_writing_text_live.py: w Rīga, a Cēsis, r, w Liepāja. Atvērt output/lesson06/modes.txt, prognozēt saturu.
- mkdir, write bez jaunrindas; avota datus nekad nepārrakstīt. 04_filter_text.py vienādu ceļu aizliegums.

### 19:10–19:30 — funkcijas un teksts
- 06_text_processing_live.py: read_text → count_words → save_word_counts. Rīga 2; tukšs teksts. Algoritms strādā arī bez faila.
- Pēc laika: Rainis/Veidenbaums fragmenti, tukšās rindas, pieturzīmes. Neuzspiest Counter vai regex.

### 19:30–19:40 — pārtraukums

### 19:40–20:00 — CSV
- Atvērt expenses.csv kā tekstu; galvene, atdalītājs, pēdiņas. 07_csv_reading_live.py salīdzināt reader, DictReader un split.
- 08_csv_analysis_live.py: str, float, running total, dict.get; 10 ieraksti, 35.00 EUR.
- products_lv.csv: semikols, decimālkomats, utf-8-sig; Excel .xlsx nav CSV.

### 20:00–20:20 — rakstīšana un kļūdas
- 09_csv_writing_live.py: writeheader, writerow, pārtikas 5 ieraksti; atvērt rezultātu.
- 10_file_debugging_live.py: neesošs fails, abc, tukšs, NaN, negatīvs; 2 derīgi, 4 nederīgi. Galvenes pārbaude, reader.line_num ir fiziskā beigu rinda.
- Ja kavējas, tikai neesošs fails un ValueError; pārējais pēc prakses.

### 20:20–21:05 — patstāvīgais darbs (45 min)
- 6.1–6.4; starter.py pēc izvēles; 10+10+15+10 min. Vispirms pašiem, tad details.
- Ātrākajiem 6.5–6.15; 6.7–6.9 kā alternatīvas demonstrācijām.
- Diagnostika: cwd, faila esamība, kolonnu nosaukumi, float; viens padoms pirms risinājuma.

### 21:05–21:20 — apspriede
- Četri uzdevumi; tukšs fails, neviena atbilstoša rinda, nepareiza galvene. Apskatīt output, ne tikai print.
- Salīdzināt funkciju ar tiešu kodu, pārbaudīt citu ievadi.

### 21:20–21:35 — papildu
- 11_batch_processing_bonus.py: glob, 2 un 1 rinda; Decimal no teksta; reģionālais CSV; pēc vajadzības rb/wb atkārtojums.

### 21:35–21:40 — noslēgums
- Kur sākas relatīvais ceļš? Kāpēc w bīstams? Kāpēc CSV skaitlis jāpārveido?
- 7. nodarbībā tie paši izdevumi → JSON → notebook un grafiks.

## Tipiskās kļūdas
| Simptoms | Diagnostika |
|---|---|
| FileNotFoundError | Path.cwd(), resolve(), is_file(), VS Code terminālis |
| UnicodeDecodeError | Noskaidrot kodējumu; neignorēt |
| Tukšs otrais read | Pozīcija beigās |
| Pazudis saturs | w saīsina failu atvēršanas brīdī |
| Salipušas rindas | write nepievieno jaunrindu |
| KeyError | Galvene, atdalītājs, BOM |
| ValueError / NaN | Skaitļu validācija |
| Nepareiza summa | str pārveide, skaits, kategorijas un decimālatdalītājs |

## Sagatavošana
- Palaist 8 īsos skriptus, 12 live coding skriptus (04 ar w/a/r) un bonus_solutions.py no saknes.
- `python -m unittest discover -s exercises/06_files_csv -p "test_*.py" -v`
- `python -m unittest discover -s tests -v`
- Pārbaudīt avotu nemainību, JS laboratorijas, kopēšanu, 10 sadaļu progresu, mobilo skatu, navigāciju un Teams ekrāna kopīgošanu.
