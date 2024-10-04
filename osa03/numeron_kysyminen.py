
def kysy_numero(kysymys):
    """
    Kysyy käyttäjältä numeroa, kunnes saa vastaukseksi positiivisen
    kokonaisluvun, joka palautetaan funktiosta.
    """
    while True:
        vastaus = input(kysymys)

        if vastaus.isdigit():
            return int(vastaus)
