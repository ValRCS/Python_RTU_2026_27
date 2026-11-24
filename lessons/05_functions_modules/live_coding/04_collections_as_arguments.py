"""Maināmi objekti: lokāla piesaiste nenozīmē objekta kopiju."""

def add_in_place(products, product):
    products.append(product)


def with_product(products, product):
    return products + [product]


def replace_locally(products):
    products = ["jauns saraksts"]
    return products


basket = ["maize", "piens"]
print("Pirms:", basket)
result = add_in_place(basket, "ābols")
print("Pēc mutācijas:", basket, "return:", result)
new_basket = with_product(basket, "siers")
print("Oriģināls:", basket, "Jauns:", new_basket)
print("Lokāla pārsaiste:", replace_locally(basket), basket)
assert basket == ["maize", "piens", "ābols"]
assert new_basket == ["maize", "piens", "ābols", "siers"]

# Papildus: vārdnīcas mutācija darbojas pēc tā paša principa.
def increase(counts, word):
    counts[word] = counts.get(word, 0) + 1


counts = {}
increase(counts, "rīga")
increase(counts, "rīga")
print(counts)
