from datetime import date

hinta1 = 12.99
hinta2 = 5.99
hinta3 = 10

alv_muutos_pvm = "2024-09-01"
nykyinen_pvm = date.today().isoformat()

alv_prosentti = 24.0

if nykyinen_pvm >= alv_muutos_pvm:
    alv_prosentti = 25.5

alv_kerroin = (100 + alv_prosentti) / 100

valisumma = hinta1 + hinta2 + hinta3
loppusumma = valisumma * alv_kerroin

print(f"Kokonaissumma on {valisumma} €")
print(f"Loppusumma on {round(loppusumma, 2)} (ALV {alv_prosentti} %) €")


ilmainen_toimitus = loppusumma >= 5

if ilmainen_toimitus:
    print('ilmainen toimitus!')
