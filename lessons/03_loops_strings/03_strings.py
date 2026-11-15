"""3. nodarbība: virknes, indeksi, šķēlumi un metodes."""

text = "Rīga"
print("Virkne:", text)
print("Garums:", len(text))  # 4
for character in text:
    print("Rakstzīme:", character)

print("Pirmā:", text[0])   # R
print("Pēdējā:", text[-1])  # a
print("Vidus:", text[1:3])  # īg
print("Atpakaļ:", text[::-1])  # agīR

# str objekts ir nemaināms: text[0] = "L" izraisītu TypeError.
changed = "L" + text[1:]
print("Jauna virkne:", changed)  # Līga
print("Sākotnējā:", text)  # Rīga

sample = "  Banāns  "
print("Bez ārējām atstarpēm:", sample.strip())
print("Mazie burti:", sample.lower())
print("Lielie burti:", sample.upper())
print("Aizvietots:", sample.replace("a", "@"))
print("Burtu 'a' skaits:", sample.count("a"))
print("Sākas ar divām atstarpēm:", sample.startswith("  "))
print("Beidzas ar divām atstarpēm:", sample.endswith("  "))

vowels = "aāeēiīouū"
vowel_count = 0
for character in text.lower():
    if character in vowels:
        vowel_count += 1
print("Patskaņi:", vowel_count)  # 2
