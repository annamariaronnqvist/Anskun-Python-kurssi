# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa,
# onko se alkuluku. Tässä tehtävässä alkulukuja ovat luvut,
# jotka ovat jaollisia vain ykkösellä ja itsellään.

# Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain
# luvuilla 1 ja 13 siten, että jako menee tasan.
# Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan
# jakaa tasan myös luvulla 3 tai luvulla 7.

import math
luku = int(input("Anna minulle kokonaisuluku" ))
maxluku = math.sqrt(luku)
lukulista = []

testilista = [maxluku]
testilista.append(lukulista)

print(testilista)
print(maxluku)
print(lukulista)

lukulista.append(2)
lukulista.append(3)
lukulista.append(5)
lukulista.append(7)
lukulista.append(9)
lukulista.append(11)
lukulista.append(13)

print(*lukulista)

if lukulista < testilista:
    print("luku on alkuluku")
else:
    print("luku ei ole alkuluku")

#        print("luku ei ole alkuluku")
 #   else:
  #      print("luku on alkuluku")

#for testiluku in lukulista:
#    if luku % lukulista() == 0:
#        print ("luku on alkuluku")

#    else:
#        print ("luku ei ole alkuluku")