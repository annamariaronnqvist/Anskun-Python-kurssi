# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
# hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee
# uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman
# ICAO-koodin ja nimen. Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin
# ja tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa,
# ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten monta
# kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa. (ICAO-koodi on
# lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi
# on EFHK. Löydät koodeja helposti selaimen avulla.)

lentoasema = input(str("Kerropa lentoaseman nimi: "))
lentoasemalista = []
count = 0

while count < 10 and lentoasema != "":
    lentoasemalista.append(lentoasema)
    lentoasema = input(str("Anna toisen lentoaseman nimi: "))
    count +=1
else:
    for lentoasema in lentoasemalista:
        print (lentoasema)

    #aloitettu, nyt pitää rakentaa listaa, hakea olemassa olevaa tietoa ja tehdä jokintietokanta
    # githubista löytyy tämä:
    # https: // github.com / ip2location / ip2location - iata - icao / blob / master / iata - icao.csv