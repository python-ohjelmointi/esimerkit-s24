# print('<input type="checkbox" />' * 1_000_000)

"""
# Tavoitteet:

* jokaiselle checkboxille tarvitaan uniikki id (juokseva numerointi)
* checkboxeja ei haluta kerätä muistiin, vaan ne halutaan tulostaa sitä mukaa kun niitä saadaan luotua
"""

i = 0                       # "askeltaja"

print('<html><body>')

# toistetaan aina, kun toistoehto on tosi
while i < 1_000_000:
    print(f'<input id="box-{i}" type="checkbox" />')

    # lopussa pitää muistaa kasvattaa askeltajaa
    i += 1

print('</body></html>')
