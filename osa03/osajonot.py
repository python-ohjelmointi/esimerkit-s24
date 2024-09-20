# Testitunnus, ei oikea henkilö (https://www.tuomas.salste.net/doc/tunnus/henkilotunnus.html)
tunnus = "311299-9872"
#         0123456789

paiva = int(tunnus[:2])
kk = int(tunnus[2:4])
vuosi = int(tunnus[4:6])
valimerkki = tunnus[6]
yksilo = int(tunnus[7:10])

if valimerkki == '-':
    vuosi = 1900 + vuosi
elif valimerkki == '+':
    vuosi = 1800 + vuosi
elif valimerkki == 'A':
    vuosi = 2000 + vuosi

print(f"""
{paiva=}
{kk=}
{vuosi=}
{valimerkki=}
{yksilo=}
""")

if yksilo % 2 == 0:
    print('nainen')
else:
    print('mies')
