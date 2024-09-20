import random

merkkijono = "abcdefghijklmnopqrstuvwxyzåäö"
#             0123456789              -4321

print(merkkijono)

# indeksit alusta loppuun
print(merkkijono[0])
print(merkkijono[1])
print(merkkijono[2])
print(merkkijono[3])

# indeksit lopusta alkuun
print(merkkijono[-1])
print(merkkijono[-2])
print(merkkijono[-3])

# "muiden kielien" tapa laskea lopusta alkuun päin
vika_indeksi = len(merkkijono) - 1
print(merkkijono[vika_indeksi])
print(merkkijono[len(merkkijono) - 1])

# satunnainen merkki merkkijonosta
# halutaan ottaa satunnainen numero väliltä [0, pituus - 1]
# poimitaan merkkijonosta yksittäinen kirjain saadusta kohdasta
satunnainen = random.randint(0, len(merkkijono) - 1)
print(satunnainen)
print(merkkijono[satunnainen])
