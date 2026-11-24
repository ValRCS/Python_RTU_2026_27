from urllib.parse import urljoin
from bs4 import BeautifulSoup
from catalog_scraper import CATALOG, CATALOG_URL

soup = BeautifulSoup(CATALOG.read_text(encoding="utf-8"), "html.parser")
for link in soup.select("a[href]"):
    print(link.get_text(strip=True), urljoin(CATALOG_URL, link["href"]))
