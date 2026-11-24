from bs4 import BeautifulSoup
from catalog_scraper import CATALOG

soup = BeautifulSoup(CATALOG.read_text(encoding="utf-8"), "html.parser")
for selector in ["h2", ".price", "#catalog", "article.product", ".product h2", "a[href]", ".missing"]:
    matches = soup.select(selector)
    print(selector, len(matches))
first = soup.select_one(".price")
if first is not None:
    print(float(first.get_text(strip=True)))
