"""HTML parsēšana bez tīkla pieprasījumiem."""
from math import isfinite
from pathlib import Path
from urllib.parse import urljoin

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[2]
CATALOG = ROOT / "datasets" / "book_catalog.html"
CATALOG_URL = "https://valrcs.github.io/Python_RTU_2026_27/datasets/book_catalog.html"


def parse_price(text):
    """Atbalsta punktu vai komatu kā decimālatdalītāju, ne tūkstošu grupēšanu."""
    value = float(text.strip().removesuffix("€").strip().replace(",", "."))
    if not isfinite(value) or value < 0:
        raise ValueError("Nederīga cena")
    return value


def extract_products(html, base_url=CATALOG_URL):
    soup = BeautifulSoup(html, "html.parser")
    products = []
    for item in soup.select("article.product"):
        title = item.select_one("h2")
        price = item.select_one(".price")
        if title is None or price is None:
            continue
        name = title.get_text(strip=True)
        if not name:
            continue
        try:
            amount = parse_price(price.get_text(strip=True))
        except ValueError:
            continue
        category = item.select_one(".category")
        link = item.select_one("a[href]")
        products.append({
            "name": name,
            "price": amount,
            "category": category.get_text(strip=True) if category else "",
            "url": urljoin(base_url, link["href"]) if link else "",
        })
    return products


if __name__ == "__main__":
    products = extract_products(CATALOG.read_text(encoding="utf-8"))
    for product in products:
        print(product["name"], product["price"])
    print("Ieraksti:", len(products))
