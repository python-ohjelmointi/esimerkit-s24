from lukija import lue_rivit

sanat_fi = lue_rivit("kaikkisanat.txt")
print(f"{len(sanat_fi)=}")

sanat_sv = lue_rivit("swe_wordlist.txt")
print(f"{len(sanat_sv)=}")

# kerätään tälle listalle sanat, jotka löytyvät molemmista kielistä
yhteiset: list[str] = []


dict_sv: dict[str, bool] = {}
for sana_sv in sanat_sv:  # m = 410 756 lisäystä
    dict_sv[sana_sv] = True

# käydään suomenkieliset sanat läpi
for sana in sanat_fi:  # n = 93 086 kertaa

    # lisätään listalle, jos löytyy myös ruotsin kielestä
    if sana in dict_sv:  # 1 hakuoperaatio
        yhteiset.append(sana)

print(f"{len(yhteiset)=}")
for sana in yhteiset:
    print(sana)
