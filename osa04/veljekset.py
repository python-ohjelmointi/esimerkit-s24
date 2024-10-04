def tulosta_akkosjarjestyksessa(nimet):
    # ei muuta alkuperäistä, vaan luo järjestetyn kopion:
    jarjestetty = sorted(nimet)
    yhdistetty = ", ".join(jarjestetty)

    print(yhdistetty)


sisarukset = ["Aino", "Eero", "Sofia", "Lauri", "Emma",
              "Ville", "Linnea", "Juhani"]

tulosta_akkosjarjestyksessa(sisarukset)

print(sisarukset)

sisarukset.insert(2, "Veera")
sisarukset.append("Elias")

tulosta_akkosjarjestyksessa(sisarukset)

vanhin = sisarukset[0]  # Aino (?)
kuopus = sisarukset[-1]  # Elias (?)

print("\n", "*"*30, "\n")

print(sisarukset)
print(f'{vanhin=}')
print(f'{kuopus=}')
