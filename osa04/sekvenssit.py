
def tutki_sekvenssia(data):
    print(data)

    # indeksit alkavat nollasta:
    print("eka:", data[0])

    # katsotaan pituus:
    print("pituus:", len(data))

    # vika saadaan joko pituuden avulla (pituus - 1):
    print("vika (len):", data[len(data) - 1])

    # tai negatiivisella indeksillä:
    print("vika [-1]:", data[-1])

    # osajonoja voidaan ottaa "slice"-operaatiolla:
    print("kolme ekaa:", data[0:3])

    # osajonoista voidaan jättää alku- tai loppu pois:
    print("neljä ekaa:", data[:4])
    print("kuusi vikaa:", data[-6:])

    # in-operaatio:
    print("sisältää o:n:", "o" in data)

    # käydään läpi yksi kerrallaan:
    indeksi = 0  # kasvatetaan tätä yksi kerrallaan luuppissa

    while indeksi < len(data):
        # haetaan arvo:
        arvo = data[indeksi]
        print(indeksi, arvo)
        indeksi += 1


tutki_sekvenssia("Monty Python")

print("\n", "*"*60, "\n")

lista = [1, 3, 5, 7, 9, 42, 100, -5]
tutki_sekvenssia(lista)
