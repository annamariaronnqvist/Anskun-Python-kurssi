# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan
# senttimetreinä sekä pizzan hinnan euroina. Funktio laskee ja palauttaa
# pizzan yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä
# kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa
# paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

#tarvitaan matikkaa, jotta voidaan laskea tuota alaa
import math

#rakennetaan funktio

def rahanvastine(europersquare):

#tehdään paikka, jonne tallentaa halkaisijat ja hinnat
    count = 0
    halkaisijalista = []
    hintalista = []

#pyydetään pari kertaa inputtia pitsojen kooosta ja hinnasta
    while count < 2:
        halkaisija = int(input("Anna pitsan halkaisija: "))
        halkaisijalista.append(halkaisija)
        hinta = int(input("Anna pizzan hinta: "))
        hintalista.append(hinta)
        count += 1
    else:
#pikku testi tässä kohtaa, että mitä numeroita listoihin tuli laitettua
        print (halkaisijalista)
        print (hintalista)

#määritellään suureet, joilla lasketaan ja tehdää vertailu

        hl1 = halkaisijalista[0]
        hl2 = halkaisijalista[1]
        hil1 = hintalista[0]
        hil2 = hintalista[1]

#tehdään laskenta

        vastine1 = (math.pi*hl1**2)/(hil1)
        vastine2 = (math.pi*hl2**2)/(hil2)

#kerrotaan tulos
        if vastine1 > vastine2:
            print ("ensimmäinen pitsa on parempaa vastinetta rahoille")
        else:
            print ("toinen pitsa on parempaa vastinett rahoille")


rahanvastine(0)

#committed