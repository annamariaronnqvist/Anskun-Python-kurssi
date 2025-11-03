#Kirjoita funktio, joka saa parametrinaan bensiinin määrän
# Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan
# litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä
# ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen.
# Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
# Yksi gallona on 3,785 litraa.

#pyydetään ensin bensan määrä

bensat = int(input("anna bensamäärä "))

#määritellään funktio ja sen parametri
def galloona(bensat):

#määritellään funktion toiminto ja ehdot
    while bensat > 0:
        print(f"{bensat * 3.785:.2f}")
        bensat = int(input("anna toinen litramäärä "))

    else:
        print("Kiitos kun käytit bensamuunninta")

        return
#ajetaan funktio

galloona(bensat)

#committed