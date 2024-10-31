from postinumerot import postinumerot

smartpostit = []

for numero, nimi in postinumerot.items():
    if nimi == "SMARTPOST":
        smartpostit.append(numero)

print(smartpostit)
print(len(smartpostit))