# 5. nodarbība — Funkcijas, moduļi un pirmie testi

**Datums:** ceturtdiena, 2026. gada 26. novembris, **17:45–21:40** (MS Teams).  
**Mācību lapa:** [interaktīvā 5. nodarbība](../../docs/lessons/05-functions-modules/index.html)  
**Patstāvīgā prakse:** [5 uzdevumi, pārbaudes un sākuma kods](../../exercises/05_functions_modules/README.md)  
**Iepriekš:** [4. nodarbība — kolekcijas](../04_collections/README.md). **Nākamreiz:** [faili, ceļi un CSV](../06_files_csv/README.md).

## Galvenā ideja

4. nodarbībā uzrakstījām vārdu biežuma skaitītāju un iepirkumu groza cenas aprēķinu. Tagad šos algoritmus **ietinam funkcijās**, lai tos varētu izsaukt atkārtoti, dot tiem citus datus un pārbaudīt rezultātus.

```python
def count_words(text):
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts

result = count_words("Rīga Python Rīga")
print(result)  # {'rīga': 2, 'python': 1}
```

## Sasniedzamie rezultāti

Pēc nodarbības students prot:
1. Uzrakstīt `def`, ievērot atkāpes un **izsaukt** funkciju.
2. Atšķirt **parametru** definīcijā no **argumenta** izsaukumā; izmantot vairākus argumentus.
3. Izskaidrot, ka `print()` attēlo, bet `return` atgriež vērtību, kuru var saglabāt vai izmantot citā izteiksmē.
4. Pārveidot ciklu un vārdnīcu lietojošu kodu par funkciju `count_words(text)`.
5. Saprast, ka funkcijas lokālais mainīgais nav tas pats, kas tāda paša nosaukuma mainīgais ārpus tās.
6. Izmantot `import math` un importēt paša veidotu moduli no blakus esoša `.py` faila.
7. Pārbaudīt funkcijas rezultātus ar `assert`, arī pie tukšas ievades.

**Ja ir laiks:** parametru noklusētās vērtības, atslēgvārdu argumenti, `if __name__ == "__main__"` un `unittest`.  
**Šoreiz neapgūstam:** `*args`, `**kwargs`, `lambda`, dekoratorus, rekursiju, objektorientētas klases, `pytest` un pakotņu instalēšanu. Pie pakotnēm atgriezīsimies 7. nodarbībā.

## Jēdzieni soli pa solim

### 1. Definīcija nav izsaukums

```python
def greet(name):
    print(f"Sveiki, {name}!")

greet("Anna")  # Tikai tagad funkcija izpildās.
```

`name` ir **parametrs**; `"Anna"` ir **arguments**. Funkcijas ķermenis jāatkāpina. Pēc definīcijas nekas netiek izpildīts, kamēr funkciju neizsauc.

### 2. `return` nav `print`

```python
def double_a(number):
    print(number * 2)

def double_b(number):
    return number * 2

a = double_a(5)  # Izdrukā 10; a ir None.
b = double_b(5)  # Nekas netiek izdrukāts; b ir 10.
print(b + 3)     # 13
```

Funkcija bez izpildīta `return` atgriež `None`. `return` arī **pārtrauc** šīs funkcijas izpildi. `print` pats par sevi atgriež `None`.

### 3. Vairākas vērtības un noklusējuma arguments

```python
def add(a, b=0):
    return a + b

print(add(2, 3))       # 5
print(add(2))          # 2
print(add(b=3, a=2))   # 5
```

Sākumā pietiek ar pozicionāliem argumentiem. Atslēgvārdu argumentus un noklusēto `b=0` uztveram kā praktiskus papildinājumus.

### 4. Lokālie mainīgie

```python
city = "Rīga"

def show_city():
    city = "Liepāja"
    return city

print(show_city())  # Liepāja
print(city)         # Rīga
```

`show_city()` izveido **savu** lokālo `city`. Šajā piemērā ārējais `city` paliek nemainīgs. `global` un detalizētu nosaukumu meklēšanas noteikumu teoriju atliekam.

### 5. Modulis: vēl viens Python fails

Fails `word_tools.py` satur funkcijas; blakus esošajā `main.py` tās izsauc:

```python
import word_tools

print(word_tools.count_words("Rīga rīga"))
```

Palaid `main.py` tieši no mapes vai ar zemāk doto komandu. Python meklē `word_tools.py` izpildāmā skripta mapē. `import` var izpildīt moduļa augšējā līmeņa kodu — tādēļ demonstrācijās blakusefektu izvairāmies. Izvēles piemērā `if __name__ == "__main__":` pasargā demonstrāciju no automātiskas izpildes importēšanas laikā.

### 6. Testi: sagaidāmais pret faktisko

```python
assert count_words("") == {}
assert count_words("Python") == {"python": 1}
assert count_words("Rīga rīga") == {"rīga": 2}
```

Ja nosacījums ir aplams, parasti saņemsim `AssertionError`; ja tas ir patiess, `assert` neko nedrukā. Pārbaudi normālu ievadi, tukšu ievadi un robežgadījumu. `assert` nav paredzēts lietotāja datu validēšanai, jo optimizētā režīmā to var izlaist. `unittest` ir standarta bibliotēkā; demonstrēsim, kā vairākus testus palaist atkārtoti.

## Nodarbības ritms

| Laiks | Temats |
| --- | --- |
| 17:45–18:00 | Kolekciju atkārtojums; kāpēc izvairīties no koda dublēšanas |
| 18:00–18:30 | `def`, izsaukšana un atkāpes |
| 18:30–19:05 | Parametri, argumenti, `print` un `return` |
| 19:05–19:25 | `count_words(text)` — iepriekšējā algoritma pārveidošana |
| 19:25–19:35 | Pārtraukums |
| 19:35–19:55 | Lokālie mainīgie; viena funkcija izsauc citu |
| 19:55–20:15 | `math` un paša modulis `word_tools.py` |
| 20:15–20:25 | Pirmās `assert` pārbaudes |
| 20:25–21:05 | Patstāvīgie uzdevumi, 1.–3. obligāti mēģināmi |
| 21:05–21:25 | Pārrunas, kļūdu labošana un alternatīvie risinājumi |
| 21:25–21:35 | `unittest` (papildus) |
| 21:35–21:40 | Kopsavilkums un pāreja uz failiem |

## Izpildāmo piemēru palaišana

Nav jāinstalē papildu pakotnes. Terminālī no **repozitorija saknes**:

```powershell
python lessons/05_functions_modules/01_basic_functions.py
python lessons/05_functions_modules/02_parameters_return.py
python lessons/05_functions_modules/03_word_counter.py
python lessons/05_functions_modules/04_scope.py
python lessons/05_functions_modules/05_modules/main.py
python lessons/05_functions_modules/06_testing.py
python -m unittest discover -s lessons/05_functions_modules/05_modules -p "test_*.py" -v
```

macOS/Linux vajadzības gadījumā lieto `python3` un `python3 -m unittest ...`. Moduļu piemēra `main.py` un `word_tools.py` jāatrodas vienā mapē; lai komandas darbotos, nevajag tīmekļa savienojumu. `unittest` ir **papilddemonstrācija**.

## Tipiskas kļūdas

| Kļūda | Kāpēc tā notiek |
| --- | --- |
| `def greet(name): ...` bez `greet("Anna")` | Definēšana pati par sevi funkciju neizsauc |
| `print(add(1, 2))` pret `result = print(...)` | `print` atgriež `None` |
| `return` ierakstīts ārpus funkcijas | `SyntaxError` |
| Neatbilst argumentu skaits | `TypeError` |
| Mēģina lietot lokālu mainīgo ārpus funkcijas | `NameError`, ja tāds nav definēts ārpusē |
| `math.sqrt(9)` bez `import math` | `NameError` |
| `assert` nekas netiek izdrukāts | Sekmīgs assertions ir kluss |
| `word_tools.py` neatrodas blakus `main.py` | Parasti `ModuleNotFoundError` |

## Turpinājums

6. nodarbībā izmantosim tās pašas funkcijas ar datiem no faila: `read_text(path)` → `count_words(text)` → rezultātu saglabāšana.  
Papildus: [Python pamācība par funkcijām](https://docs.python.org/3/tutorial/controlflow.html#defining-functions), [moduļi](https://docs.python.org/3/tutorial/modules.html), [unittest](https://docs.python.org/3/library/unittest.html), [2024/25 funkciju piemēri](https://github.com/ValRCS/Python_RTU_2024_25/tree/main/topic_7_functions).
