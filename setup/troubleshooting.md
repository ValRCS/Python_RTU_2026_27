# Biežākās problēmas

| Simptoms | Iespējamais iemesls | Ko pārbaudīt |
|---|---|---|
| `python` nav atrodams | Nav instalēts vai nav komandu ceļā | Pārbaudi `py --version` Windows vai `python3 --version` macOS/Linux; atkārtoti atver termināli |
| Atveras Microsoft Store | Windows lietotnes izpildes aizstājvārds | Pārbaudi instalāciju un *App execution aliases* |
| `can't open file` | Nepareiza pašreizējā darba mape vai faila nosaukums | `pwd` (macOS/Linux), `Get-Location` (PowerShell), `dir`/`ls` |
| `SyntaxError` | Kļūda kodā (iekavas, pēdiņas, atkāpes) | Izlasi kļūdas rindu un pārbaudi blakus esošās rindas |
| `NameError` | Mainīgais vēl nav definēts vai nosaukums kļūdains | Pārbaudi lielos/mazos burtus un izpildes secību |
| `ValueError` pie `int(input(...))` | Ievadīts teksts, ko nevar pārvērst veselā skaitlī | Ievadi veselu skaitli; vēlāk apgūsim `try/except` |
| `ModuleNotFoundError` | Pakotne nav uzstādīta attiecīgajam interpretatoram | Sākuma nodarbībās izmanto tikai standarta bibliotēku |
| Darbojas IDLE, bet ne terminālī | Atšķirīgi interpretatori vai darba mapes | Pārbaudi Python versiju un faila pilno ceļu |
| Dīvaini burti latviešu tekstā | Termināļa/rediģētāja kodējums | Saglabā avota failu UTF-8; izmēģini citu termināli |
| Programma gaida bez izvades | `input()` gaida atbildi | Ieraksti prasītos datus un nospied Enter |

**Kas jāpieraksta, lūdzot palīdzību:** operētājsistēma, Python versija, izpildītā komanda, pilnais kļūdas paziņojums un minimālais kods. **Nekad** nesūti paroles vai API atslēgas.

Pēc problēmas atrisināšanas pārbaudi:
```python
print("Python darbojas!")
print(2 + 2)
```
Šīs rindas var palaist interaktīvajā Python konsolē; `python` bloka piemērs nav termināļa komanda.
