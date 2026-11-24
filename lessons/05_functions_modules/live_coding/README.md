# 5. nodarbība — izvērstie dzīvās programmēšanas piemēri

Papildina sešus īsos pamata piemērus. VS Code: prognoze → palaišana → izmaiņa → atkārtota pārbaude. Ne visi bloki jādemonstrē. Viss darbojas ar Python 3 standarta bibliotēku.

| Fails | Saturs | Prioritāte |
| --- | --- | --- |
| [01_functions_live.py](01_functions_live.py) | Definīcija, izsaukums, None | Pamati |
| [02_parameters_arguments_live.py](02_parameters_arguments_live.py) | Parametri, argumenti, noklusējumi, TypeError | Pamati; noklusējumi papildus |
| [03_return_values_live.py](03_return_values_live.py) | print/return, agrīna atgriešana, kortežu izpakošana | Pamati |
| [04_collections_as_arguments.py](04_collections_as_arguments.py) | Mutācija pret jaunu sarakstu | Papildus |
| [05_refactoring_algorithms_live.py](05_refactoring_algorithms_live.py) | Vārdu biežums, aprēķins atsevišķi no I/O | Pamati |
| [06_scope_and_composition_live.py](06_scope_and_composition_live.py) | Lokālie mainīgie, funkciju kompozīcija, VS Code debugger | Pamati |
| [07_standard_library_live.py](07_standard_library_live.py) | math, random, statistics, datetime | Izvēlēties 1–2 piemērus |
| [08_custom_modules](08_custom_modules/) | Paša modulis, main, unit tests | Pamati; guard un unittest papildus |
| [09_testing_live.py](09_testing_live.py) | assert, robežgadījums, kļūme, float | Pamati |
| [10_debugging_functions.py](10_debugging_functions.py) | Agrīns return, trūkstošs return, kļūdas zari | Apspriede |
| [11_advanced_functions_bonus.py](11_advanced_functions_bonus.py) | Anotācijas, *args, maināma noklusējuma vērtība, rekursija | Tikai pēc pamatprakses |

No repozitorija saknes:

```powershell
python lessons/05_functions_modules/live_coding/03_return_values_live.py
python lessons/05_functions_modules/live_coding/05_refactoring_algorithms_live.py
python lessons/05_functions_modules/live_coding/05_refactoring_algorithms_live.py --input
python lessons/05_functions_modules/live_coding/08_custom_modules/main.py
python -m unittest discover -s lessons/05_functions_modules/live_coding/08_custom_modules -v
```

macOS/Linux: ja nepieciešams, lieto python3. Bez --input demonstrācijas neprasa lietotāja ievadi. Kļūdainie piemēri ir apzināti un komentēti; apstrādātie izņēmumi nepārtrauc demonstrāciju.

**VS Code atkļūdošana:** atver 06_scope_and_composition_live.py, ieliec breakpoint pie result, izvēlies Python Debugger → Python File (F5), Step Into (F11), Step Over (F10), Step Out (Shift+F11). Variables un Call Stack rāda atšķirīgus izsaukuma kontekstus. Ja paplašinājums nav pieejams, izseko izsaukumu ar īsām print rindām.

Iedvesma: [2024/25 funkciju piemēri](https://github.com/ValRCS/Python_RTU_2024_25/tree/main/topic_7_functions).
