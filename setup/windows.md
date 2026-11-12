# Python uzstādīšana — Windows 10/11

1. Atver https://www.python.org/downloads/windows/ un izmanto oficiālo Python instalēšanas risinājumu. Ja instalācijā tiek piedāvāta komandu pieejamības (PATH) konfigurācija, seko norādēm.
2. Aizver un no jauna atver **PowerShell** vai **Command Prompt**.
3. Pārbaudi:
   ```powershell
   python --version
   ```
   Ja komanda nav atrodama, izmēģini:
   ```powershell
   py --version
   ```
4. Pārej uz mapi ar kursa failiem; terminālī palaid:
   ```powershell
   python .\lessons\01_getting_started\hello.py
   ```
   Ja tavā instalācijā darbojas tikai `py`, izmanto `py .\lessons\01_getting_started\hello.py`.
5. Alternatīva: atver failu **IDLE** un izmanto **Run → Run Module (F5)**.

**Biežs Windows gadījums:** `python` atver Microsoft Store vai paziņo, ka Python nav atrodams. Pārbaudi, vai Python tiešām ir instalēts, vai darbojas `py`, un vajadzības gadījumā aplūko Windows *App execution aliases*. Nejauc komandu uzvednes atrašanās vietu ar Python instalācijas vietu.

Pirmajā nodarbībā **neinstalē** `requirements` vai trešo pušu bibliotēkas. Ja datoram ir organizācijas administrēšanas ierobežojumi, paziņo pasniedzējam; var izmantot alternatīvu vidi.

[Atpakaļ pie uzstādīšanas](README.md) · [Kļūdu risināšana](troubleshooting.md)
