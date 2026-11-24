with open("datasets/pilsetas.txt", encoding="utf-8") as file:
    text = file.read()

print(text, end="")
print("Rindas:", len(text.splitlines()))
print("Vārdi:", len(text.split()))
