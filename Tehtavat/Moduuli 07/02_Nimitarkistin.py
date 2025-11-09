# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes
# käyttäjä syöttää tyhjän merkkijonon. Kunkin nimen syöttämisen jälkeen
# ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
# syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet
# yksi kerrallaan allekkain mielivaltaisessa järjestyksessä. Käytä
# joukkotietorakennetta nimien tallentamiseen.

nimi = input(str("Anna minulle eka nimi: "))
nimilista = []
while nimi != "":
    nimilista.append(nimi)
    nimi = input(str("Anna minulle seuraava nimi: "))

    if nimi == [nimilista]:
        print("Nimi on jo listalla")
    else:
        print("Tämä on uusi nimi")

for nimi in nimilista:
    print (nimi)
