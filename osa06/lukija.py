from pathlib import Path


def lue_rivit(tiedoston_nimi: str) -> list[str]:
    tiedosto = Path(__file__).parent / tiedoston_nimi

    try:
        sisalto = tiedosto.read_text(encoding="utf-8")
        return sisalto.splitlines()

    except FileNotFoundError:
        print(f"Tiedostoa {tiedoston_nimi} ei löytynyt")
        return []

    except LookupError:
        print(f"Tiedostossa {tiedoston_nimi} löytyi virheellinen merkki")
        return []


if __name__ == '__main__':
    sanat = lue_rivit("kaikkisanat.txt")
    print(sanat[:50])

    ord = lue_rivit("swe_wordlist.txt")
    print(ord[:50])
