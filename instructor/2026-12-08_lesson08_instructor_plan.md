# 8. nodarbība — pasniedzēja plāns: HTML un tīmekļa datu iegūšana

2026-12-08, 17:45–21:40. [Studentu lapa](https://valrcs.github.io/Python_RTU_2026_27/lessons/08-html-scraping/) · [Piemēri](../lessons/08_html_scraping/README.md) · [Dzīvā programmēšana](../lessons/08_html_scraping/live_coding/README.md).

## Pirms nodarbības
- Aktivizē .venv, izvēlies interpretatoru; uzstādi requests, beautifulsoup4. Pārbaudi importus un `python -m unittest discover -s lessons/08_html_scraping -p "test_*.py"`.
- Atver lokālo HTML pārlūkā, GitHub Pages datu lapu, VS Code un notebook. Pārbaudi tīkla pieejamību; ja nav, izmanto lokālo failu. Colab izmanto iekļauto HTML.
- Ja paredzēts pandas bonuss, uzstādi requirements-bonus.txt atsevišķi.

| Laiks | Saturs un demonstrācija |
|---|---|
| 17:45–18:00 | Atkārto JSON, list/dict, pip, notebook. Pajautā, vai HTML arī ir teksts. |
| 18:00–18:25 | Klients/serveris, URL, HTTPS, GET, statusi 200/404/403/429. Salīdzini ar faila lasīšanu. |
| 18:25–18:40 | 02_html_basics.py, Inspect Elements un Network; tagi, klase, ID, href, DOM pret sākotnējo HTML. |
| 18:40–18:50 | Pārtraukums |
| 18:50–19:10 | 01_http_requests.py: timeout, status, raise_for_status, text, fallback. |
| 19:10–19:30 | 03/04/05: find, find_all, select, select_one, get_text, href; paredzi sakritību skaitu. |
| 19:30–19:40 | Pārtraukums |
| 19:40–20:00 | live_coding/01: vispirms virsraksti, tad ieraksti. 07_table_extraction.py: rindas un šūnas. |
| 20:00–20:20 | catalog_scraper.py, 06/08/09: funkcijas, skaitļu konversija, eksports, kļūdas, testēšana. |
| 20:20–21:05 | 4 patstāvīgi uzdevumi (7+10+13+15 min). |
| 21:05–21:15 | Apspried risinājumus un pārbaudes; parādi vismaz vienu kļūdu. |
| 21:15–21:40 | 15 min pandas.read_html; 10 min dinamiskas lapas, atbildīga ieguve, REST API ievads. |

## Dzīvās programmēšanas scenārijs
1. Pārlūkā atver book_catalog.html un Inspect vienu produktu. Parādi, ka h2 nav pašas cenas tags; klase nav ID. Network cilnē apskati dokumenta pieprasījumu.
2. Terminālī parādi `python -m pip show beautifulsoup4`, tad `from bs4 import BeautifulSoup`. Nejauc pakotnes un importa nosaukumu. 
3. Izpildi vienu GET ar timeout, pārbaudi statusu un Content-Type. Parādi tikai pirmās 300 rakstzīmes. Ja lapa nav pieejama, pārej uz vietējo kopiju; neveic atkārtotu pieprasījumu ciklu.
4. Live coding: no soup.find("h1") pārej uz find_all("h2"), select(".price"), select_one(".missing"). Paredzējums: 6 virsraksti, 6 cenas, None. Tad cikls pa article, nevis divu neatkarīgu sarakstu sapārošana.
5. Izveido list[dict] ar name/price, pārraksti izvilkšanu funkcijā. Atsevišķa tīkla funkcija ļauj testēt parsēšanu bez tīkla. Izmanto min/max/vidējo; 160.70 EUR kopā, 26.78 vidēji.
6. Ar pathlib izveido output un saglabā JSON/CSV. Pārbaudi failu atpakaļlasīšanu. Atgādini UTF-8 un CSV newline.
7. Nepilnīgais katalogs: demonstrē None.get_text kļūdu (AttributeError), float("nav zināma") (ValueError), float("NaN") (neizmet izņēmumu); math.isfinite. Derīgi 2, izlaisti 4. Testē tukšu HTML.
8. Pajautā, kāpēc requests neredz JavaScript ielādēto saturu. Iepazīstini ar API kā stabilāku strukturētu datu avotu; neinstalē Selenium.

## Kļūdu diagnostika
| Simptoms | Darbība |
|---|---|
| ModuleNotFoundError | Pārbaudi python -m pip un VS Code interpretatoru |
| Timeout / ConnectionError | Viena mēģinājuma robeža, lokāla kopija |
| HTTPError 403/429 | Pārtrauc; nepārvari liegumu, pārbaudi atļauju |
| None / tukšs saraksts | Inspect, pārbaudi selektoru, izvada fragmentu |
| ValueError / NaN | Atdali teksta normalizāciju, konversiju un galīguma pārbaudi |
| Bojāti burti | UTF-8 failiem, pārbaudi HTTP kodējumu |
| Relatīvs href | urljoin |
| Atšķirīgs DOM | Skati Network response, skaidro JavaScript |

## Prakse un diferenciācija
[Uzdevumi](../exercises/08_html_scraping/README.md), [starter](../exercises/08_html_scraping/starter.py), [risinājumi](../exercises/08_html_scraping/solutions.py), [bonuss](../exercises/08_html_scraping/bonus.md). Lēnākajiem pietiek ar 1–2 un vienu JSON failu ar pasniedzēja palīdzību; ātrākie aprēķina īri/m² un testē bojātos datus. Palūdz studentiem parādīt rezultātu un izskaidrot vienu selektoru.

## Iepriekšējie gadi un drošība
[topic_15_web_scraping](https://github.com/ValRCS/Python_RTU_2024_25/tree/main/topic_15_web_scraping): WebScraping koncepti, Apartments un Tractor cenu analīze, Pandas tabulas; SS.com un Selenium tikai atsaucei. Vecajos piemēros papildini timeout un statusa pārbaudi; nepaļaujies uz fiksētu tabulas indeksu. Neizmanto personas datus vai piekļuves apiešanu. robots.txt nav vispārēja juridiska atļauja; pārbaudi lietošanas noteikumus, API alternatīvas un slodzi.
