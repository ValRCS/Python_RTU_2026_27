# Pasniedzēja plāns — 5. nodarbība: funkcijas, moduļi un testi

**Datums:** 2026-11-26 (ceturtdiena), **17:45–21:40**, MS Teams  
**Studentu tīmekļa lapa:** [docs/lessons/05-functions-modules/index.html](../docs/lessons/05-functions-modules/index.html)  
**Python piemēri:** [lessons/05_functions_modules](../lessons/05_functions_modules/README.md)  
**Prakse:** [exercises/05_functions_modules](../exercises/05_functions_modules/README.md)

## Didaktiskais pamatojums

Šī ir pāreja no atsevišķa algoritma pie **atkārtoti izmantojamas un pārbaudāmas programmas daļas**. Lielāko uzmanību (aptuveni 65–70%) veltīt funkcijām, 15–20% moduļiem, atlikumu pārbaudēm. Nemainīt pazīstamo algoritmu — 4. nodarbības vārdu biežums un groza cena ir tilts, nevis jauna problēma.

**Svarīgākā diagnostika:** studenti mēdz sajaukt `print` un `return`, funkcijas definēšanu ar izsaukšanu, parametrus ar argumentiem un lokālos mainīgos ar ārējiem. Katrā piemērā prasīt **prognozi pirms palaišanas**. Saglabāt īsus `.py` skriptus; pārlūka JavaScript demonstrācijas nav Python izpildvide.

**Saistība ar kursu:** 1.–4. nodarbībās apgūtas izteiksmes, `if`, cikli, virknes, saraksti un vārdnīcas; 6. nodarbībā `read_text(path)` izmantos `count_words(text)`. Oficiālais plāns skaidri ietver funkcijas, moduļus un vienību testu pamatus. Pakotņu uzstādīšana, Jupyter/Colab un JSON apzināti paliek 7. nodarbībā.

## Sasniedzamie rezultāti un īsas pārbaudes

| Mērķis | Pārbaude stundā |
| --- | --- |
| Uzraksta `def`, pareizi atkāpina un izsauc | Nosauc, kurā rindā pirmoreiz izpildās funkcijas ķermenis |
| Atšķir parametrus un argumentus | Parāda `name` un `"Anna"` funkcijā `greet(name)` |
| Saprot `return` pret `print` | Paredz `a = double_a(5)` un `b = double_b(5)` |
| Lieto lokālos mainīgos | Izskaidro, kāpēc ārējais `city` paliek `"Rīga"` |
| Izveido un izmanto pielāgotu moduli | Palaiž `05_modules/main.py` |
| Izmanto `assert` trīs ievadēm | Pārbauda `""`, vienu vārdu un atkārtojumus |
| Papildus `unittest` | Palaiž testu atklāšanu ar `python -m unittest discover` |

## Stundas gaita

### 17:45–18:00 — atkārtojums (15 min)
- Atvērt iepriekšējo vārdu skaitītāju un groza piemēru; jautāt, kā šo kodu lietot **vairākiem dažādiem tekstiem**, nekopējot ciklu.
- Četri īsi jautājumi par `dict.get`, `split`, `for`, `return` vārdu (jauns jēdziens).
- Pārskatīt, ka kopu demonstrācija 4. nodarbībā bija papildu — šeit nav nepieciešama.

### 18:00–18:30 — `def` un izsaukšana (30 min)
- `01_basic_functions.py`: parādīt, ka `def` izveido funkciju, bet nepalaiž tās ķermeni.
- Salīdzināt divus izsaukumus `greet_person("Anna")`, `greet_person("Jānis")`; atkāpes, resnās zarnas, iekavas.
- Studenti pirms palaišanas paredz izvadi; tīmekļa jautājumi un kopēšanas poga.

### 18:30–19:05 — parametri, argumenti un `return` (35 min)
- `02_parameters_return.py`; salīdzināt `double_with_print` un `double_with_return`.
- Pierakstīt uz tāfeles `a is None` un `b == 10`; uzsvērt `return` pārtrauc funkcijas izpildi.
- Funkciju izsaukumu laboratorijā mainīt `a` un `b`; norādīt, ka pārlūkā tiek modelēts tikai konkrēts piemērs.
- Parādīt `add(2,3)`; pēc tam *īsi*, ja laiks, `add(2)` un `add(b=3,a=2)`.
- Pieminēt argumentu skaita neatbilstību un `TypeError`.

### 19:05–19:25 — 4. nodarbības algoritma pārveide (20 min)
- Uzrakstīt `count_words(text)` kopā ar studentiem, neatverot pilnu risinājumu.
- Funkcija saņem tekstu, atgriež `dict`; ārpusē veido `result`, izdrukā to.
- Izsaukt to divreiz ar atšķirīgiem argumentiem, arī `""`.
- Neievadīt `Counter`, comprehensions, `re` vai pieturzīmju normalizēšanu.

### 19:25–19:35 — pārtraukums (10 min)

### 19:35–19:55 — lokālie mainīgie un kompozīcija (20 min)
- `04_scope.py`: ārējais `city = "Rīga"`; funkcijas `city = "Liepāja"`; studenti paredz abus `print`.
- `count_unique_words(text)` izsauc `count_words(text)`; parādīt divu funkciju sadarbību.
- Neiedziļināties `global` un nosaukumu meklēšanas noteikumos.

### 19:55–20:15 — moduļi un imports (20 min)
- `import math`, `math.sqrt(81)`; no standarta bibliotēkas piemēra pāriet uz pašu `word_tools.py`.
- Parādīt divas blakus esošas datnes; palaist `05_modules/main.py`.
- `if __name__ == "__main__"` skaidrot tikai pēc nepieciešamības kā izvēles paplašinājumu.
- Neapspriest `pip`, virtuālās vides un sarežģītus importēšanas ceļus.

### 20:15–20:25 — `assert` (10 min)
- `06_testing.py`: trīs pareizi gadījumi un ceturtais salīdzināšanai.
- Ja tests veiksmīgs, ekrānā **nekas neparādās par pašu `assert`**; izdrukas paziņojums ir atsevišķs.
- Parādīt vienu neveiksmīgu `assert` kā demonstrāciju, pēc tam atgriezt atpakaļ.
- Uzsvērt `assert` nelietot lietotāja ievades validēšanai.

### 20:25–21:05 — patstāvīgā prakse (40 min)
- Visi mēģina uzdevumus 1.–3. (`format_name`, `count_words`, `basket_total`).
- Ātrākie turpina ar pielāgoto moduli un `unittest`.
- Sākuma fails `exercises/05_functions_modules/starter.py`; `pass` **nav** gatavs risinājums.
- Pārbaudes: `""`, `"  ANNA  "`, `"Rīga rīga"`, tukšs grozs, atkārtoti produkti, summa 3.90.
- Students vispirms izmēģina; sniegt vienu padomu pirms pilna risinājuma. Referenču risinājumi slēpti tīmekļa `details`.

### 21:05–21:25 — kļūdu un risinājumu apspriede (20 min)
- Pārskatīt trīs pamata uzdevumus, katram vismaz vienu alternatīvu/robežtestu.
- Biežākās kļūdas: `print` `return` vietā; `return` cikla **iekšpusē**, kas pārtrauc pēc pirmā vārda; funkcijas izsaukuma trūkums; sajaukti `basket`/`prices` argumenti.
- Atgādināt, ka `str.split()` pats pieturzīmes nenovāc.

### 21:25–21:35 — `unittest` izvēles demonstrācija (10 min)
- `python -m unittest discover -s lessons/05_functions_modules/05_modules -p "test_*.py" -v`.
- Izvērtēt vienu `assertEqual` sekmīgo un vienu tīši nepareizo sagaidāmo rezultātu; labojumu atjaunot.
- Ja laika trūkst, atstāt `unittest` kā izvēles materiālu, nezaudējot pamatprakses laiku.

### 21:35–21:40 — noslēgums (5 min)
- Trīs jautājumi: kas ir arguments, ko atgriež `print()`, kāpēc pārbaudīt tukšu ievadi?
- 6. nodarbības tilts: `read_text(path)` → `count_words(text)` → `save_results(...)`.

## Tipiskās kļūdas — demonstrējamais labojums

| Simptoms | Cēlonis un risinājums |
| --- | --- |
| `IndentationError` | Atkāpe pēc `def ...:`; sajaukta atkāpju struktūra |
| `TypeError` pie izsaukuma | Nepareizs pozicionālo argumentu skaits |
| Rezultāts ir `None` | Funkcija drukā, bet neizmanto `return`, vai neizpilda to visos zaros |
| Tikai pirmais vārds saskaitīts | `return counts` atrodas `for` iekšpusē |
| `NameError` ārpus funkcijas | Lokāls mainīgais nav automātiski pieejams ārpus tās |
| `ModuleNotFoundError` | Moduļu faili nav vienā mapē vai nosaukums ir kļūdains |
| Tests neko nedrukā | Sekmīgs `assert` ir kluss; atsevišķi ziņot par testu palaišanu |
| Cenai nepareizs rezultāts | Ignorēti atkārtoti produkti vai nepareizi argumenti |

## Sagatavošanas un pieņemšanas pārbaude

1. Ar Python 3 palaist sešus demonstrāciju skriptus un `unittest` testu atklāšanu; **visiem obligātajiem testiem jāiziet**.
2. Pārbaudīt `word_tools.py` importēšanu no `main.py` bez ārējām pakotnēm.
3. Tīmekļa lapā pārbaudīt **25** pašpārbaudes jautājumus, pareizās/nepareizās atbildes un skaidrojumus.
4. Funkciju laboratorijā pārbaudīt negatīvus skaitļus, 0, tukšu ievadi un nepareizu argumentu; neapgalvot, ka tiek izpildīts Python.
5. `print`/`return` laboratorijā atšķirt redzamo izvadi un atgriezto `None`.
6. Tvērumu un testēšanas laboratorijā pārbaudīt atkārtotas izsaukšanas, tukša teksta un kļūdainas sagaidāmās vērtības rezultātus.
7. Pārbaudīt `details` paslēptos risinājumus, koda kopēšanas pogas, sadaļu progresa saglabāšanu un iepriekšējās/nākamās nodarbības saites.
8. Pārbaudīt skatu telefonā, tastatūras navigāciju un ekrānlasītāja `role=status` paziņojumus.
9. MS Teams: ekrāna kopīgošana, koda fonta izmērs, ierakstīšana; studentiem vēlams atvērt vietni otrā logā.

## Robežas un nākamā nodarbība

Neziedot pamatfunkciju praksi par labu teorijai par rekursiju, dekoratoriem, funkcionālo programmēšanu vai `pytest`. Ja laika mazāk, izlaist `unittest`, nevis saīsināt 40 min praksi. Saglabāt darbojošos `count_words(text)` — 6. nodarbībā apstrādāsim tekstu no faila un pēc tam CSV.
