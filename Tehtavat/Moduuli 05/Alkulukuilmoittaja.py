# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa,
# onko se alkuluku. Tässä tehtävässä alkulukuja ovat luvut,
# jotka ovat jaollisia vain ykkösellä ja itsellään.

# Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain
# luvuilla 1 ja 13 siten, että jako menee tasan.
# Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan
# jakaa tasan myös luvulla 3 tai luvulla 7.

luku = int(input("Anna minulle kokonaisuluku"))
jakaja = 2

#kerrataan ensin pienet alkuluvut, niin ei tarvitse ottaa niihin kantaa myöhemmin
while (luku == 1 or luku == 2 or luku == 3):
    print ("Tiesit jo, tämä on alkuluku, ja ykkönen on määrittelemätön")
    break
else:

if luku % jakaja == 0:
    print("luku ei ole alkuluku")



#    while luku % jakaja == 0:
#jos jakojäännös on nolla
#        print("luku on kokonaisuluku, mutta ei alkuluku")
#        break

    jakaja = jakaja + 2
    while True (luku % jakaja == 0):
            print("luku on kokonaisuluku, mutta ei alkuluku")
            break

    jakaja = jakaja + 3
    while True(luku % jakaja == 0):
            print("luku on kokonaisuluku, mutta ei alkuluku")
            break

    jakaja = jakaja + 4
    while True(luku % jakaja == 0):
                print("luku on kokonaisuluku, mutta ei alkuluku")
                break

    jakaja = jakaja + 5
    while True(luku % jakaja == 0):
                print("luku on kokonaisuluku, mutta ei alkuluku")
                break

    jakaja = jakaja + 6
    while True(luku % jakaja == 0):
                print("luku on kokonaisuluku, mutta ei alkuluku")
                break

    jakaja = jakaja + 7
    while True(luku % jakaja == 0):
                print("luku on kokonaisuluku, mutta ei alkuluku")
                break

    jakaja = jakaja + 8
    while True(luku % jakaja == 0):
                print("luku on kokonaisuluku, mutta ei alkuluku")
                break

    jakaja = jakaja + 9
    while True(luku % jakaja == 0):
                print("luku on kokonaisuluku, mutta ei alkuluku")
                break

    jakaja = jakaja + 10
    while True(luku % jakaja == 0):
                print("luku on kokonaisuluku, mutta ei alkuluku")
                break

# mikäli jokin jako 2-10 on totta, niin luku ei ole alkuluku, eli jos mikään
# ylläolevista ei ole totta, niin luku on alkuluku

    else:
        print("Hiphei, tämähän on alkuluku, ruotsiksi primtal")

#

# seuraavaksi pitää hiffata miten saan tuon alkuluvun tunnistettua kaikkiin suuriin
# lukuihin, pitäsi tehdä lista, jota tuo testi testaa, eli jakojäännös
# kun jaetaan millä tahansa numerolla paitsi yhdellä, pitäisi olla nolla)
# pienemmät luvut toimii, 1-3 poikkeuksena, pikkuhiljaa eteenpäin
