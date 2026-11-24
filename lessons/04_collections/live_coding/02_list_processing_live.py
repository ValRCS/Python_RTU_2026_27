"""Skaitļu saraksti, filtrēšana un ievade; bez ārējām pakotnēm."""
import sys

temperatures = [4.5, -2.0, 3.2, -5.1, 1.7]
# Papildus: palaid ar --input, lai ievadītu savus skaitļus.
if "--input" in sys.argv:
    temperatures = []
    while True:
        text = input("Temperatūra (beigt): ").strip()
        if text.lower() == "beigt":
            break
        try:
            number = float(text)
        except ValueError:
            print("Ievadi skaitli, piemēram, -2.5.")
            continue
        temperatures.append(number)

# 1. Apkopojums. Pārbaudi arī temperatures = [].
print("Skaits:", len(temperatures))
print("Summa:", sum(temperatures))
if temperatures:
    print("Vidējā:", sum(temperatures) / len(temperatures))
    print("Min:", min(temperatures), "Max:", max(temperatures))
else:
    print("Nav mērījumu.")

# 2. Atlase: no viena saraksta veido citu.
freezing_days = []
for temperature in temperatures:
    if temperature < 0:
        freezing_days.append(temperature)
print("Sala dienas:", freezing_days)

# 3. Pārveidošana: jauns saraksts, sākotnējais paliek.
numbers = [3, 7, 12, 5, 18, 21, 4]
evens = []
squares = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)
    squares.append(number ** 2)
print(evens)  # [12, 18, 4]
print(squares)

# Papildus tikai pēc cikla izpratnes: list comprehension.
print([number for number in numbers if number % 2 == 0])
