import random
import string

from numeron_kysyminen import kysy_numero

merkkijono = string.ascii_letters + string.digits

pituus = kysy_numero("Anna salasanan pituus: ")
salasana = ""

while len(salasana) < pituus:
    # lisätään salasanaan uusi satunnainen merkki
    salasana += random.choice(merkkijono)

print(salasana)
print(len(salasana))
