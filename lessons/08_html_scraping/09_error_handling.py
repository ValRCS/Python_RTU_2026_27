from bs4 import BeautifulSoup
from catalog_scraper import ROOT, extract_products

html = (ROOT / "datasets/book_catalog_incomplete.html").read_text(encoding="utf-8")
soup = BeautifulSoup(html, "html.parser")
missing = soup.select_one(".unknown")
print("Neatrasts elements:", missing)
# Izmēģini interaktīvi: missing.get_text() -> AttributeError.
for row in soup.select("article.product"):
    price = row.select_one(".price")
    if price is None:
        print("Trūkst cenas")
    else:
        print("Cenas teksts:", price.get_text(strip=True))
products = extract_products(html)
print("Derīgi:", len(products), products)
print("Izlaisti:", len(soup.select("article.product")) - len(products))
