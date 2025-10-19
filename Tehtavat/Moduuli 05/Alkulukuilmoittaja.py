# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa,
# onko se alkuluku. Tässä tehtävässä alkulukuja ovat luvut,
# jotka ovat jaollisia vain ykkösellä ja itsellään.

# Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain
# luvuilla 1 ja 13 siten, että jako menee tasan.
# Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan
# jakaa tasan myös luvulla 3 tai luvulla 7.

luku = int(input("Anna minulle kokonaisuluku"))

#testaillaan mitä pitää olla totta, jotta ollaan alkuluku
while (luku == 1 or luku == 2 or luku == 3):
    print ("Tiesit jo, tämä on alkuluku")
    break
else:
    while (luku % (1;536870912) == 0):
#or luku % 3 == 0 or luku % 4 == 0):
        print("luku on kokonaisuluku, mutta ei alkuluku")
        break
#mikäli luku on alkuluku, niin sitten tuo looginen testi ei ole totta
    else:
        print("Hiphei, tämähän on alkuluku, ruotsiksi primtal")

#

# seuraavaksi pitää hiffata miten saan tuon alkuluvun tunnistettua kaikkiin suuriin
# lukuihin, pitäsi tehdä lista, jota tuo testi testaa, eli jakojäännös
# kun jaetaan millä tahansa numerolla paitsi yhdellä, pitäisi olla nolla)
# pienemmät luvut toimii, 1-3 poikkeuksena, pikkuhiljaa eteenpäin
