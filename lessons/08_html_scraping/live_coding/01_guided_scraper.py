from pathlib import Path
from bs4 import BeautifulSoup

root = Path(__file__).resolve().parents[3]
html = (root / "datasets/book_catalog.html").read_text(encoding="utf-8")
soup = BeautifulSoup(html, "html.parser")

# 1. Viens elements
print(soup.find("h1").get_text(strip=True))
# 2. Visi virsraksti
for heading in soup.select("h2"):
    print(heading.get_text(strip=True))
# 3. Saistām laukus viena article ietvaros
products = []
for item in soup.select(".product"):
    name = item.select_one("h2").get_text(strip=True)
    price = float(item.select_one(".price").get_text(strip=True))
    products.append({"name": name, "price": price})
# 4. Analīze
print(products)
print("Kopā:", round(sum(row["price"] for row in products), 2))
