"""2. nodarbība: Būla algebra ar and, or, not."""
ir_lietus = True
ir_lietussargs = False

# 'not' apgriež loģisko vērtību.
print("Līst:", ir_lietus)
print("Nelīst:", not ir_lietus)
ir_lietus = not ir_lietus  # Pārslēdz True <-> False.
print("Pēc pārslēgšanas līst:", ir_lietus)

# 'and' ir True tikai tad, ja abas puses ir True.
print("\nand patiesumtabula:")
print("False and False:", False and False)
print("False and True: ", False and True)
print("True  and False:", True and False)
print("True  and True: ", True and True)

# 'or' ir True, ja vismaz viena puse ir True.
print("\nor patiesumtabula:")
print("False or False:", False or False)
print("False or True: ", False or True)
print("True  or False:", True or False)
print("True  or True: ", True or True)

ir_lietus = True
var_iet_ara = not ir_lietus or ir_lietussargs
print("\nVar iet ārā bez salīšanas?", var_iet_ara)

# Ja ir lietussargs, rezultāts mainās.
ir_lietussargs = True
var_iet_ara = not ir_lietus or ir_lietussargs
print("Ar lietussargu:", var_iet_ara)

# Loģiskos operatorus parasti lietojam kopā ar salīdzinājumiem.
temperatura = 17
print("Patīkams laiks:", 15 <= temperatura <= 25 and not ir_lietus)
