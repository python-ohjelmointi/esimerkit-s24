print("Luetaan tiedosto Pythonilla")

# encoding on lähes pakollinen parametri aina tiedostoja käsiteltäessä!!!
with open("esimerkki.txt", encoding="utf-8") as tiedosto:
    sisalto = tiedosto.read()

    for rivi in sisalto.splitlines():
        print(rivi)
