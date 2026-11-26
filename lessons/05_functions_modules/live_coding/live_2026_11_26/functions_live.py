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

# mēs varam atgriezt arī vertības no funkcijām
# teiksim mēs gribam aprēķināt kvadrātu no skaitļa
def square(number):
    return number ** 2

#izsaucam funkciju un saglabājam rezultātu mainīgajā
result = square(5) 

print(f"Kvadrāts no 5 ir {result}")

# izrēķināsim kvadrātus no pirmiem desmit skaitļiem
# for i in range(1, 11):
#     print(f"Kvadrāts no {i} ir {square(i)}")

# mēs varētu definēt drukāšanas funkciju kvadrātiem
def print_square(number):
    print(f"Kvadrāts no {number} ir {square(number)}")

# un izsaukt pirmiem 5
for i in range(1, 6):
    print_square(i)

# labas funkcijas nav pārāk garas un tās dara vienu lietu,
#  tāpēc mēs varam sadalīt funkcijas mazākās daļās

# mēs taču varētu uztaisīt funkciju kas ņem sākuma skaitli un beigu skaitli un izdrukā kvadrātus no visiem skaitļiem šajā intervālā
def print_squares_in_range(start, end):
    for i in range(start, end + 1):
        print_square(i)

# tad es varu rakstīt šādi:
print_squares_in_range(1, 5)

# es varētu veidot arī funkciju kas saglabā kvadrātus sarakstā un atgriež to
def get_squares_in_range(start=1, end=5):
    squares = [] # jauns saraksts
    for i in range(start, end + 1):
        squares.append(square(i))
    return squares

my_squares = get_squares_in_range(10, 15)
print(my_squares)


# let's make a power function that has default power 2
def power(number, exponent=2): # noklusētam vērtībām jābūt beigās
    return number ** exponent

# ideja ja nav dots eksponents, tad tiek izmantots 2
print(power(3)) # 9
print(power(3, 4)) # 81

# es varu lietot default vērtības tagad get squares_in_range funkcijā
print(get_squares_in_range()) # default 1, 5

# kā izsaukt funkcijua ja man interesē tikai beigu vērtība, bet sākuma vērtība lai paliek default
print(get_squares_in_range(end=10)) # default start 1, end 10

# piemēram print es varu nomainīt end
print("Bez jaunas rindas", end=" ") # default end="\n"
# varam beigt ar emoji vienmēr
print("Lielisks alus! 🍺", end="XXX\n") # default end="\n"

a, b, c = 1, 2, 3
print(a, b, c, sep=" | ") # default sep=" "

# mēs varam arī nedaudz aprakstīt funkcijas, lai tās būtu vieglāk saprotamas
def greet_person_with_docstring(name):
    """Sveicina personu ar dotu vārdu
    Args:
        name (str): Personas vārds
    Returns:
        None
    """
    print(f"Sveiks, {name}!")

# tagad ja es rakstu help(greet_person_with_docstring) es redzu aprakstu
greet_person_with_docstring("Anna")

# par to None, ja navc return tad atgriež None, bet ja ir return tad atgriež to ko returnē
result = greet_person_with_docstring("Jānis")
print(result) # None

# izmantojot noklusētās vērtības un aprakstus, mēs varam veidot ļoti elastīgas funkcijas, kuras ir viegli saprotamas un atkārtoti lietojamas.
# rēķināsim laukumu apļiem, taisnstūriem un trijstūriem
def circle_area(radius, precision=4, debug=False):
    """Aprēķina apļa laukumu pēc dotā rādiusa.
    
    Args:
        radius (float): Apļa rādiuss.
        precision (int): Precizitāte ciparos pēc komata. Noklusētā vērtība ir 4.
        debug (bool): Ja True, tad izdrukā debug informāciju. Noklusētā vērtība ir False.
    Returns:
        float: Apļa laukums.
    """

    import math # importējam math moduli, lai izmantotu pi
    # ļoti tipiski funkcijām mēs izveidojam mainīgos, kas ir atkarīgi no parametriem, un tad atgriežam rezultātu
    result = round(math.pi * radius ** 2, precision)
    if debug:
        print(f"Debug: radius={radius}, area={result}")
    return result

# varam izsaukt šo funkciju
print(f"Apļa laukums ar rādiusu 5 ir {circle_area(5)}")
# ja es gribu teiksim 6 ciparu precizitāti
print(f"Apļa laukums ar rādiusu 5 ir {circle_area(5, precision=6)}")

# varam tagad izmanit debug vērtību
# varu arī rezultātu globāli saglabāt mainīgajā, izmantot to vēlāk
circle_10_area = circle_area(10, debug=True)
print(f"Apļa laukums ar rādiusu 10 ir {circle_10_area}")
# print(f"Apļa laukums ar rādiusu 10 ir {circle_area(10, debug=True)}")

#Vēl viena lieta ar funkcijām mēs varam ieteikt datu tipus - type hints
def rectangle_area(width: float, height: float) -> float:
    """Aprēķina taisnstūra laukumu pēc dotajiem platuma un augstuma.
    
    Args:
        width (float): Taisnstūra platums.
        height (float): Taisnstūra augstums.
    Returns:
        float: Taisnstūra laukums.
    """
    return width * height

rectange_area = rectangle_area(5, 10)
print(f"Taisnstūra laukums ar platumu 5 un augstumu 10 ir {rectange_area}")

# type hints ir tikai ieteikums, Python tos nepiemēro, 
# bet tie palīdz citiem programmētājiem saprast kādi datu tipi tiek sagaidīti un atgriezti.
# ir arī tā sauktie linters, kas pārbauda kodu un brīdina ja tiek izmantoti nepareizi datu tipi.

# kā atgriest vairākas vērtības no funkcijas
def min_max(numbers: list) -> tuple:
    """Atgriež saraksta minimālo un maksimālo vērtību.
    
    Args:
        numbers (list): Saraksts ar skaitļiem.
    Returns:
        tuple: Minimālā un maksimālā vērtība.
    """
    # tipiski ir atgriest kortežu, bet var arī atgriezt sarakstu vai vārdnīcu
    return min(numbers), max(numbers)

my_numbers = [3, 5, 1, 8, 2]
minimum, maximum = min_max(my_numbers) # atpakojam kortežu
print(f"Minimālā vērtība ir {minimum}, maksimālā vērtība ir {maximum}")