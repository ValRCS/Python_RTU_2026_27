# mēs varam veikt vienkāršu testēšanu, lai pārliecinātos, ka mūsu funkcijas strādā pareizi
# tam izmantojam assert funkciju, kas pārbauda vai izteiksme ir patiess, ja nav tad tiek izmests kļūdas paziņojums
from my_pakotne.apaksmodulis_a import yell_name, multiply_by_100
from my_pakotne.apaksmodulis_b import power_of_4

assert yell_name("Alice") == "ALICE!!!", "yell_name funkcija nedarbojas pareizi"
assert multiply_by_100(5) == 500, "multiply_by_100 funkcija nedarbojas pareizi"
assert power_of_4(2) == 16, "power_of_4 funkcija nedarbojas pareizi"

# ieliekam ko nepareizu
# assert power_of_4(10) == 100, "power_of_4 funkcija nedarbojas pareizi"
# tātad jābūt pareizam testam, lai pārliecinātos, ka funkcijas strādā pareizi

# ko parasti testē?
# 0, 1 un teiksim -1, un tad teiksmi 10 un -10 un tad ko lielu, kā arī ko mazāku, piemēram 0.1 un -0.1
# ja ir str tad tad arī tukšs str, garš str, str ar speciālajiem simboliem

print("Visas funkcijas strādā pareizi!")