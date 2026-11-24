# 8. nodarbība — HTML un tīmekļa datu iegūšana

[Interaktīvā nodarbība](https://valrcs.github.io/Python_RTU_2026_27/lessons/08-html-scraping/) · [Uzdevumi](../../exercises/08_html_scraping/README.md) · [Dati](../../datasets/README.md)

## Sasniedzamie rezultāti
- Izskaidrot URL, HTTP GET un atbildes statusu; atšķirt lejupielādi no parsēšanas.
- Atrast HTML tagus, atribūtus, klases un elementus ar Beautiful Soup.
- Izveidot sarakstu ar vārdnīcām, pārveidot cenu uz skaitli, saglabāt CSV/JSON.
- Atpazīt trūkstošus laukus, nederīgus datus un tīkla kļūdas.

## Palaide
No repozitorija saknes, izvēlētā .venv vidē: `python -m pip install -r lessons/08_html_scraping/requirements.txt`.
Piemēram, `python lessons/08_html_scraping/03_beautiful_soup.py`. Visas pamata datu apstrādes demonstrācijas darbojas bez tīkla pēc instalēšanas; 01 demonstrē tīklu ar lokālu rezerves variantu. Pandas ir tikai papildu tēma: `python -m pip install -r lessons/08_html_scraping/requirements-bonus.txt`.

## Python piemēri
- [catalog_scraper.py](catalog_scraper.py)
- [01_http_requests.py](01_http_requests.py)
- [02_html_basics.py](02_html_basics.py)
- [03_beautiful_soup.py](03_beautiful_soup.py)
- [04_css_selectors.py](04_css_selectors.py)
- [05_extract_links.py](05_extract_links.py)
- [06_catalog_scraper.py](06_catalog_scraper.py)
- [07_table_extraction.py](07_table_extraction.py)
- [08_export_csv_json.py](08_export_csv_json.py)
- [09_error_handling.py](09_error_handling.py)
- [test_scraping.py](test_scraping.py)

Testi: `python -m unittest discover -s lessons/08_html_scraping -p "test_*.py"`.

## Notebook
- [01_web_scraping_basics.ipynb](01_web_scraping_basics.ipynb) · [Colab](https://colab.research.google.com/github/ValRCS/Python_RTU_2026_27/blob/main/lessons/08_html_scraping/01_web_scraping_basics.ipynb)
- [02_catalog_analysis.ipynb](02_catalog_analysis.ipynb) · [Colab](https://colab.research.google.com/github/ValRCS/Python_RTU_2026_27/blob/main/lessons/08_html_scraping/02_catalog_analysis.ipynb)
- [03_pandas_html_tables_bonus.ipynb](03_pandas_html_tables_bonus.ipynb) · [Colab](https://colab.research.google.com/github/ValRCS/Python_RTU_2026_27/blob/main/lessons/08_html_scraping/03_pandas_html_tables_bonus.ipynb)
Ja pakotņu nav, atkomentē %pip šūnu. Iekļautie HTML dati darbojas bez augšupielādes.

## Avoti un atbildīga datu ieguve
Izmanto mācību katalogu un fiktīvos dzīvokļus. Pirms ārējas vietnes automatizētas ieguves pārbaudi noteikumus, robots.txt, datu izmantošanas tiesības; dod priekšroku API vai lejupielādei. Neapej piekļuves ierobežojumus. [Requests](https://requests.readthedocs.io/) · [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) · [MDN HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) · [2024/25 piemēri](https://github.com/ValRCS/Python_RTU_2024_25/tree/main/topic_15_web_scraping).

[Dzīvā programmēšana](live_coding/README.md) · [Atpakaļ](../../README.md)
