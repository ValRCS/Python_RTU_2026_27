# 2. nodarbība — Nosacījumi un Būla loģika

**Datums:** otrdiena, 2026. gada 17. novembris, 17:45–21:40.  
**Mācību vietne:** [interaktīvā 2. nodarbība](../../docs/lessons/02-types-conditions/index.html).  
**Patstāvīgā prakse:** [pieci uzdevumi ar pārbaudes piemēriem](../../exercises/02_types_conditions/README.md).  
**Iepriekš:** [1. nodarbība — Python ievads](../01_getting_started/README.md).  
**Nākamreiz:** [3. nodarbība — cikli un virknes](../03_loops_strings/README.md).

Šī nodarbība turpina 1. nodarbībā apgūto `print()`, `input()`, mainīgo un vienkāršo datu tipu izmantošanu. **Galvenais jaunais temats ir lēmumu pieņemšana programmā:** salīdzinājumi, Būla loģika un `if/elif/else`. Tipi un aritmētika tiek **atkārtoti**, nevis mācīti vēlreiz no sākuma.

## Sasniedzamie rezultāti

Pēc nodarbības students spēj:

1. Paskaidrot, kāpēc `input()` atgriež `str`, un pārveidot skaitlisku ievadi ar `int()` vai `float()`.
2. Lietot salīdzinājumus `==`, `!=`, `<`, `<=`, `>`, `>=` un izskaidrot to `bool` rezultātu.
3. Izmantot `True`, `False`, `and`, `or`, `not` un paredzēt vienkāršu loģisko izteiksmju rezultātu.
4. Uzrakstīt `if`, `elif`, `else` konstrukciju, ievērot atkāpes un zaru pārbaudes secību.
5. Kombinēt vairākus nosacījumus, lietot intervālu pārbaudi (piemēram, `18 <= vecums < 65`) un nepieciešamības gadījumā ligzdotu `if`.
6. Patstāvīgi palaist nelielu programmu, pārbaudīt robežvērtības un izskaidrot kļūdu cēloni.

## Īss atgādinājums

| Izteiksme | Nozīme | Rezultāta piemērs |
| --- | --- | --- |
| `int("18")` | Virkni pārvērš veselā skaitlī | `18` |
| `float("2.5")` | Virkni pārvērš decimālskaitlī | `2.5` |
| `12 == 12` | Vienāds ar | `True` |
| `12 != 12` | Nav vienāds ar | `False` |
| `18 <= vecums < 65` | Salīdzinājumu ķēde | `True` pie `vecums = 20` |
| `True and False` | Abi nosacījumi patiesi | `False` |
| `True or False` | Vismaz viens ir patiess | `True` |
| `not True` | Loģiskā noliegšana | `False` |

**Svarīgi:** `=` piešķir vērtību, bet `==` pārbauda vienādību. `bool("False")` ir `True`, jo netukša virkne ir patiesa loģiskā kontekstā; teksts `"False"` nav Būla vērtība `False`.

### Nosacījuma izpildes kārtība

~~~python
punkti = 75
if punkti >= 90:
    print("Izcili")
elif punkti >= 60:
    print("Ieskaitīts")
else:
    print("Vēl jāpatrenējas")
~~~

Vienā `if/elif/else` ķēdē tiek izpildīts **pirmais zars, kura nosacījums ir patiess**. Vēlākie zari netiek pārbaudīti. Atkāpes norāda, kuras komandas pieder attiecīgajam zaram; aiz `if`, `elif` un `else` lieto kolu. Ja sākumā pārbaudi `punkti >= 60`, vērtība `95` tur jau nonāks un `>= 90` zars vairs netiks sasniegts.

## Nodarbības laika plāns

| Laiks | Saturs |
| --- | --- |
| 17:45–18:00 | 1. nodarbības atkārtojums: `input`, tipi, konvertēšana |
| 18:00–18:25 | Tipu pārveides kļūdas un operatori |
| 18:25–18:55 | Salīdzinājumi, `bool` un robežvērtības |
| 18:55–19:20 | `and`, `or`, `not`; patiesumtabulas |
| 19:20–19:30 | Pārtraukums |
| 19:30–20:00 | `if/elif/else`, atkāpes un zaru secība |
| 20:00–20:25 | Salikti nosacījumi un temperatūras ieteikumu programma |
| 20:25–21:05 | Patstāvīgie uzdevumi: 1.–3. pamata, 4.–5. izaicinājumi |
| 21:05–21:30 | Risinājumu apspriešana, atkļūdošana un robežu pārbaude |
| 21:30–21:40 | Kopsavilkums; pāreja uz `for` un `while` |

## Palaid Python piemērus

Vajadzīgs lokāli uzstādīts **Python 3**; ārējas pakotnes nav vajadzīgas. Atver termināli repozitorija saknes mapē:

~~~powershell
python lessons/02_types_conditions/01_types_conversion.py
python lessons/02_types_conditions/02_comparisons.py
python lessons/02_types_conditions/03_boolean_logic.py
python lessons/02_types_conditions/04_if_elif_else.py
python lessons/02_types_conditions/05_compound_conditions.py
python lessons/02_types_conditions/06_temperature_advisor.py
~~~

macOS/Linux sistēmās izmanto `python3`, ja `python` nav pieejams; dažās Windows instalācijās vari izmantot `py`. **1.–5. faili nav interaktīvi:** maini sākotnējās mainīgo vērtības, saglabā un palaid vēlreiz. **6. fails** prasa temperatūru un atbildi `j/n`; decimālskaitli ievadi ar punktu, piemēram, `12.5`. Ja ievadīsi `abc` skaitļa vietā, `float()` izraisīs `ValueError`; detalizētu izņēmumu apstrādi apgūsim vēlāk.

| Fails | Ko tajā pētīt |
| --- | --- |
| [01_types_conversion.py](01_types_conversion.py) | `str` un skaitļu atšķirība, `int()`, `float()`, `bool()` |
| [02_comparisons.py](02_comparisons.py) | Salīdzinājumi, intervāli, robežas |
| [03_boolean_logic.py](03_boolean_logic.py) | `and`, `or`, `not`, patiesumtabulas |
| [04_if_elif_else.py](04_if_elif_else.py) | Zari, atkāpes, pārbaudes secība |
| [05_compound_conditions.py](05_compound_conditions.py) | Salikti un ligzdoti nosacījumi |
| [06_temperature_advisor.py](06_temperature_advisor.py) | Pilna programma ar lietotāja ievadi |
| [07_bonus_logic.py](07_bonus_logic.py) | Neobligāti: De Morgana likumi, īssavienojuma izpilde, `match/case` (Python 3.10+) |

## Patstāvīgā prakse un pašpārbaude

[Pieci uzdevumi ar konkrētiem pārbaudes piemēriem](../../exercises/02_types_conditions/README.md): skaitļa zīme, pilngadība, punktu vērtējums, biļetes cena un kalkulators. **Sāc ar 1.–3. uzdevumu**, tad, ja laiks ļauj, turpini ar 4.–5. Raksti katru uzdevumu atsevišķā `.py` failā. Padomi un atveramie paraugrisinājumi atrodami [interaktīvās nodarbības 6. sadaļā](../../docs/lessons/02-types-conditions/index.html#prakse) — atver tos **pēc paša mēģinājuma**.

Pirms pabeidz programmu, pārbaudi skaitļus tieši uz robežām (piemēram, `17`/`18`, `59`/`60` un `89`/`90`). Pārbaudi arī nederīgas vērtības un to, vai zaru secība ir korekta.

## Tipiskas kļūdas

| Piemērs | Kas nav kārtībā / ko darīt |
| --- | --- |
| `if x = 5:` | `=` piešķir vērtību; salīdzināšanai lieto `x == 5`. |
| `if x == 5 or 10:` | Izteiksme ir patiesa gandrīz jebkurai `x` vērtībai, jo `10` ir loģiski patiess; raksti `x == 5 or x == 10`. |
| `vecums = input(...)` un `vecums >= 18` | `input()` atgriež `str`; vajadzīga pārveidošana ar `int()`. |
| Nepareizas atkāpes | Komanda var nonākt nepareizā zarā vai rasties `IndentationError`. |
| `if x >= 60` pirms `elif x >= 90` | Vēlākā pārbaude nekad nepieņems `x >= 90`; plašāko nosacījumu liec pēc konkrētākā. |
| `int("divi")` | Izraisa `ValueError`; šajā nodarbībā vēl neveidojam pilnu izņēmumu apstrādi. |
| `a / 0` | Izraisa `ZeroDivisionError`; pārbaudi dalītāju pirms dalīšanas. |

## Būtiskais un papildu saturs

**Obligāti:** salīdzinājumi, `bool`, `and/or/not`, `if/elif/else`, atkāpes, zaru secība, skaitļu robežas, vienkārša ievades konvertēšana.  
**Pēc iespējas:** ligzdots `if`, salīdzinājumu ķēdes un lasāmas izteiksmes ar iekavām.  
**Papildu izaicinājumi:** De Morgana likumi, īssavienojuma izpilde (`short-circuit`), `match/case` (Python 3.10+) — skatīt [papildu failu](07_bonus_logic.py) un [HTML 7. sadaļu](../../docs/lessons/02-types-conditions/index.html#papildus).  
**Nākamreiz:** `for`, `while`, virknes un to metodes; atkārtotu lēmumu izpilde ciklā.

## Atsauces un iepriekšējā kursa piemēri

- [Python pamācība: `if` statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements).
- [Python dokumentācija: Būla operatori](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not).
- [Python dokumentācija: salīdzināšana](https://docs.python.org/3/library/stdtypes.html#comparisons).
- [Python 2024/25 arhīvs: datu tipi un ievade](https://github.com/ValRCS/Python_RTU_2024_25/tree/main/topic_2_data_types_input).
- [Python 2024/25 arhīvs: Būla loģika un zarojumi](https://github.com/ValRCS/Python_RTU_2024_25/tree/main/topic_3_booleans_logic_branching).

Arhīvs ir **papildavots**, nevis obligāti izpildāmo uzdevumu saraksts. Šīs nodarbības aktuālais kods ir šajā mapē.
