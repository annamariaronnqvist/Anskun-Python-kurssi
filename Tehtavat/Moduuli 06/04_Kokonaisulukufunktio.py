# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta
# varten pääohjelma, jossa luot listan,
# kutsut funktiota ja tulostat sen palauttaman summan.

kokonaislukulista = []

def lukupalauttaja():
    kokonaisluku = int(input("Anna minulle kokonaisuluku, enter lopettaa "))

    while kokonaisluku != "":
        kokonaislukulista.append(kokonaisluku)
        kokonaisluku = int(input("Anna minulle kokonaisuluku, enter lopettaa "))

    else:
        print(sum(kokonaislukulista))

    return

lukupalauttaja()