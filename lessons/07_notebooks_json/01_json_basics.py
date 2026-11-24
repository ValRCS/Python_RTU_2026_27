import json

city = {"nosaukums": "Rīga", "galvaspilsēta": True, "piezīme": None}
text = json.dumps(city, ensure_ascii=False, indent=4)
print(text)
data = json.loads(text)
print(data["nosaukums"], type(data))
