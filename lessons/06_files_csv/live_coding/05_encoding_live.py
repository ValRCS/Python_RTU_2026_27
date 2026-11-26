from pathlib import Path

text = "Rīga"
data = text.encode("utf-8")
print(len(text), len(data), data)
print(data.decode("utf-8"))
path = Path("output/lesson06/encoding.txt")
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(text, encoding="utf-8")
try:
    path.read_text(encoding="ascii")
except UnicodeDecodeError as error:
    print(type(error).__name__, "ASCII nevar attēlot šo tekstu.")
print(path.read_text(encoding="utf-8"))
