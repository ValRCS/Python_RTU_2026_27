from pathlib import Path

source = Path("datasets/sample_texts")
output = Path("output/lesson06/filtered")
output.mkdir(parents=True, exist_ok=True)
for path in sorted(source.glob("*.txt")):
    count = 0
    with path.open(encoding="utf-8") as src, (output / path.name).open("w", encoding="utf-8") as dst:
        for line in src:
            if "rīga" in line.lower():
                dst.write(line)
                count += 1
    print(path.name, count)
