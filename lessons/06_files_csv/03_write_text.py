from pathlib import Path

# Rakstām tikai mācību rezultātu mapē.
Path("output").mkdir(exist_ok=True)
with open("output/pilsetas_demo.txt", "w", encoding="utf-8") as file:
    file.write("Rīga\n")
with open("output/pilsetas_demo.txt", "a", encoding="utf-8") as file:
    file.write("Cēsis\n")
with open("output/pilsetas_demo.txt", encoding="utf-8") as file:
    print(file.read(), end="")
