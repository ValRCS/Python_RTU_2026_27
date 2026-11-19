# Saskaiti latviešu patskaņus a, ā, e, ē, i, ī, o, u, ū. 
# Pārbaudi Rīga → 2, Ābols → 2, brrr → 0.

vowels = "aāeēiīouū"
text = input("Ievadi tekstu: ") # teksts varētu būt ļoti garšs
count = 0
for char in text.lower(): # pārveidojam visu tekstu uz maziem burtiem, lai nebūtu jāuztraucas par lielajiem burtiem
    if char in vowels:
        count += 1
print(f"Patskaņu skaits: tekstā '{text}' ir {count}")