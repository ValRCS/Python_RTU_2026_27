"""5. nodarbība: funkcijas definēšana un izsaukšana."""


def greet():
    """Izdrukā vienkāršu sveicienu."""
    print("Sveiki, Python!")


def greet_person(name):
    """Izdrukā personalizētu sveicienu."""
    print(f"Sveiki, {name}!")


print("Funkcija ir definēta, bet vēl nav izsaukta.")
greet()
greet_person("Anna")
greet_person("Jānis")
