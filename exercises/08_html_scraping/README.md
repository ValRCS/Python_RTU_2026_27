# 8. nodarbība — patstāvīgais darbs (20:20–21:05)

Darba mape: kursa repozitorija sakne. Instalē `python -m pip install -r lessons/08_html_scraping/requirements.txt`. Palaid `python exercises/08_html_scraping/starter.py`. Izmanto lokālo `datasets/book_catalog.html`; ja nav repozitorija, lejupielādē ZIP vai atver nodarbības notebook Colab.

## 1. Lapas virsraksti (7 min)
Izdrukā title, h1, visus h2 un saišu skaitu. Paredzēts: 6 h2, 6 saites. Padoms: find, find_all.

## 2. Grāmatu katalogs (10 min)
Katram article.product izveido vārdnīcu ar name un price (float). Sagaidāmi 6 ieraksti, pirmais Python pamati, 25.90. Padoms: selektorus lieto katra article ietvaros.

## 3. Cenu analīze (13 min)
Aprēķini min, max, vidējo; izdrukā grāmatas zem 30 EUR augošā cenu secībā. Sagaidāms min 15.90, max 39.50, vidējā 26.78; 4 grāmatas zem 30. Padoms: saraksts ar cenām, sorted ar key.

## 4. Saglabāšana (15 min)
Izveido output mapi, saglabā JSON vai CSV ar galveni name,price. Nolasi rezultātu atpakaļ un pārbaudi 6 ierakstus. Padoms: json.dump / json.load vai csv.DictWriter / DictReader; encoding="utf-8", CSV newline="".

Pēc patstāvīga mēģinājuma: [paraugrisinājums](solutions.py), [papildu uzdevumi](bonus.md). Pārbaudi savu programmu arī ar tukšu HTML.
