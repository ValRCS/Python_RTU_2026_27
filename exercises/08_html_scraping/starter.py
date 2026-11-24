from pathlib import Path
from bs4 import BeautifulSoup

root = Path(__file__).resolve().parents[2]
html = (root / "datasets/book_catalog.html").read_text(encoding="utf-8")
soup = BeautifulSoup(html, "html.parser")

# 1. Virsraksti un saites
print(soup.title.get_text(strip=True))
# TODO: h1, visi h2, saišu skaits

# 2. Saraksts ar vārdnīcām
products = []
# TODO: cikls pār article.product

# 3. Statistika un atlase
# TODO: min, max, vidējā, atlase un kārtošana

# 4. Eksports un pārbaude
# TODO: JSON vai CSV
