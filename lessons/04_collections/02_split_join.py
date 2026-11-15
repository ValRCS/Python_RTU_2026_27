"""4. nodarbība: pāreja no virknes uz sarakstu un atpakaļ."""

text = "Python ir interesanta valoda"
words = text.split()
print("Vārdi:", words)

words[2] = "populāra"
new_text = " ".join(words)
print("Jaunais teikums:", new_text)
print("Sākotnējā virkne nav mainījusies:", text)

colors = "sarkans,zaļš,zils"
color_list = colors.split(",")
print("Ar komatu:", color_list)
print("Ar semikolu:", "; ".join(color_list))

# split() bez argumentiem sadala pēc atstarpēm un citiem whitespace.
# join() ir str metode: atdalītājs ir pa kreisi no .join().
