# mēs varam operēt ar vairākiem Booleaniem
# izmantojam tā saukto https://en.wikipedia.org/wiki/Boolean_algebra

# pietiek ar tikai 3 operācijām no tās, negaciju, disjunkciju un conjunkciju (sic)

print("Nav True ->", not True)
print("Nav False ->", not False)

# viens mazs triks ar negāciju ko varam izmantot ir tā sauktā radio poga
# tas ir mainīgais apgriež savu vērtību neatkarīgi vai tā bija True vai False

is_raining = True
print("Līst?", is_raining)
# mēs varam apgriezt šo vērtību
is_raining = not is_raining # atkal darbība notiek no labās puses
print("Līst?", is_raining)
is_raining = not is_raining # atkal darbība notiek no labās puses
print("Līst?", is_raining)
is_raining = not is_raining # atkal darbība notiek no labās puses
print("Līst?", is_raining)
is_raining = not is_raining # atkal darbība notiek no labās puses
print("Līst?", is_raining)

print("*"*40)

# Conjuction abām pusēm jābūt patiešam lai būtu True
print("True un True?", True and True)
print("True un False?", True and False)
print("False un True?", False and True)
print("False un False?", False and False)

# protams mēs neizmanto tiešā veida

is_warm = True
is_raining = True # varēju jau neparsaukt

if is_warm and not is_raining: # no is_warm and not is_raining es iegūsut True vai False
    print("nelīst un ir silts")
    print("tātad peldamies!")
else: # tas else principā pieļauj trīs dažādus gadījumus
    print("vai nu nav silts, vai arī līst, vai arī abi")

# ar Disjunction mums pietiek ar vienu nosacījumu, lai ko izpildītu
print("True vai True?", True or True) # True jo vismaz viens ir patiess
print("True vai False?", True or False) # True jo vismaz viens ir patiess
print("False vai True?", False or True) # True jo vismaz viens ir patiess
print("False vai False?", False or False) # False jo abi Nepatiesi