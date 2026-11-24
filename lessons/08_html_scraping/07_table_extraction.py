from bs4 import BeautifulSoup
from catalog_scraper import ROOT

soup = BeautifulSoup((ROOT / "datasets/apartments.html").read_text(encoding="utf-8"), "html.parser")
apartments = []
for row in soup.select("#apartments tbody tr"):
    cells = row.find_all("td")
    if len(cells) != 3:
        continue
    district, area, rent = [cell.get_text(strip=True) for cell in cells]
    apartments.append({"district": district, "area": int(area), "rent": int(rent)})
for row in apartments:
    print(row["district"], round(row["rent"] / row["area"], 2), "EUR/m²")
