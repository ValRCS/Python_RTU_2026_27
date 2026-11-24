import json

with open("datasets/recipes.json", encoding="utf-8") as file:
    data = json.load(file)

for recipe in data["recipes"]:
    if "kartupelis" in recipe["ingredients"]:
        print(recipe["name"], recipe["minutes"], "min")
