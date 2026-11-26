from pathlib import Path

folder = Path("datasets")
print("Mape?", folder.is_dir())
for path in sorted(folder.iterdir()):
    print(path.name, path.stem, path.suffix, path.is_file())
for path in sorted(folder.glob("*.txt")):
    print(path.name)
# Papildu: meklē rekursīvi tikai mācību mapē.
for path in sorted(folder.rglob("*.txt")):
    print(path.relative_to(folder))
