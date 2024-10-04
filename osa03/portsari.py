from numeron_kysyminen import kysy_numero

ika = kysy_numero('Syötä ikäsi: ')
onnenluku = kysy_numero('Syötä onnenluku: ')

if ika >= 18:
    print('Tervetuloa kuppilaan 🕺💃')
else:
    print('Ikä ei riitä 👶')

print(f'Onnenlukusi on {onnenluku}')
