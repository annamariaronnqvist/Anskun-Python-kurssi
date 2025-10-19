# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa,
# onko se alkuluku. Tässä tehtävässä alkulukuja ovat luvut,
# jotka ovat jaollisia vain ykkösellä ja itsellään.

# Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain
# luvuilla 1 ja 13 siten, että jako menee tasan.
# Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan
# jakaa tasan myös luvulla 3 tai luvulla 7.

lukulista = [2,536870912]
luku = int(input("Anna minulle kokonaisuluku"))
uusi_lukulista = []

for luku in lukulista:
    if luku % lukulista [:] == 0:
        append.uusi_lukulista(luku)
else:
    print("luku on kokonaisuluku")

#list = [2,4,8]
#new_list = [x//2 for x in list]
#print(new_list)

#myList = [10,20,30,40,50,60,70,80,90]
#myInt = 10
#newList = [x / myInt for x in myList]