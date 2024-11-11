from pathlib import Path


print(f"{__name__=}")
print(f"{__file__=}")

tyohakemisto = Path(".")
print("pwd:", tyohakemisto.resolve())

py_tiedosto = Path(__file__)
print("py-tiedoston hakemisto:", py_tiedosto.parent)

txt_tiedosto = Path(__file__).parent / "esimerkki.txt"
print("txt-polku:", txt_tiedosto)

# encoding on lähes pakollinen parametri aina tiedostoja käsiteltäessä!!!
sisalto = txt_tiedosto.read_text(encoding="utf-8")
print(sisalto)
