# PYthon ļauj mums pārbaudīt vairākas nosacījumus īsākā sintaksē
temp = 36 
low_temp = 35
high_temp = 37

if low_temp < temp < high_temp: # tas pats kas low_temp < temp and temp < high_temp
    print("Temperaturā normā!")
    print(f"{low_temp} < {temp} < {high_temp}")
else:# tātad vai nu 35 un zemāk temp vai 37 un augstāk
    print(f"Kaut kas nav labi ar jūsu {temp} temperetūru")

# var taisīt arī garākas ķēdītes šadi

a = 5
b = 10

if 0 < a < 7 < b < 500: # tas pats kas 0<a and a<7 and 7<b and b<500
    print("0 < a < 7 < b < 500 ir patiess!")
