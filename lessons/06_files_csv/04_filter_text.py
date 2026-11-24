from pathlib import Path

def filter_lines(source, destination, keyword):
    count = 0
    with open(source, encoding="utf-8") as src:
        with open(destination, "w", encoding="utf-8") as dst:
            for line in src:
                if keyword.lower() in line.lower():
                    dst.write(line)
                    count += 1
    return count

Path("output").mkdir(exist_ok=True)
count = filter_lines("datasets/pilsetas.txt", "output/riga.txt", "Rīga")
print("Atlasītas rindas:", count)
