import csv
import json
from pathlib import Path
from bs4 import BeautifulSoup

root = Path(__file__).resolve().parents[2]
soup = BeautifulSoup((root / "datasets/book_catalog.html").read_text(encoding="utf-8"), "html.parser")
print(soup.title.get_text(strip=True))
print(soup.h1.get_text(strip=True))
for h2 in soup.select("h2"):
    print(h2.get_text(strip=True))
print("Saites:", len(soup.select("a[href]")))
products = []
for item in soup.select("article.product"):
    name = item.select_one("h2").get_text(strip=True)
    price = float(item.select_one(".price").get_text(strip=True))
    products.append({"name": name, "price": price})
if products:
    prices = [row["price"] for row in products]
    print(f"{min(prices):.2f}, {max(prices):.2f}, {sum(prices)/len(prices):.2f}")
    for row in sorted(products, key=lambda row: row["price"]):
        if row["price"] < 30:
            print(row)
output = root / "output"
output.mkdir(exist_ok=True)
with (output / "practice_books.json").open("w", encoding="utf-8") as file:
    json.dump(products, file, ensure_ascii=False, indent=2)
with (output / "practice_books.json").open(encoding="utf-8") as file:
    assert json.load(file) == products
with (output / "practice_books.csv").open("w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "price"])
    writer.writeheader()
    writer.writerows(products)
with (output / "practice_books.csv").open(encoding="utf-8", newline="") as file:
    assert len(list(csv.DictReader(file))) == len(products)
print("Pārbaudīts:", len(products))
