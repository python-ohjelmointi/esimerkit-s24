def muunna_kelviniksi(celsiukset: float) -> float:
    return celsiukset + 273.15


# lämpötilat celsius-asteina
mittaukset = [-2.5, 1.1, 7.5, 14.6, 21.0, 19.2]
print("celsiukset:", mittaukset)

# käydään läpi sekä indeksejä, että arvoja samalla kertaa!!!
for i, celsius in enumerate(mittaukset):
    mittaukset[i] = muunna_kelviniksi(celsius)

# nyt listalle halutaan kelvinejä!!!
print("kelvinit:", mittaukset)
