# ar moduļiem mēs varam sadalīt kodu vairākās daļās, lai tas būtu pārskatāmāks un vieglāk uzturams
# principā modulis ir tāds pats kā python fails, kurā mēs varam definēt funkcijas, mainīgos un klases
MY_PI = 3.14159
my_people = ["Anna", "Jānis", "Pēteris"]

# visbiežāk modulī mēs definējam funkcijas, kuras tad varam izmantot citos failos
def my_greet_person(name):
    print(f"Sveiks, {name}!")

def my_square(number):
    return number ** 2

# es varu uzreiz izsaukt funkciju, ja es to gribu testēt
# tas var nebūt īsti labs, jo tad šī funkcija tiks izsaukta arī tad, ja es importēšu šo moduli citā failā
# print(f"Kvadrāts no 10 ir {my_square(10)}")

# labāk ir izmantot tā saucamo "if __name__ == '__main__':" konstrukciju, lai izsauktu funkcijas tikai tad, ja modulis tiek izpildīts tieši, nevis importēts
if __name__ == "__main__": # pārbauda vai modulis tiek izpildīts tieši, nevis importēts
    print(f"Kvadrāts no 10 ir {my_square(10)}")