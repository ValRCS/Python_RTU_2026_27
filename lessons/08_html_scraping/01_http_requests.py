"""Viens HTTP GET; kļūdas gadījumā izmanto lokālo failu."""
import requests
from catalog_scraper import CATALOG, CATALOG_URL


def download_html(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    print("Statuss:", response.status_code)
    print("Satura tips:", response.headers.get("Content-Type"))
    return response.text


if __name__ == "__main__":
    try:
        html = download_html(CATALOG_URL)
    except requests.RequestException as error:
        print("Tīkla kļūda:", error, "Izmantojam lokālo kopiju.")
        html = CATALOG.read_text(encoding="utf-8")
    print(html[:300])
