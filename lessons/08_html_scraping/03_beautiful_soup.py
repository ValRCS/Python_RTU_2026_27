from bs4 import BeautifulSoup
from catalog_scraper import CATALOG

soup = BeautifulSoup(CATALOG.read_text(encoding="utf-8"), "html.parser")
print(soup.title.get_text(strip=True))
print(soup.find("h1").get_text(strip=True))
for heading in soup.find_all("h2"):
    print(heading.get_text(strip=True))
print("Saites:", len(soup.find_all("a", href=True)))
