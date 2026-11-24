from catalog_scraper import CATALOG, extract_products

products = extract_products(CATALOG.read_text(encoding="utf-8"))
if products:
    prices = [product["price"] for product in products]
    print(f"Min: {min(prices):.2f}; max: {max(prices):.2f}; vidējā: {sum(prices)/len(prices):.2f}")
    for product in sorted(products, key=lambda row: row["price"]):
        if product["price"] < 30:
            print(product["name"], product["price"])
else:
    print("Nav atrasti produkti")
