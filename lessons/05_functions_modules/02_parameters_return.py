"""5. nodarbība: parametri, argumenti, print un return."""


def double_with_print(number):
    print(number * 2)


def double_with_return(number):
    return number * 2


def add(a, b=0):
    """Atgriež divu skaitļu summu; otrais arguments nav obligāts."""
    return a + b


first = double_with_print(5)  # Ekrānā 10, bet mainīgajā None.
second = double_with_return(5)  # Nekas netiek izdrukāts.
print("print funkcijas atgrieztā vērtība:", first)
print("return funkcijas atgrieztā vērtība:", second)
print("Ar rezultātu var rēķināt:", second + 3)
print("Pozicionālie argumenti:", add(4, 6))
print("Noklusētā vērtība:", add(4))
print("Atslēgvārdu argumenti:", add(b=6, a=4))
