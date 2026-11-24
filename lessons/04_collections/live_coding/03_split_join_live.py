"""Teksts -> saraksts -> teksts."""
text = "  Rīga   Liepāja  Jelgava  "
words = text.split()
print(words)
print(", ".join(words))
print("\n".join(words))
print(" → ".join(words[::-1]))
print(repr(text))  # Sākotnējā virkne nemainās.

# Atšķirība: whitespace pret tieši norādītu atdalītāju.
print("a  b".split())
print("a  b".split(" "))
print("".split(), "".split(","))
raw = " maize, piens,, ābols "
parts = raw.split(",")
clean = []
for part in parts:
    part = part.strip()
    if part:
        clean.append(part)
print(parts, clean)
print("; ".join(clean))

# join savieno tikai virknes; skaitļus pārveido ar str().
numbers = [10, 20, 30]
strings = []
for number in numbers:
    strings.append(str(number))
print(", ".join(strings))
# ", ".join(numbers)  # TypeError: izmēģini atkļūdošanas failā.
