# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta
# suuruusjärjestyksessä suurimmasta alkaen. Vihje: listan alkioiden
# lajittelujärjestyksen voi kääntää
# antamalla sort-metodille argumentiksi reverse=True.

#tehdään ensin lista ja pyydetään käyttäjää lisäämään numeroita
lukulista = []
luku = input("anna minulle luku")

#varmistetaan, että käyttäjä pystyy lisäämään lukuja tarpeellisen määrän
while luku!= "":
    lukulista.append(luku)
    #pyydetään lisää lukuja
    luku = input("anna minulle toinen luku, tai jos haluat lopettaa paina enter")
    #järjestellään lista suurimmasta pienimpään
    lukulista.sort(reverse=True)

print(lukulista)
