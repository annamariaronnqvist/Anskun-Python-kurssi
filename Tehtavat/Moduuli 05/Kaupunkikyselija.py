# Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet
# yksi kerrallaan (käytä for-toistorakennetta nimien kysymiseen) ja
# tallentaa ne listarakenteeseen. Lopuksi ohjelma tulostaa kaupunkien
# nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne
# syötettiin. käytä for-toistorakennetta nimien kysymiseen
# ja for/in toistorakennetta niiden läpikäymiseen.

kaupunkilista = []
kaupunki = (input("anna eka kaupunkinimi, kerään niitä viisi "))

kaupunkilista.append(kaupunki)
for kaupunki in range(4):
        kaupunki = input("anna uusi kaupunkinimi ")
        kaupunkilista.append(kaupunki)
for kaupunki in kaupunkilista:
    print(kaupunki)

#committed



#kokeilin tähtihommaa, mutta ei toiminut: print ("tässä on lista kaupungeista:", *(kaupunkilista))

#eka ohjelma alla. ei toimi niinkuin pitää
#kaupunkilista = []
#kaupunki = input("anna eka nimi tai lopeta Enterillä")

#while kaupunki!= "":
#    kaupunkilista.append(kaupunki)
#    kaupunki = input("anna nyt taas jokin kaupunkinimi nimi tai lopeta Enterillä")

#print(kaupunkilista)

#nyt kysytään kaupunkeja, mutta väärällä metodilla.
#pitää saada loppumaan viiden jälkeen ja sitten vielä kolumniksi, hihi