# Visual Studio Code (VS Code) uzstādīšana un pirmā Python programma

**1. nodarbības papildu ceļvedis iesācējiem. Pārbaudīts pēc oficiālās dokumentācijas 2026. gada 12. novembrī.**

Šajā kursā var strādāt ar **IDLE** vai **Visual Studio Code (VS Code)**. VS Code nav obligāts, bet tas noderēs arī turpmākās nodarbībās. Pirmajā dienā pietiek ar vienu veiksmīgi palaistu `.py` failu; nav jāapgūst visas redaktora iespējas.

## 1. Trīs dažādas lietas

| Komponents | Kam tas vajadzīgs? |
|---|---|
| **Python 3** | Interpretators, kas **izpilda** Python programmu. To instalē atsevišķi. |
| **VS Code** | Redaktors, kurā atver mapes, raksta un saglabā failus. |
| **Python paplašinājums (extension)** | Savieno VS Code ar Python: koda papildināšana, interpretatora izvēle, palaišana, atkļūdošana. |

**Svarīgi:** instalējot tikai VS Code vai Python paplašinājumu, pats Python interpretators netiek instalēts.

Vispirms uzstādi Python saskaņā ar sava datora instrukciju: [Windows](../../setup/windows.md), [macOS](../../setup/macos.md) vai [Linux](../../setup/linux.md).

Atver sistēmas termināli un pārbaudi Python versiju:

- **Windows (PowerShell):** `python --version`. Ja nedarbojas, izmēģini `py --version`.
- **macOS / Linux (Terminal):** `python3 --version`.

Jāparādās `Python 3.x.y` (konkrētais versijas numurs var atšķirties). Ja neredzi versiju, atrisini Python instalēšanas problēmu **pirms** nākamajiem soļiem.

## 2. Instalē VS Code

Atver **[oficiālo VS Code lejupielādes lapu](https://code.visualstudio.com/download)** un izvēlies **Stable** versiju savai operētājsistēmai.

### Windows 10/11

1. Izvēlies **Windows User Installer** (parasti nav vajadzīgas administratora tiesības).
2. Palaid lejupielādēto `.exe` un izpildi instalētāja norādes.
3. Atver **Visual Studio Code** no Start izvēlnes.
4. Ja vēlāk vēlies lietot komandu `code .`, aizver un atver termināli no jauna, lai atjaunotos `PATH`. Šī komanda pirmajā dienā **nav nepieciešama**.

[Oficiālā Windows instrukcija](https://code.visualstudio.com/docs/setup/windows).

### macOS

1. Lejupielādē macOS `.dmg` (piemērotu Intel vai Apple silicon datoram).
2. Atver `.dmg` un pārvelc **Visual Studio Code.app** uz **Applications**.
3. Palaid VS Code no Applications vai Spotlight.

Ja vēlāk vajag termināļa komandu `code .`, VS Code komandu paletē (Cmd+Shift+P) meklē **Shell Command: Install 'code' ... in PATH**. Tas **nav obligāti**, lai programmētu.

[Oficiālā macOS instrukcija](https://code.visualstudio.com/docs/setup/mac).

### Linux (piemēram, Ubuntu, Linux Mint, Fedora)

1. Lejupielādes lapā izvēlies savai sistēmai atbilstošu pakotni: **`.deb`** Debian/Ubuntu/Mint vai **`.rpm`** Fedora/RHEL.
2. Atver pakotni grafiskajā pakotņu pārvaldniekā un instalē. Ubuntu/Debian gadījumā to var arī izdarīt terminālī no lejupielādes mapes: `sudo apt install ./faila_nosaukums.deb` (aizstāj ar īsto faila nosaukumu).
3. Atver VS Code no lietotņu izvēlnes. Python pārbaudei Linux parasti lieto `python3 --version`.

[Oficiālā Linux instrukcija](https://code.visualstudio.com/docs/setup/linux).

## 3. Instalē Microsoft Python paplašinājumu

1. Atver VS Code.
2. Kreisajā malā izvēlies **Extensions** (paplašinājumu ikona). Saīsne: **Ctrl+Shift+X** Windows/Linux vai **Cmd+Shift+X** macOS.
3. Meklē **Python**.
4. Izvēlies paplašinājumu **Python**, kura izdevējs ir **Microsoft** (identifikators: `ms-python.python`), un spied **Install**.
5. Paplašinājums var uzstādīt vai ieteikt arī **Pylance** un **Python Debugger** — tas ir normāli. **Code Runner** paplašinājums šim kursam nav vajadzīgs.

**Nav vajadzīgs:** GitHub konts, Git, Copilot, maksas abonements vai papildu Python pakotnes. Ja VS Code piedāvā pierakstīties vai ieslēgt AI funkcijas, to var izlaist.

[Oficiālā Python integrācijas instrukcija](https://code.visualstudio.com/docs/languages/python).

## 4. Atver kursa mapi (ne tikai atsevišķu failu)

1. Atver [kursa repozitoriju GitHub](https://github.com/ValRCS/Python_RTU_2026_27).
2. Izvēlies **Code → Download ZIP**, saglabā failu un **izpako** to, piemēram, mapē Documents. Git instalācija nav vajadzīga.
3. VS Code izvēlies **File → Open Folder** (macOS arī **File → Open Folder**) un atver izpakoto `Python_RTU_2026_27-main` mapi.
4. Ja parādās jautājums par uzticēšanos mapei (**Workspace Trust**), apstiprini tikai tad, ja atpazīsti paša lejupielādēto kursa repozitoriju.
5. Kreisajā **Explorer** panelī atrodi `lessons/01_getting_started/hello.py` un atver to.

Mapes atvēršana palīdz VS Code pareizi atrast failus un izmantot termināli. Ja lejupielādēji ZIP, nesāc rakstīt kodu pašā ZIP arhīvā — vispirms izpako!

## 5. Izvēlies Python interpretatoru

1. Atver `hello.py` — faila beigās jābūt paplašinājumam `.py`.
2. Atver **Command Palette**: **Ctrl+Shift+P** (Windows/Linux) vai **Cmd+Shift+P** (macOS).
3. Ieraksti un izvēlies **Python: Select Interpreter**.
4. Sarakstā izvēlies savu instalēto **Python 3** interpretatoru. Tas var būt atzīmēts kā **Global**, **System**, **Recommended** vai ar konkrētu faila ceļu.
5. Izvēlētais interpretators parasti redzams arī VS Code statusa joslā.

Ja paplašinājums piedāvā **Create Environment**, pirmajā nodarbībā **nav nepieciešams** veidot virtuālo vidi: pietiek ar jau instalētu Python 3. Pie `.venv` un pakotņu pārvaldības atgriezīsimies vēlāk.

[Oficiālā interpretatoru izvēles instrukcija](https://code.visualstudio.com/docs/python/environments).

## 6. Palaid `hello.py`

Atvērtajā failā `lessons/01_getting_started/hello.py`:

1. Nospied **Ctrl+S** (macOS: **Cmd+S**), lai saglabātu izmaiņas.
2. Redaktora augšējā labajā stūrī nospied **▶ Run Python File** (*Run Python File in Terminal*).
3. Apakšā jāatveras panelim **Terminal** ar programmas izvadi. Starp citu, šī nav `Output` vai `Debug Console` cilne.

Sagaidāmajā izvadē būs, piemēram:

```text
Sveiki, Python!
2 + 2 = 4
Sveiks, Students
```

Failā ir arī vēl citas rindas, tostarp emocijzīme. Precīza izvade ir atkarīga no konkrētā faila satura.

**Otrs veids — terminālī:** izvēlies **Terminal → New Terminal**. Ja terminālis ir atvērts repozitorija saknes mapē, palaid:

**Windows:**

```powershell
python lessons/01_getting_started/hello.py
```

Ja `python` nedarbojas, bet `py` darbojas:

```powershell
py lessons/01_getting_started/hello.py
```

**macOS / Linux:**

```bash
python3 lessons/01_getting_started/hello.py
```

Ja failu neatrod, pārbaudi, vai terminālis atrodas pareizajā **mapē**. VS Code terminālī tās ceļš redzams pirms komandas. Parasti `Terminal → New Terminal` atver termināli pašreizējās darba mapes kontekstā.

## 7. Mazais patstāvīgais uzdevums

Tajā pašā `01_getting_started` mapē izveido jaunu failu `mans_sveiciens.py` (Explorer panelī **New File**). Ieraksti:

```python
print("Sveiki, Python!")
vards = input("Kā tevi sauc? ")
print(f"Prieks iepazīties, {vards}!")
```

Saglabā ar **Ctrl+S / Cmd+S**, tad palaid ar **▶ Run Python File**. Terminālī ieraksti savu vārdu un spied **Enter**.

**Pašpārbaude:** vari nosaukt, kurš ir redaktors, kurš — interpretators, atrast savu `.py` failu un palaist to vēlreiz pēc izmaiņām.

## 8. Ja kaut kas nedarbojas

| Problēma | Ko darīt |
|---|---|
| VS Code rāda **Select Interpreter** vai **No interpreter selected** | Izpildi **Python: Select Interpreter** un izvēlies instalēto Python 3; ja tāda nav, pārbaudi Python instalāciju ārpus VS Code. |
| `python` nav atrodams Windows | Izmēģini `py --version`; atver jaunu termināli un skati [Windows instrukciju](../../setup/windows.md). |
| `python3` nav atrodams macOS/Linux | Vispirms uzstādi/pārbaudi Python 3 atbilstoši [macOS](../../setup/macos.md) vai [Linux](../../setup/linux.md) instrukcijai. |
| `can't open file` vai `No such file or directory` | Pārliecinies, ka ir izpakots ZIP un ar **Open Folder** atvērta pareizā mape. |
| Kods nepalaižas un redzams tikai `>>>` | Tu esi interaktīvajā Python konsolē, nevis komandu terminālī. Ievadi `exit()`, spied Enter un pēc tam palaid failu terminālī. |
| Programma šķiet apstājusies pie `input()` | Tas ir normāli: terminālī ieraksti atbildi un spied **Enter**. |
| Nav redzams **Run Python File** | Pārbaudi, vai fails beidzas ar `.py` un Microsoft Python paplašinājums ir uzstādīts/ieslēgts. |
| `code .` nav atpazīts | Atver VS Code ar lietotnes ikonu un izvēlies **File → Open Folder**; termināļa saīsne nav nepieciešama. |
| Rādās kļūda pēc izmaiņām | Saglabā failu, izlasi precīzo kļūdas tekstu un rindiņas numuru; salīdzini ar piemēru. |

Vairāk: [kursa biežāko problēmu ceļvedis](../../setup/troubleshooting.md).

## Oficiālās atsauces

- [VS Code lejupielāde](https://code.visualstudio.com/download)
- [VS Code Python pamācība](https://code.visualstudio.com/docs/python/python-tutorial)
- [Python atbalsts VS Code](https://code.visualstudio.com/docs/languages/python)
- [Python instalācija](https://www.python.org/downloads/)

**Atpakaļ:** [1. nodarbība](README.md) · [Darba vides uzstādīšana](../../setup/README.md)
