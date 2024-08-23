# sekä " että ' käyvät merkkijonoissa:
print("terve maailma")
print('hello world')

# monirivinen merkkijono:
print("""
* tomaatti
* porkkana
* kaali""")

teksti = "Tuntien määrä vuodessa on "
tunteja = 365 * 24

# tapa 1: print-funktion pilkku
print(teksti, tunteja, sep='')

# tapa 2: muutetaan luku merkkijonoksi
print(teksti + str(tunteja))

# tapa 3: muotoiltu merkkijono (f-string)
print(f"{teksti}{tunteja}")
