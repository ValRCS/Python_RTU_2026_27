# 4. nodarbības patstāvīgie uzdevumi — 2026-11-24

**Laiks nodarbībā:** 20:25–21:05 (40 min). **Obligāti mēģini 1.–3. uzdevumu.** 4.–5. ir papildu izaicinājumi.  
**Temati:** saraksti, vārdnīcas, cikli, `split()`/`join()`, korteži un kopas.

Raksti katru programmu savā `.py` failā. Pārbaudi vismaz trīs gadījumus, ieskaitot tukšu ievadi, ja iespējams. Padomi un pilni risinājumi pieejami [nodarbības lapā](../../docs/lessons/04-collections/index.html) tikai pēc paša mēģinājuma.

## 1. Iepirkumu saraksts (pamata, aptuveni 8–10 min)

Ar `while True` vaicā produkta nosaukumu līdz komandai `beigt`. Pievieno katru iepriekš ievadīto produktu sarakstam ar `append()`. Izdrukā sarakstu un elementu skaitu. Noslēguma komandu neiekļauj. Saglabā produkta oriģinālo nosaukumu, bet komandu pārbaudi pēc `strip().lower()`.

| Ievades | Sagaidāmais |
| --- | --- |
| `beigt` | `[]`, skaits 0 |
| `ābols, piens, beigt` | `["ābols", "piens"]`, skaits 2 |
| `ābols, ābols, BEIGT` | `["ābols", "ābols"]`, skaits 2 |

**Padoms:** `items = []`; pievieno ar `items.append(text)`.  
**Papildus:** izdrukā katru produktu atsevišķā rindā.

## 2. Vārdu biežuma skaitītājs (pamata, aptuveni 10–12 min)

Ievadi vienu teikumu. Pārvērt to mazajos burtos, sadali ar `split()` un izveido vārdnīcu, kas katram vārdam glabā reižu skaitu. Šajā uzdevumā pieturzīmes vēl nenormalizējam.

| Ievade | Sagaidāmais |
| --- | --- |
| `Rīga Python Rīga` | `{"rīga": 2, "python": 1}` |
| `ābols ābols ābols` | `{"ābols": 3}` |
| tukša rinda | `{}` |

**Padoms:** `counts[word] = counts.get(word, 0) + 1` vai `if word in counts`.  
**Papildus:** izdrukā katru atslēgu un vērtību atsevišķi, izmantojot `items()`.

## 3. Pirkumu kopējā cena (pamata, aptuveni 12–15 min)

Programma saņem jau sagatavotu cenu vārdnīcu un iepirkumu sarakstu:

~~~python
prices = {"maize": 1.50, "piens": 1.20, "ābols": 0.60}
basket = ["maize", "ābols", "ābols", "piens"]
~~~

Ar ciklu aprēķini visu produktu kopējo cenu, ieskaitot atkārtotus produktus. Izmanto vārdnīcu, lai iegūtu katra produkta cenu. **Šī groza rezultāts ir 3.90 EUR.**

| Grozs | Sagaidāmā cena |
| --- | --- |
| `[]` | 0.00 EUR |
| `["ābols", "ābols"]` | 1.20 EUR |
| `["maize", "ābols", "ābols", "piens"]` | 3.90 EUR |

**Padoms:** `total = 0`; `for product in basket: total += prices[product]`.  
**Papildus:** pievieno nezināmu produktu (piemēram, `siers`); izmanto `if product in prices`, lai izvairītos no `KeyError`, un izdrukā trūkstošās cenas.

## 4. Koordinātas (izaicinājums — korteži)

Izveido `coordinates = (56.95, 24.10)`, izdrukā abas koordinātas, iegūsti `len(coordinates)`. Pēc tam paskaidro, kāpēc `coordinates[0] = 57.0` nestrādā; šo rindu vari palaist atsevišķi, lai redzētu kļūdu.

**Padoms:** `tuple` atbalsta indeksēšanu, bet nav maināms.  
**Papildus:** izveido vienas vērtības kortežu un pārbaudi tā tipu.

## 5. Unikālie vārdi (izaicinājums — kopas)

Dots saraksts `["Anna", "Jānis", "Anna", "Ilze"]`. Iegūsti kopu ar unikālajiem vārdiem un izdrukā tās elementu skaitu. Skaidri pasaki, vai saraksta sākotnējā kārtība saglabāsies kopā.

**Sagaidāmais:** trīs unikāli vārdi. Izvadam vari lietot `sorted(...)`, lai iegūtu stabilu secību.  
**Papildus:** atrodi vārdus, kas kopīgi divām kopām, izmantojot `&`.

## Pašpārbaude

- Vai protu izlemt, kad jālieto `list`, bet kad `dict`?
- Vai saprotu, kā saraksts atšķiras no virknes un korteža?
- Vai protu ar `split()` izveidot sarakstu un ar `join()` izveidot virkni?
- Vai `in` vārdnīcā pārbauda atslēgas vai vērtības?
- Vai zinu, kāpēc `set` izņem dublikātus un kā izveidot tukšu kopu?

[Atpakaļ uz nodarbības konspektu](../../lessons/04_collections/README.md)
