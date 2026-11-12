# Python programmēšanas pamati pieaugušajiem | RTU 2026/27

Praktisks **12 nodarbību Python kurss iesācējiem**. Priekšzināšanas programmēšanā nav nepieciešamas. Kurss paredzēts pieaugušajiem, kuri vēlas patstāvīgi veidot nelielas programmas, apstrādāt datus un iepazīt automatizāciju.

**Pirmā nodarbība (2026. gada rudens): 12. novembrī, plkst. 17:45–21:40.**

> Šis repozitorijs ir **studentiem paredzētā 2026/27 kursa darba vide**. 12 lekciju plāns ir pamats; uzdevumi un papildu materiāli tiks papildināti kursa gaitā. Nākamā gada kursam laika grafiks būs atsevišķs, neatkarīgi no kopīgajiem mācību materiāliem.

## Sāc šeit

1. Izlasi [uzstādīšanas un darba vides ceļvedi](setup/README.md), izvēlies savu operētājsistēmu un pārbaudi Python versiju.
2. Atver [1. nodarbību](lessons/01_getting_started/README.md) un palaid `hello.py`.
3. Izdari [pirmās nodarbības uzdevumus](exercises/01_getting_started/README.md).
4. Nākamo lekciju materiāli atrodami zemāk. Failus var lejupielādēt ar **Code → Download ZIP** — Git nav obligāts.

**2026. gada rudens nodarbību datumi:** [cohorts/2026_fall.md](cohorts/2026_fall.md).  
**Oficiālais programmas apraksts:** https://digitalasprasmes.lv/module_nva/python.php

## Mācību temati (12 nodarbības)

| Nr. | Temats | Materiāli |
|---:|---|---|
| 1 | Ievads Python un pirmā programma | [Atvērt](lessons/01_getting_started/README.md) |
| 2 | Datu tipi, operatori un nosacījumi | [Atvērt](lessons/02_types_conditions/README.md) |
| 3 | Cikli un virknes | [Atvērt](lessons/03_loops_strings/README.md) |
| 4 | Kolekcijas: saraksti un vārdnīcas | [Atvērt](lessons/04_collections/README.md) |
| 5 | Funkcijas, moduļi un pirmie testi | [Atvērt](lessons/05_functions_modules/README.md) |
| 6 | Faili, ceļi un CSV | [Atvērt](lessons/06_files_csv/README.md) |
| 7 | Pakotnes, Jupyter/Colab un JSON | [Atvērt](lessons/07_notebooks_json/README.md) |
| 8 | HTML un tīmekļa datu iegūšana | [Atvērt](lessons/08_html_scraping/README.md) |
| 9 | REST API un datu apstrāde | [Atvērt](lessons/09_rest_apis/README.md) |
| 10 | Datu bāzes un SQL | [Atvērt](lessons/10_sqlite/README.md) |
| 11 | Automatizācija un Flask ievads | [Atvērt](lessons/11_automation_flask/README.md) |
| 12 | Noslēguma mini-projekti un atkārtojums | [Atvērt](lessons/12_final_project/README.md) |

## Kā strādāsim

- Sākumā lietosim **lokāli uzstādītu Python** un vienkāršus `.py` failus. IDLE darbojas kā viegla iesācēju vide; Visual Studio Code ir izvēles iespēja.
- Vēlāk iepazīsim **Jupyter un Google Colab** datu, JSON un API uzdevumiem: [Colab ceļvedis](setup/colab.md).
- Sākuma nodarbībām pietiek ar Python **standarta bibliotēku**. Nav jāinstalē visi iespējamie `pip` pakotņu saraksti pirmajā dienā.
- Katrā nodarbībā ir mērķi, neliels praktisks darbs un pašpārbaudes uzdevums. Daļa turpmāko nodarbību lapu pašlaik ir **plāns**, nevis jau pabeigts lekcijas konspekts.

## Repozitorija saturs

- [setup/](setup/README.md) — Windows, macOS, Linux, Colab, biežākās kļūdas
- [lessons/](lessons/01_getting_started/README.md) — 12 nodarbības, pirmie piemēri un turpmāko tēmu aprises
- [exercises/](exercises/README.md) — uzdevumi un sagaidāmie rezultāti
- [datasets/](datasets/README.md) — mazi, reproducējami treniņdati
- [projects/](projects/README.md) — mini-projekts un vērtēšanas kritēriji
- [instructor/](instructor/README.md) — publiski pasniedzēja organizatoriskie norādījumi
- [cohorts/](cohorts/2026_fall.md) — konkrētā kursa grafiks

## Agrākie kursi un papildmateriāli

- [Python_RTU_2024_25](https://github.com/ValRCS/Python_RTU_2024_25) — plašāks iepriekšējo gadu piemēru arhīvs; tas **nav** šī kursa nodarbību secība.
- [Python dokumentācija](https://docs.python.org/3/) — oficiālā valodas dokumentācija.
- [Python lejupielāde](https://www.python.org/downloads/) — oficiālais izplatīšanas avots.

## Ja kaut kas nedarbojas

Sāc ar [troubleshooting.md](setup/troubleshooting.md). Kursa laikā ir normāli saņemt `SyntaxError`, `NameError` un `ValueError`: mācāmies izlasīt kļūdas paziņojumu un to labot.

Materiāli paredzēti mācībām; nepublicē repozitorijā paroles, API atslēgas vai personas datus. Skatīt [CONTRIBUTING.md](CONTRIBUTING.md) un [LICENSE](LICENSE).
