import csv
import json
from catalog_scraper import ROOT, CATALOG, extract_products

products = extract_products(CATALOG.read_text(encoding="utf-8"))
output = ROOT / "output"
output.mkdir(exist_ok=True)
with (output / "books.json").open("w", encoding="utf-8") as file:
    json.dump(products, file, ensure_ascii=False, indent=2)
with (output / "books.csv").open("w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "price", "category", "url"])
    writer.writeheader()
    writer.writerows(products)
with (output / "books.json").open(encoding="utf-8") as file:
    assert json.load(file) == products
print("Saglabāti ieraksti:", len(products))
