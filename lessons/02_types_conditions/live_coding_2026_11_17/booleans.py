# jauns datu tips Boolean
# tikai divas vērtības - True vai False
# tātad jā vai nē, 0 vai 1, sarkans vai melns un utt
# Boolean ir mūsu bāzes minimālie informācijas vienības kuras izmantojam programmās
is_cold = True
is_sunny = False
# izdrukāsim izmantojot f-strings
print(f"Vai ir Auksts? {is_cold}")
print(f"Vai saulains? {is_sunny}")
# boolean cold nebūtu tik labs jo nav skaidrs ko nozīme True ,varbūt jā var'but
# is_ uzreiz norāda ka sagaidam boolean nevis teiksim string vai int vai float
# datu tips tātad ir
print(f"Datu tips {is_sunny} ir {type(is_sunny)}")
print(is_sunny)
print(type(is_sunny))

# mēs varam iegūt booleans arī ar kādu darbību piemēram salīdzināšanām
print("2>3", 2>3)
print("2<3", 2<3)
print("2==3", 2==3) # salīdzinam divas vērtības
a = 2
b = 3
print("a vienāds b ?", a == b)
# ir vēl daži citi
# lielāks vai vienāds un otrādi
print("a >= b", a, b, a >= b)
print("a <= b", a, b, a <= b)
# visķepīgākais ir apgrieztais, vai nav vienāds,
print("a nav vienāds ar b?", a != b) # ievērojam izsaukuma zīmi != nozīme parbāudīt vai nav vienāds

# mēs arī varam saglabāt mūsu salidzinājuma rezultātus

alice_age = 20
bob_age = 35
# mēs varam saglabāt salīdzināšanas rezultāti vēlākai apstrādei
is_alice_younger_than_bob = alice_age < bob_age # programmēšanā tipiski darbības apstrāda no labās puses šeit
print(f"Vai Alise ir jaunāka par Bobu? {is_alice_younger_than_bob}")

# vēlak vairāk darbojoties ar stringiem un citiem datu tipiem būs arī citi veidi kā iegūt Boolean
# piemēram varam pārbaudīt vai viens teksts ir citā
print("alus" in "Medalus dzēriens")
print("kefirs" in "Medalus dzēriens")

name = "Valdis"
cits = "Voldemārs"
# cits = "Vol"
# te drusku tricky?
# ko mēs salīdzinam šeit
print(f"Vai {name} ir mazāks par {cits}? Bet kā?")
print(name < cits)

# atbilde pēc leksikografiskā kārtojumu tur "a" ir pirms "o"

# ja gribam garumu tad izmantojam len
print(f"Vai {name} vārda garums mazāks par {cits}? ")
print(len(name) < len(cits))
print(f"{name} ir {len(name)} simbolus garš")
print(f"{cits} ir {len(cits)} simbolus garš")
