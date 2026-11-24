from pathlib import Path
from bs4 import BeautifulSoup

root = Path(__file__).resolve().parents[3]
soup = BeautifulSoup((root / "datasets/book_catalog_incomplete.html").read_text(encoding="utf-8"), "html.parser")

for item in soup.select(".product"):
    title = item.select_one("h2")
    price = item.select_one(".price")
    # Pirms pārbaudes demonstrē title.get_text() un price.get_text() kļūdas.
    if title is None or price is None:
        print("Izlaists: trūkst lauka")
        continue
    try:
        amount = float(price.get_text(strip=True).replace("€", "").replace(",", "."))
    except ValueError:
        print("Izlaists: nederīgs skaitlis")
        continue
    # Vai float("NaN") rada ValueError? Nē! Pievieno math.isfinite pārbaudi.
    print(title.get_text(strip=True), amount)
