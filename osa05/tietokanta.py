# tämä ei ole oikea tietokanta, mutta käytetään mielikuvitusta :)
from time import sleep
from functools import lru_cache
from collections import namedtuple

Auto = namedtuple("Auto", ["merkki", "malli", "vuosi", "km", "kulutus", "vari"])

# lru_cache välimuistittaa funktion palauttaman arvon, ja palauttaa sen seuraavalla kerralla ilman, että funktiota suoritetaan.
@lru_cache
def hae_autot() -> list[Auto]:
    sleep(1) # tämä tekee funktiosta hitaan, minkä vuoksi se kannattaa välimuistittaa
    return [
        Auto("Toyota", "Corolla", 2018, 75000, 5.8, "sininen"),
        Auto("Volkswagen", "Golf", 2016, 85000, 6.3, "harmaa"),
        Auto("Ford", "Fiesta", 2017, 67000, 5.6, "valkoinen"),
        Auto("BMW", "3 Series", 2015, 95000, 7.4, "musta"),
        Auto("Audi", "A4", 2019, 54000, 6.2, "punainen"),
        Auto("Mercedes-Benz", "C-Class", 2017, 78000, 6.8, "hopea"),
        Auto("Honda", "Civic", 2020, 32000, 5.4, "sininen"),
        Auto("Mazda", "3", 2016, 90000, 6.1, "punainen"),
        Auto("Nissan", "Qashqai", 2018, 68000, 6.5, "valkoinen"),
        Auto("Hyundai", "i30", 2019, 45000, 6.0, "musta")
    ]


autot = hae_autot()

for auto in autot:
    print(auto[0], auto[1], auto[3], auto[2])
    print(auto.merkki, auto.malli, auto.km, auto.vuosi)
