import random
import string

merkkijono = string.ascii_letters + string.digits

salasana = ""

while len(salasana) < 64:
    # lisätään salasanaan uusi satunnainen merkki
    salasana += random.choice(merkkijono)

print(salasana)
print(len(salasana))
