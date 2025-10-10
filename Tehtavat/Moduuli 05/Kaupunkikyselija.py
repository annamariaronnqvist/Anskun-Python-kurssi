# Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet
# yksi kerrallaan (käytä for-toistorakennetta nimien kysymiseen) ja
# tallentaa ne listarakenteeseen. Lopuksi ohjelma tulostaa kaupunkien
# nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne
# syötettiin. käytä for-toistorakennetta nimien kysymiseen
# ja for/in toistorakennetta niiden läpikäymiseen.

kaupunkilista = []
kaupunki = input("anna eka nimi tai lopeta Enterillä")


while kaupunkilista != "":
    kaupunkilista.append(kaupunki)
    kaupunki = input("anna nyt taas jokin kaupunkinimi nimi tai lopeta Enterillä")
print (kaupunkilista)

#pääsin melkein loppuun.pitää saada loppumaan

