# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta
# varten pääohjelma, jossa luot listan,
# kutsut funktiota ja tulostat sen palauttaman summan.

kokonaislukulista = []

#määritellään funktio

def lukupalauttaja(kokonaislukulista):
    kokonaisluku = int(input("Anna minulle kokonaisuluku, enter lopettaa "))
#annetaan ehdot, lisätään lukuja käyttäjän haluaman mukaisesti

    while kokonaisluku != "":
    #lisäillään listaan käytääjän määrittelemät luvut
        kokonaislukulista.append(kokonaisluku)
    #summataan listan luvut, on nyt kumulatiivinen
        print(sum(kokonaislukulista))
        kokonaisluku = int(input("Anna minulle kokonaisuluku, enter lopettaa "))

    else:
        print(sum(kokonaislukulista))

    return

lukupalauttaja([kokonaislukulista])

#Module 6, tehtävä 4. Funktio lähtee rakentamaan listaa. Sitten feilaa.