# Funkcijas
print("Runāsim par funkcijām!")

# mēs izmantojam funkcijas lai definētu kodu, ko mēs varam atkārtoti izmantot
def greet_python():
    print("Sveiks, Python!")
    # es varu pielikt klāt vēl vienu print teiksim ar emoji
    print("Priekā 👋")

# funkcijas izsaukums
# greet_python()

# # es varu 3 x izsaukt ar ciklu
# for _ in range(3): # _ representē mainīgo, kuru mēs neizmantojam
#     greet_python()

# meš varam definēt parametrus funkcijās
def greet_person(name):
    print(f"Sveiks, {name}!")

# sveicam valdi
greet_person("Valdis")

# izveidojam sarakstu ar cilvēkiem un sveicam katru no tiem
persons = ["Anna", "Jānis", "Pēteris"]
for person in persons:
    greet_person(person)

# izveidosim funkciju kas pieņem sarakstu ar personām un sveic katru no tiem
def greet_persons(persons):
    for person in persons:
        greet_person(person)

# izsaucam šo funkciju ar sarakstu
greet_persons(persons)

print("Esam beiguši")