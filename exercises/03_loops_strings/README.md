# 3. nodarbības patstāvīgie uzdevumi — 2026-11-19

**Darba laiks klasē:** 20:25–21:05. **Pirmie trīs uzdevumi ir pamata līmenis**, nākamie divi — izaicinājumi.  
**Tēmas:** `for`, `while`, `range()`, `if`, virknes, indeksi, metodes.  
**Piemēri:** [Python skripti](../../lessons/03_loops_strings/README.md), [interaktīvā mācību lapa](../../docs/lessons/03-loops-strings/index.html).

Saglabā katru risinājumu atsevišķā `.py` failā. Palaid savā datorā un pārbaudi vismaz trīs dažādas ievades. Pēc mēģinājuma interaktīvajā lapā drīksti atvērt padomu un parauga risinājumu. Šajā nodarbībā arī apgūstam `try/except ValueError` atkārtotai skaitļa ievadei. **Pamata risinājumiem tas nav obligāts**, bet 1. un 4. uzdevumam ir papildu variants ar drošu ievadi.

## 40 minūšu darba secība

| Posms | Orientējošais laiks | Galvenās prasmes |
| --- | ---: | --- |
| 1. Skaitļu summa | 8–12 min | `for`, `range`, akumulators |
| 2. Atkārtota ievade | 8–12 min | `while` un `break` |
| 3. Patskaņu skaitītājs | 10–15 min | `for` + `if` + `str` |
| Testēšana un kļūdu labošana | atlikušais laiks | Vismaz trīs ievades katram uzdevumam |
| 4.–5. uzdevums | ātrākajiem | Papildu izaicinājumi |

Sāc ar 1.–3. uzdevumu. Ja grūtības sagādā atkāpes vai cikla uzbūve, zemāk pieejamas **Sākuma sagataves**. Neveido visiem uzdevumiem izvērstu kļūdu apstrādi uz obligātā darba laika rēķina.

## 1. Skaitļu summa (pamata)

Ievadi veselu nenegatīvu `n` un ar `for` un `range()` saskaiti visus skaitļus no 1 līdz `n`. Ja `n < 0`, parādi paziņojumu, nevis rēķini summu.

| Ievade | Sagaidāmais |
| --- | --- |
| 0 | 0 |
| 1 | 1 |
| 10 | 55 |

**Padoms:** `total = 0`, tad ciklā `total += number`.  
**Papildus:** aprēķini tikai pāra skaitļu summu no 1 līdz `n`; pie `n = 10` rezultāts ir 30. **Ievades drošība:** ar `while True` un `try/except ValueError` pēc `abc` jautā skaitli vēlreiz; negatīvu skaitli noraidi ar `if`.

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
**Papildus:** lieto `random.randint(1, 10)`; tas ir standartbibliotēkas modulis, tāpēc šī daļa ir neobligāta. **Ievades drošība:** `abc` un skaitļi ārpus 1–10 nedrīkst patērēt vienu no pieciem *derīgajiem* minējumiem; izmanto `while attempts < 5` un palielini skaitītāju tikai pēc veiksmīgas pārbaudes.

## 5. Palindroms (izaicinājums)

Ievadi vārdu. Nosaki, vai tas ir identisks, lasot no kreisās un labās puses. Pēc tam ignorē lielos/mazos burtus un atstarpes.

| Ievade | Sagaidāmais |
| --- | --- |
| aka | palindroms |
| Python | nav palindroms |
| A ka | palindroms pēc atstarpju noņemšanas |

**Padoms:** `normalized = text.lower().replace(" ", "")`, pēc tam `normalized[::-1]`.  
**Papildus:** salīdzini savu šķēluma risinājumu ar ciklu, kas secīgi pārbauda simbolus no abām pusēm.

<details>
<summary><strong>Sākuma sagataves iesācējiem (atver pēc vajadzības)</strong></summary>

**1. uzdevums:** pievieno ciklu, kas maina `total`.

```python
n = int(input("n: "))
if n < 0:
    print("Nederīgs n")
else:
    total = 0
    # TODO: for number in range(...):
    #     total += ...
    print(total)
```

**2. uzdevums:** papildini iziešanas nosacījumu.

```python
count = 0
while True:
    text = input("Teksts: ")
    # TODO: ja text.strip().lower() ir "beigt", izpildi break
    count += 1
print(count)
```

**3. uzdevums:** nomaini `pass` ar pārbaudi un skaitītāja palielināšanu.

```python
text = input("Teksts: ")
vowels = "aāeēiīouū"
count = 0
for char in text.lower():
    # TODO: ja char ir vowels, palielini count
    pass
print(count)
```

Saglabā sagatavi kā `.py` failu un aizpildi TODO komentārus. Atkāpes aiz `for` un `if` ir obligātas.
</details>

## Noslēguma pašpārbaude

- Vai zinu, kad izvēlēties `for`, bet kad `while`?
- Vai spēju izskaidrot, kāpēc `range(1, 5)` nedod 5?
- Vai zinu, kā apstādināt potenciāli bezgalīgu ciklu?
- Vai protu ar `try/except ValueError` kļūdainas skaitļa ievades gadījumā jautāt vēlreiz?
- Vai protu iegūt virknes pēdējo simbolu un izveidot apgrieztu virkni?
- Vai saprotu, ka `.replace()` atgriež jaunu virkni?

**Nākamreiz (24. novembrī):** saraksti (`list`), korteži (`tuple`), vārdnīcas (`dict`), kopas (`set`); `split()` un `join()` sasaistīs tekstu ar sarakstiem.
