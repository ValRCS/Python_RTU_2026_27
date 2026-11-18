# 3. nodarbība — Cikli un virknes

**Datums:** ceturtdiena, 2026. gada 19. novembris, 17:45–21:40.  
**Mācību vietne:** [Interaktīvā 3. nodarbība](../../docs/lessons/03-loops-strings/index.html)  
**Patstāvīgie uzdevumi:** [5 uzdevumi ar pārbaudēm](../../exercises/03_loops_strings/README.md)  
**Pasniedzēja papildu piemēri:** [ievades kļūdu apstrāde](../../instructor/2026-11-19_lesson03_error_handling_bonus.md)

## Sasniedzamie rezultāti

Pēc nodarbības students spēj:
1. Lietot `for` un `range(start, stop, step)` un paskaidrot, kāpēc `stop` nav iekļauts.
2. Izmantot `while` ar skaitītāju vai pārtraukšanas komandu, nepazaudējot cikla beigu nosacījumu.
3. Atšķirt `break` no `continue`, kombinēt ciklus ar iepriekš apgūtajiem `if` nosacījumiem.
4. Iterēt cauri `str`, lietot `len()`, indeksus un šķēlumus; saprast, kāpēc virknes ir nemaināmas.
5. Ar `try/except ValueError` ciklā atkārtoti pieprasīt ievadi, līdz to var pārveidot par skaitli; atšķirt konvertēšanas kļūdu no nederīgas vērtības.
6. Lietot `strip()`, `lower()`, `upper()`, `replace()`, `count()` un pārbaudīt apakšvirkni ar `in`.

## Laika plāns

| Laiks | Saturs |
| --- | --- |
| 17:45–18:05 | Atkārtojums: dati, `if`, Būla loģika |
| 18:05–18:40 | `for`, `range`, akumulators, iterāciju vizualizācija |
| 18:40–19:10 | `while`, ievades komandas, `break` un `continue` |
| 19:10–19:25 | `try/except ValueError` kopā ar `while`: ievades atkārtošana |
| 19:25–19:35 | Pārtraukums |
| 19:35–20:05 | Virknes, `for char`, `len()`, indeksi un šķēlumi |
| 20:05–20:25 | Virkņu metodes un kopīgi piemēri |
| 20:25–21:05 | Patstāvīgā prakse (3 pamata + 2 izaicinājumi) |
| 21:05–21:30 | Risinājumu apspriede un atkļūdošana |
| 21:30–21:40 | Noslēgums; pāreja uz sarakstiem un vārdnīcām |

## Palaid piemērus lokāli

Nepieciešams Python 3; ārējas pakotnes nav vajadzīgas. Atver termināli repozitorija saknē:

```powershell
python lessons/03_loops_strings/01_for_range.py
python lessons/03_loops_strings/02_while.py
python lessons/03_loops_strings/03_strings.py
python lessons/03_loops_strings/04_combined.py
python lessons/03_loops_strings/05_error_handling.py
```

Mac/Linux dažkārt jālieto `python3` komanda. Otrā, ceturtā un piektā programma prasa ievadi. Apturi ilgstošu ciklu terminālī ar Ctrl+C.

## Būtiskais un papildu saturs

**Obligāti:** `for`, `range`, `while`, cikla mainīgais, `break`, `try/except ValueError` ievades atkārtošanai, `str` iterācija, indeksi, `[start:stop]`, `strip` un `lower`.  
**Pēc iespējas:** `continue` (arī kļūdu apstrādē), negatīvs `range` solis, `[::-1]`, `replace`, `count`, `startswith`, `endswith`, skaitļu ievade ar iziešanas komandu.  
**Nākamreiz:** `list`, `tuple`, `dict`, `set`, `split` un `join` (jo `split()` atgriež sarakstu).  
**Vēlāk:** regulārās izteiksmes, detalizēta Unicode normalizēšana, funkciju definēšana un paplašināta izņēmumu apstrāde (`else`, `finally`, izņēmumu hierarhija).

## Piezīmes

- `range(1, 6)` satur 1, 2, 3, 4, 5, nevis 6.
- `int("abc")` izraisa `ValueError`; apstrādā to ar `except ValueError` un turpini `while` ciklu. `int("-2")` izpildās veiksmīgi, tāpēc nenegatīva skaitļa prasību pārbauda ar `if`.
- `for char in text` ir saprotamāks par `for i in range(len(text))`, ja indekss nav vajadzīgs.
- Atšķir vienu rakstzīmi (`str`) no atsevišķa `char` tipa, kura Python nav.
- `text.replace(...)` atgriež jaunu virkni, nemaina oriģinālo.
- `text[-1]` tukšai virknei izraisa `IndexError`; `text[1:3]` pāri robežai parasti neizraisa kļūdu.
- Latvian `ā, ē, ī, ū` jāņem vērā piemēros. `len()` skaita Unicode koda punktus, ne obligāti vizuālos grafēmu klasterus.

## Atsauces un vēsturiskie piemēri

- [Python dokumentācija: for](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Python dokumentācija: str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
- [Python dokumentācija: try/except](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)
- [2024/25 arhīva ciklu piemēri](https://github.com/ValRCS/Python_RTU_2024_25/tree/main/topic_4_loops_and_errors)
- [2024/25 arhīva virkņu piemēri](https://github.com/ValRCS/Python_RTU_2024_25/tree/main/topic_5_strings)

Arhīva piemēri kalpo par atsauci; aktuālie nodarbības materiāli atrodas šajā repozitorijā.
