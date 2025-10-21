# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa,
# onko se alkuluku. Tässä tehtävässä alkulukuja ovat luvut,
# jotka ovat jaollisia vain ykkösellä ja itsellään.

# Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain
# luvuilla 1 ja 13 siten, että jako menee tasan.
# Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan
# jakaa tasan myös luvulla 3 tai luvulla 7.

luku = int(input("Annatko minulle kokonaisuluvun "))
jakaja = 3

#kerrataan ensin pienet alkuluvut, niin ei tarvitse ottaa niihin kantaa myöhemmin

if (luku == 1 or luku == 2 or luku == 3 or luku == 5 or luku == 7):
    print ("Tiesit jo, tämä on alkuluku")

#kaikki kahdella jaolliset eivät ole alkulukuja, loppuu tähän jos totta

elif luku % 2 == 0:
    print ("Tämä ei ole alkuluku")

#testataan muut luvut
else:
# kun jakaja potenssiin on pienempi kuin luku, ja jakojäännös on nolla kun luku jaetaan jakajalla
# on luku alkuluku. Aloitetaan testi kolmosesta, koska erikoistapaukset käsitelty yllä

    while jakaja*jakaja <= luku:
        if luku % jakaja == 0:
            print("luku ei ole alkuluku")

        else:
            print("tämä on alkuluku")

# lisätään looppiin aina pari lisää, niin testailee kaikki ei parilliset, parilliset
# testattiin jo poislukevasti yllä

        jakaja += 2

        break

# committed

