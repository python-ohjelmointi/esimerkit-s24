from pathlib import Path

teksti = """Tervetuloa Python-kurssille! Löydät tältä sivustolta tiedot kurssin
tiedotukseen, tukikanaviin, tehtäviin ja muihin aiheisiin liittyen.
Kurssilla hyödynnetään Helsingin yliopiston mooc-kurssin oppimateriaaleja
ja tehtäviä, mutta meillä on mooc-kurssista poikkeavat aikataulut,
käytännön järjestelyt, kokeet sekä arviointikriteerit."""


def tallenna_tiedostoon(tiedostonimi: str, sisalto: str):
    tiedosto = Path(__file__).parent / tiedostonimi

    if tiedosto.exists():
        vastaus = input("Tiedosto on olemassa, ylikirjoitetaanko? (k/e) ")

        if vastaus != "k":
            print("ei tallenneta")
            return

    tiedosto.write_text(sisalto, encoding="utf-8", newline="\n")


if __name__ == '__main__':
    tallenna_tiedostoon("tallennettava.txt", teksti)

    print("🥳")
