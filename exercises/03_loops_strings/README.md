# 3. nodarbības patstāvīgie uzdevumi — 2026-11-19

**Darba laiks klasē:** 20:25–21:05. **Pirmie trīs uzdevumi ir pamata līmenis**, nākamie divi — izaicinājumi.  
**Tēmas:** `for`, `while`, `range()`, `if`, virknes, indeksi, metodes.  
**Piemēri:** [Python skripti](../../lessons/03_loops_strings/README.md), [interaktīvā mācību lapa](../../docs/lessons/03-loops-strings/index.html).

Saglabā katru risinājumu atsevišķā `.py` failā. Palaid savā datorā un pārbaudi vismaz trīs dažādas ievades. Pēc mēģinājuma interaktīvajā lapā drīksti atvērt padomu un parauga risinājumu. Šajā nodarbībā `int(input(...))` var izraisīt `ValueError`, ja ievada ne-skaitli; pilna kļūdu apstrāde būs vēlāk.

## 1. Skaitļu summa (pamata)

Ievadi veselu nenegatīvu `n` un ar `for` un `range()` saskaiti visus skaitļus no 1 līdz `n`. Ja `n < 0`, parādi paziņojumu, nevis rēķini summu.

| Ievade | Sagaidāmais |
| --- | --- |
| 0 | 0 |
| 1 | 1 |
| 10 | 55 |

**Padoms:** `total = 0`, tad ciklā `total += number`.  
**Papildus:** aprēķini tikai pāra skaitļu summu no 1 līdz `n`; pie `n = 10` rezultāts ir 30.

## 2. Atkārtota ievade (pamata)

Ar `while` vaicā tekstu līdz komandai `beigt`. Izdrukā ievadīto ierakstu skaitu, neieskaitot noslēguma komandu.

**Testi:** uzreiz `beigt` → 0; pēc `ābols`, `bumbieris`, `BEIGT` → 2; komanda ar ārējām atstarpēm arī beidz ciklu.

**Padoms:** `while True`, `if text.strip().lower() == "beigt": break`.

## 3. Patskaņu skaitītājs (pamata)

Ievadi tekstu un saskaiti latviešu valodas patskaņu burtus `a, ā, e, ē, i, ī, o, u, ū`; lielos burtus skaiti tāpat kā mazos.

| Ievade | Sagaidāmais |
| --- | --- |
| Rīga | 2 |
| Ābols | 2 |
| brrr | 0 |

**Padoms:** iterē cauri `text.lower()`; pārbaudi `if character in vowels`.  
**Papildus:** izdrukā katra atrastā patskaņa pozīciju, izmantojot `range(len(text))`.

## 4. Skaitļa minēšanas spēle (izaicinājums)

Slepenais skaitlis ir 7. Lietotājam ir ne vairāk par pieciem minējumiem. Pēc katra kļūdainā minējuma pasaki `Par mazu` vai `Par lielu`. Pie pareizā skaitļa uzreiz pārtrauc ciklu; pēc pieciem nepareiziem minējumiem pasaki pareizo atbildi.

**Testi:** 7 uzreiz; 1, 5, 7; pieci nepareizi minējumi.  
**Padoms:** `for attempt in range(1, 6)` un `break`.  
**Papildus:** lieto `random.randint(1, 10)`; tas ir standartbibliotēkas modulis, tāpēc šī daļa ir neobligāta.

## 5. Palindroms (izaicinājums)

Ievadi vārdu. Nosaki, vai tas ir identisks, lasot no kreisās un labās puses. Pēc tam ignorē lielos/mazos burtus un atstarpes.

| Ievade | Sagaidāmais |
| --- | --- |
| aka | palindroms |
| Python | nav palindroms |
| A ka | palindroms pēc atstarpju noņemšanas |

**Padoms:** `normalized = text.lower().replace(" ", "")`, pēc tam `normalized[::-1]`.  
**Papildus:** salīdzini savu šķēluma risinājumu ar ciklu, kas secīgi pārbauda simbolus no abām pusēm.

## Noslēguma pašpārbaude

- Vai zinu, kad izvēlēties `for`, bet kad `while`?
- Vai spēju izskaidrot, kāpēc `range(1, 5)` nedod 5?
- Vai zinu, kā apstādināt potenciāli bezgalīgu ciklu?
- Vai protu iegūt virknes pēdējo simbolu un izveidot apgrieztu virkni?
- Vai saprotu, ka `.replace()` atgriež jaunu virkni?

**Nākamreiz (24. novembrī):** saraksti (`list`), korteži (`tuple`), vārdnīcas (`dict`), kopas (`set`); `split()` un `join()` sasaistīs tekstu ar sarakstiem.
