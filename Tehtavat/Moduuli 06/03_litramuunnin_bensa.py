#Kirjoita funktio, joka saa parametrinaan bensiinin määrän
# Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan
# litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä
# ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen.
# Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
# Yksi gallona on 3,785 litraa.

bensat = int(input("anna bensamäärä "))
def galloona(bensat):

    while bensat > 0:
        print(f"{bensat * 3.785:.2f}")
        break
    else:
        print("Kiitos kun käytit bensamuunninta")

        return

galloona(bensat)