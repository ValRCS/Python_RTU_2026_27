"""4. nodarbība: vārdnīcu atslēgas, vērtības un biežuma skaitīšana."""

student = {"vārds": "Anna", "vecums": 28, "pilsēta": "Rīga"}
print("Vārds:", student["vārds"])

student["vecums"] = 29
student["kurss"] = "Python"

print("Vai ir atslēga 'vārds'?", "vārds" in student)
print("Nezināma atslēga ar get:", student.get("e-pasts", "nav norādīts"))
for key, value in student.items():
    print(key, "→", value)

text = "Rīga Python Rīga dators Python Rīga"
counts = {}
for word in text.lower().split():
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print("Biežumi:", counts)

# Īsāks skaitītāja pieraksts:
short_counts = {}
for word in text.lower().split():
    short_counts[word] = short_counts.get(word, 0) + 1
print("Vienāds rezultāts:", counts == short_counts)

# student["e-pasts"] izraisītu KeyError, ja atslēgas nav.
