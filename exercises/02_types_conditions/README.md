# 2. nodarbības patstāvīgie uzdevumi — 2026-11-17

**Laiks nodarbībā:** 20:25–21:05 (40 min). **Obligāti mēģini 1.–3. uzdevumu**; 4.–5. ir papildu izaicinājumi.  
**Temati:** datu tipu pārveidošana, salīdzinājumi, `bool`, `and/or/not`, `if/elif/else`.  
**Materiāli:** [Python demonstrācijas](../../lessons/02_types_conditions/README.md) · [interaktīvā nodarbība](../../docs/lessons/02-types-conditions/index.html#prakse).

Saglabā **katra uzdevuma kodu atsevišķā `.py` failā** un izmēģini norādītās pārbaudes ievades. Atver padomu un paraugrisinājumu interaktīvajā lapā tikai pēc sava mēģinājuma. `int(input(...))` un `float(input(...))` kļūdainai teksta ievadei var izraisīt `ValueError`; pagaidām pietiek saprast kļūdas cēloni, nevis ieviest `try/except`.

## 1. Pozitīvs, negatīvs vai nulle (pamata)

Ievadi **veselu skaitli** un ar `if/elif/else` izdrukā `Pozitīvs`, `Negatīvs` vai `Nulle`.

| Ievade | Sagaidāmais |
| --- | --- |
| `-4` | `Negatīvs` |
| `0` | `Nulle` |
| `7` | `Pozitīvs` |

**Padoms:** salīdzini skaitli ar nulli, izmantojot `>` un `<`.  
**Papildus:** pārbaudi arī lielu negatīvu un lielu pozitīvu skaitli.

## 2. Pilngadības pārbaude (pamata)

Ievadi cilvēka vecumu veselā skaitlī. **Negatīvu vecumu noraidi** kā nederīgu ievadi. Pretējā gadījumā izdrukā `Pilngadīgs`, ja vecums ir vismaz 18, vai `Nepilngadīgs`, ja mazāks.

| Ievade | Sagaidāmais |
| --- | --- |
| `-1` | `Nederīgs vecums` |
| `17` | `Nepilngadīgs` |
| `18` | `Pilngadīgs` |

**Padoms:** vispirms pārbaudi nederīgu vecumu.  
**Papildus:** pievieno paskaidrojošu izdruku, ja vecums ir tieši 18.

## 3. Punktu vērtējums (pamata)

Ievadi punktus kā veselu skaitli no **0 līdz 100**. Nosaki vērtējumu: 90–100 → `A`, 75–89 → `B`, 60–74 → `C`, 0–59 → `D`. Vērtības ārpus 0–100 jāatgrūž ar `Nederīgs punktu skaits`.

| Ievade | Sagaidāmais |
| --- | --- |
| `-1`, `101` | `Nederīgs punktu skaits` |
| `59`, `60` | Attiecīgi `D`, `C` |
| `74`, `75` | Attiecīgi `C`, `B` |
| `89`, `90` | Attiecīgi `B`, `A` |

**Padoms:** pārbaudi nederīgās vērtības, pēc tam vērtējumu robežas **dilstošā secībā**.  
**Papildus:** paskaidro, kādēļ `punkti >= 60` nedrīkst būt pirms `punkti >= 90`.

## 4. Biļetes cena (izaicinājums)

Pamata biļetes cena ir **10 EUR**. Bērniem līdz 6 gadiem (vecums 0–5) tā ir 0 EUR; 6–17 gadiem — 5 EUR; no 65 gadiem — 7 EUR. Pārējiem — 10 EUR. Negatīvu vecumu noraidi.

**Papildus pēc pamata versijas:** studentiem no 18 līdz 64 gadiem cena ir **8 EUR**. Vaicā, vai persona ir students (`j/n`). Vecuma kategorijas ir prioritāras: bērnam vai senioram studenta atlaidi nepiemēro.

| Vecums / students | Sagaidāmā cena |
| --- | --- |
| `-1` / `n` | Nederīgs vecums |
| `5` / `n` | 0 EUR |
| `6` / `n` | 5 EUR |
| `17` / `j` | 5 EUR |
| `18` / `j` | 8 EUR |
| `64` / `n` | 10 EUR |
| `65` / `j` | 7 EUR |

**Padoms:** pēc nederīga vecuma pārbaudi bērnu un senioru kategorijas; studentu nosacījumu vērtē tikai tad, kad šie zari nav izpildījušies.

## 5. Vienkāršs kalkulators (izaicinājums)

Ievadi **divus skaitļus** un operācijas simbolu (`+`, `-`, `*`, `/`). Izdrukā aprēķina rezultātu. Nepazīstamai operācijai parādi `Nezināma operācija`, bet dalīšanai ar nulli — `Nedrīkst dalīt ar nulli`. Skaitļus lasi ar `float()`.

| Ievade | Sagaidāmais |
| --- | --- |
| `8`, `2`, `+` | `10.0` |
| `8`, `2`, `/` | `4.0` |
| `8`, `0`, `/` | `Nedrīkst dalīt ar nulli` |
| `8`, `2`, `%` | `Nezināma operācija` |

**Padoms:** `if/elif/else` izvēlas operāciju; dalīšanas zara **iekšienē** pievieno vēl vienu `if`, kas pārbauda dalītāju.  
**Papildus:** salīdzini izdruku ar `print(f"{rezultats:.2f}")`, ja lieto formatēšanu.

## Pašpārbaude

- Vai protu atšķirt piešķiršanu `=` no salīdzināšanas `==`?
- Vai varu izskaidrot, kāpēc `and` un `or` var dot atšķirīgu rezultātu?
- Vai zinu, kāpēc `if/elif/else` ķēdē izpilda tikai vienu zaru?
- Vai pārbaudu robežas **tieši pirms un pēc** sliekšņa?
- Vai protu palaist un labot kodu pats savā Python vidē?

**Nākamreiz (19. novembrī):** `for` un `while` atkārtos līdzīgas darbības; `if` noteiks, kurās iterācijās kaut ko darīt.

[Atpakaļ uz 2. nodarbības konspektu](../../lessons/02_types_conditions/README.md)
