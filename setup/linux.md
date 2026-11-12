# Python uzstādīšana — Linux

Atver termināli un pārbaudi Python:
```bash
python3 --version
```

Ja Python nav, lieto savas izplatīšanas oficiālo pakotņu pārvaldnieku. Piemēram, **Ubuntu/Debian**:
```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
```
Citiem distributīviem komandas atšķiras. Redaktoram var izmantot iecienīto teksta redaktoru, IDLE (ja pieejams) vai VS Code.

Lejupielādē kursa ZIP, izpako un palaid no repozitorija saknes:
```bash
python3 lessons/01_getting_started/hello.py
```

**Piezīme:** Pirmajai nodarbībai nevajag `pip install`. Vēlāk instalējamās pakotnes ieteicams izolēt virtuālajā vidē, nemainot sistēmas Python.

[Atpakaļ pie uzstādīšanas](README.md) · [Kļūdu risināšana](troubleshooting.md)
