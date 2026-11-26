from pathlib import Path

print("Darba mape:", Path.cwd())
print("Mājas mape:", Path.home())
path = Path("datasets") / "pilsetas.txt"
print(path, path.resolve(), path.is_file())
root = Path(__file__).resolve().parents[3]
print("No skripta:", (root / "datasets" / "pilsetas.txt").is_file())
# Windows: Path("C:/Users/Anna/data.txt") vai Path(r"C:\Users\Anna\data.txt")
