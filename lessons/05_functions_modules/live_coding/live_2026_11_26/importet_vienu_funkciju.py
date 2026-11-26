#mēs varam arī importēt tikai vienu funkciju no moduļa, nevis visu moduli
from my_pakotne.apaksmodulis_a import yell_name

print(f"Vārds ar lielajiem burtiem: {yell_name('Alice')}")

# šeit gan jāuzmanās, jo ja importēsim vairākas funkcijas ar vienādu nosaukumu, 
# tad tiks izmantota pēdējā importētā funkcija

# jo teorētiski ir iespējams parsaukt arī Python iebūvētās funkcijas, piemēram print() vai input(), bet tas nav ieteicams