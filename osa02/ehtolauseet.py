kuukausi = 9

if kuukausi >= 4 and kuukausi <= 9:
    print(f"On kesä {kuukausi >= 4 and kuukausi <= 9 = }")

# pieni parannus
if 4 <= kuukausi and kuukausi <= 9:
    print(f"On kesä {4 <= kuukausi and kuukausi <= 9 = }")

# opettajan mielestä paras :)
if 4 <= kuukausi <= 9:
    print(f"On kesä {4 <= kuukausi <= 9 = }")

# Huono ja vaikeasti ymmärrettävä, mutta loogisesti sama
if not (kuukausi < 4 or kuukausi > 9):
    print(f"On kesä {not (kuukausi < 4 or kuukausi > 9) = }")

# Ehto käännettynä toisin päin:

if not (4 <= kuukausi <= 9):
    print("Ei ole kesä")

if kuukausi < 4 or kuukausi > 9:
    print("Ei ole kesä")
