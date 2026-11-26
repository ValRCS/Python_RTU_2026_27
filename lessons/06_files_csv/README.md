# 6. nodarbība — Faili, ceļi un CSV

[Interaktīvā nodarbība](https://valrcs.github.io/Python_RTU_2026_27/lessons/06-files-csv/) · [Uzdevumi](../../exercises/06_files_csv/README.md) · [Dati](../../datasets/README.md)

## Sasniedzamie rezultāti
- Izskaidrot darba mapi, relatīvos un absolūtos ceļus; izmantot pathlib.
- Lasīt/rakstīt UTF-8 failus ar with open un r/w/a režīmiem.
- Apstrādāt CSV ar csv.reader, DictReader un DictWriter, pārveidot laukus skaitļos.
- Apstrādāt paredzamas kļūdas un saglabāt avota datus.

## Palaide
Atver repozitorija saknes mapi. Palaid, piemēram, `python lessons/06_files_csv/06_expense_summary.py` (Windows: var lietot py; macOS/Linux: python3). Nav vajadzīgas ārējas pakotnes. Rezultāti glabājas jaunā output/ mapē. Pārbaudi ceļu ar 01_paths.py.

- [01_paths.py](01_paths.py)
- [02_read_text.py](02_read_text.py)
- [03_write_text.py](03_write_text.py)
- [04_filter_text.py](04_filter_text.py)
- [05_read_csv.py](05_read_csv.py)
- [06_expense_summary.py](06_expense_summary.py)
- [07_write_csv.py](07_write_csv.py)
- [08_file_errors.py](08_file_errors.py)

Kopējā izdevumu summa 35.00 EUR; food 13.50, transport 3.00, books 15.60, household 2.90. Pamatuzdevumi 45 min; papildu: vairāki faili, teksta analīze, bojāti ieraksti. [2024/25 failu materiāli](https://github.com/ValRCS/Python_RTU_2024_25/tree/main/topic_12_paths_folders_file_reading_writing).

[Atpakaļ](../../README.md)

## Izvērstie materiāli

- [12 live coding demonstrācijas](live_coding/README.md)
- [Patstāvīgā darba sākuma fails](../../exercises/06_files_csv/starter.py)
- [Papildu uzdevumi 6.5–6.15](../../exercises/06_files_csv/bonus.md)
- Pārbaudes: `python -m unittest discover -s exercises/06_files_csv -p "test_*.py" -v`
- Lieto output/ rezultātiem; mape izslēgta no Git. Ja fails nav atrodams, pārbaudi Path.cwd() un resolve().
