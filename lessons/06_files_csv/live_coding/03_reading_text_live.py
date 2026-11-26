from pathlib import Path

path = Path("datasets/pilsetas.txt")
with path.open(encoding="utf-8") as file:
    text = file.read()
    print(repr(text), type(text))
    print("Otrais read:", repr(file.read()))
with path.open(encoding="utf-8") as file:
    print("Pirmā rinda:", repr(file.readline()))
    print("Atlikušās:", file.readlines())
with path.open(encoding="utf-8") as file:
    for line in file:
        print(repr(line.rstrip("\n")))
print("Rindas:", len(text.splitlines()))
print(path.read_text(encoding="utf-8"))
