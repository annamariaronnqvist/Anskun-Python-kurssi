# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan
# satunnaisen nopan silmäluvun väliltä 1..6. Kirjoita pääohjelma,
# joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan
# nopan tahkojen yhteismäärän. Muokatun funktion avulla voit heitellä
# esimerkiksi 21-tahkoista roolipelinoppaa. Edellisestä tehtävästä
# poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan
# maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

silmaluku = random.randint(1,6)


def arvanheitto():
    print("arvotaan lukuja kunnes saadaan kuutonen")
    print(silmaluku)

    return

arpaheitto = 0

while silmaluku != 6:
    silmaluku = random.randint(1, 6)
    arpaheitto += 1
    print(f"Arvonta {arpaheitto}: {silmaluku}")

else:
    print("nyt loppui kun tuli kutonen")

arvanheitto()