# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin
# parametrina saatu lista paitsi että siitä on karsittu pois kaikki
# parittomat luvut. Kirjoita testausta varten pääohjelma, jossa luot
# listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen
# että karsitun listan.

kokonaislukulista = []

#määritellään funktio

def parillinenlukupalauttaja(kokonaislukulista):
    kokonaisluku = int(input("Anna minulle kokonaisuluku, enter lopettaa "))
#annetaan ehdot, lisätään lukuja käyttäjän haluaman mukaisesti

    while kokonaisluku != "":
    #lisäillään listaan käytääjän määrittelemät luvut
        if kokonaisluku % 2 == 0:
            kokonaislukulista.append(kokonaisluku)
            print(sum(kokonaislukulista))
        else:
            kokonaisluku = int(input("Anna minulle kokonaisuluku, enter lopettaa "))

    else:
        print(sum(kokonaislukulista))

    return

parillinenlukupalauttaja(kokonaislukulista)