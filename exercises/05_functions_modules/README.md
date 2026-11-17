# 5. nodarbības uzdevumi — funkcijas, moduļi un testi

**Datums:** 2026-11-26. **Patstāvīgais darbs:** 20:25–21:05 (40 min).  
**Obligāti mēģināt 1.–3. uzdevumu;** 4.–5. paredzēts ātrākajiem.  
**Sākuma kods:** [starter.py](starter.py). **Mācību vietne ar padomiem un paslēptiem risinājumiem:** [5. nodarbība](../../docs/lessons/05-functions-modules/index.html).

Izveido katram uzdevumam funkciju. Vispirms palaid piemēra gadījumu, pēc tam divus citus, tostarp tukšu ievadi, kur piemērojams. **Pamata uzdevumos funkcijām jāatgriež vērtība ar `return`**, nevis tikai jādrukā rezultāts. `print` izmanto, ja gribi parādīt vērtību pēc funkcijas izsaukuma.

## 1. Vārda noformēšana — `format_name(name)` (7–8 min)

Funkcija saņem virkni, noņem liekās atstarpes sākumā un beigās un noformē ar `title()`. **Atgriež** jauno virkni.

| Arguments | Sagaidāmā atgrieztā vērtība |
| --- | --- |
| `"  ANNA  "` | `"Anna"` |
| `"jĀnis bĒrziņš"` | `"Jānis Bērziņš"` |
| `""` | `""` |

**Padoms:** `name.strip().title()`.  
**Papildus:** pārbaudi, kā `title()` uzvedas ar saliktiem personvārdiem; tā ir vienkārša apstrāde, ne universāla personvārdu normalizēšana.

## 2. Vārdu biežums — `count_words(text)` (12–15 min)

Pārveido 4. nodarbības ciklu par funkciju. Saņem tekstu un **atgriež** `dict` ar vārdu skaitu. Lieto `lower().split()`; pieturzīmes vēl netīrām.

| Arguments | Sagaidāmais `dict` |
| --- | --- |
| `"Rīga Python Rīga"` | `{"rīga": 2, "python": 1}` |
| `"ābols ābols ābols"` | `{"ābols": 3}` |
| `""` | `{}` |

**Padoms:** sākumā `counts = {}`, pēc tam `for word in text.lower().split():`, beigās `return counts`. Pārbaudi rezultātu ar vismaz trim `assert`.

## 3. Iepirkumu grozs — `basket_total(basket, prices)` (15–18 min)

Izmanto *tieši* 4. nodarbības datus, bet šoreiz funkcija saņem **divus argumentus** un atgriež kopējo cenu.

```python
prices = {"maize": 1.50, "piens": 1.20, "ābols": 0.60}
basket = ["maize", "ābols", "ābols", "piens"]
```

| Grozs | Sagaidāmais |
| --- | --- |
| `[]` | `0.00` |
| `["ābols", "ābols"]` | `1.20` |
| `["maize", "ābols", "ābols", "piens"]` | `3.90` |

**Pieņēmums:** katram groza produktam ir cena vārdnīcā. Nezināms produkts šajā pamata uzdevumā var izraisīt `KeyError`; tā apstrāde ir **papildu** darbs.  
**Padoms:** `total = 0.0`, `for product in basket:`, `total += prices[product]`, `return total`.  
**Tests ar `float`:** `assert abs(basket_total(basket, prices) - 3.90) < 1e-9` (vai `round(..., 2) == 3.90`).

## 4. Paša modulis — `word_tools.py` (izaicinājums, 10 min)

Jaunā mapē izveido `word_tools.py` ar `count_words(text)`, bet blakus `main.py`:

```python
import word_tools

print(word_tools.count_words("Rīga rīga"))
```

Pārbaudi, vai `main.py` var izmantot funkciju. **Papildus:** izveido otru funkciju `unique_word_count(text)`, kas izmanto pirmo un atgriež atšķirīgo vārdu skaitu.

## 5. Unit testi — `unittest` (izaicinājums, 10–15 min)

Ieraksti trīs pārbaudes ar `unittest.TestCase` un `self.assertEqual`: tukšam tekstam, atkārtotiem vārdiem un atšķirīgiem reģistriem. Ieskatam: [izpildāms testu piemērs](../../lessons/05_functions_modules/05_modules/test_word_tools.py).

Palaid no repozitorija saknes:

```powershell
python -m unittest discover -s lessons/05_functions_modules/05_modules -p "test_*.py" -v
```

**Papildus:** tīši ievadi nepareizu sagaidāmo vērtību un izskaidro kļūdas ziņojumu.

## Pašpārbaude

- Vai protu pateikt, kurš ir parametrs un kurš — arguments?
- Vai `return` dod funkcijas izsaucējam vērtību, ko var tālāk izmantot?
- Vai protu nodalīt aprēķinu no `input` un `print`?
- Vai zinu, kā importēt funkciju no blakus esoša faila?
- Vai pārbaudu vismaz vienu robežgadījumu, nevis tikai vienu veiksmīgu piemēru?

[Atpakaļ uz konspektu](../../lessons/05_functions_modules/README.md) · [Iepriekšējās nodarbības uzdevumi](../04_collections/README.md).
