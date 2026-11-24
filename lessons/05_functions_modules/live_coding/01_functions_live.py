"""Definēšana, izsaukšana un atkāpes. Prognozē pirms palaišanas."""

def greet():
    print("Sveiki, Python!")


def greet_person(name):
    print(f"Sveiki, {name}!")


print("1. Definīcijas ir izpildītas; ķermeņi vēl nav izsaukti.")
greet()
greet_person("Anna")
greet_person("Jānis")

# Prognoze: ko dara nosaukums bez iekavām? Ko dara izsaukums?
print(callable(greet))
result = greet()
print("Atgrieztā vērtība:", result)
# Patstāvīgi: izveido vēl vienu sveicienu un izsauc to divreiz.
