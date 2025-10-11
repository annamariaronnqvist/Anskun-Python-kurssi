# Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet
# yksi kerrallaan (käytä for-toistorakennetta nimien kysymiseen) ja
# tallentaa ne listarakenteeseen. Lopuksi ohjelma tulostaa kaupunkien
# nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne
# syötettiin. käytä for-toistorakennetta nimien kysymiseen
# ja for/in toistorakennetta niiden läpikäymiseen.

kaupunkilista = []
kaupunki = str(input("anna eka nimi tai lopeta Enterillä"))
count = 1

for kaupunki in kaupunkilista:
    while count < 6:
        kaupunkilista.append(kaupunki)
        count += 1
    kaupunki = input("anna uusi kaupunkinimi")

print("tässä on mainitsemasi viisi kaupunkia: ", kaupunkilista) # "\n")

kaupunkilista = []
kaupunki = input("anna eka nimi tai lopeta Enterillä")

while kaupunki!= "":
    kaupunkilista.append(kaupunki)
    kaupunki = input("anna nyt taas jokin kaupunkinimi nimi tai lopeta Enterillä")

print(kaupunkilista)

#nyt kysytään kaupunkeja, mutta väärällä metodilla.
#pitää saada loppumaan viiden jälkeen ja sitten vielä kolumniksi, hihi