def on_visa(korttinumero: str):
    # visan korttinumerot alkavat aina nelosella
    return korttinumero.startswith('4')


print(on_visa('458912412412478'))
