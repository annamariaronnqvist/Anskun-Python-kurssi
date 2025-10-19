# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa,
# onko se alkuluku. Tässä tehtävässä alkulukuja ovat luvut,
# jotka ovat jaollisia vain ykkösellä ja itsellään.

# Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain
# luvuilla 1 ja 13 siten, että jako menee tasan.
# Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan
# jakaa tasan myös luvulla 3 tai luvulla 7.

luku = int(input("Annatko minulle kokonaisuluvun "))
jakaja = 2
#True = luku/luku == 1 and luku % jakaja != 0

#kerrataan ensin pienet alkuluvut, niin ei tarvitse ottaa niihin kantaa myöhemmin
if (luku == 1 or luku == 2 or luku == 3):
    print ("Tiesit jo, tämä on alkuluku, ja ykkönen on määrittelemätön")

else:
    while jakaja^2 <= luku and luku % jakaja == 0:
            print("luku ei ole alkuluku")
            jakaja += 1
            break
    else:
        print("tämä on alkuluku")

# seuraavaksi pitää hiffata miten saan tuon alkuluvun tunnistettua > 8
# lukuihin, pitäsi ehkä tehdä lista, jota tuo testi testaa, eli jakojäännös
# kun jaetaan millä tahansa numerolla paitsi yhdellä, pitäisi olla nolla)
# pienemmät luvut toimii, 1-3 poikkeuksena, pikkuhiljaa eteenpäin
# googlen perusteella voisi testailla matemaattisesti tätä myös, mutta pitää
# hiffata ensin se
