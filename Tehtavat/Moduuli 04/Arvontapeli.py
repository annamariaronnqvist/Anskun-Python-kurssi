#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus,
# Liian pieni arvaus tai Oikein. Huomaa, että tietokone ei saa vaihtaa
# lukuaan arvauskertojen välissä.

import random

print("Tässä pelissä sinun pitää arvailla minulta lukuja väliltä 1..10")
arvottuluku = random.randint(1,10)
arvausluku = int(input("Arvaa mikä luku on mielessäni?"))

#seuraavassa kohdassa peli alkaa, tosi on kun arvottu ja arvaus ovat samat
#kerrotaan mitä tapahtuu kun arvaus ja arvottu eivät kohtaa

while arvausluku != arvottuluku:
    if arvausluku > arvottuluku:
        print("Liian suuri arvaus - arvaa uudelleen")
        #pyydetään käyttäjää antamaan toinen arvaus
        arvausluku = int(input("Arvaapa uudelleen, mikä luku on mielessäni?"))

    elif arvausluku < arvottuluku:
        print("Liian pieni arvaus - arvaa uudelleen")
        # pyydetään käyttäjää antamaan toinen arvaus
        arvausluku = int(input("Arvaapa uudelleen, mikä luku on mielessäni?"))
        # varmistetaan, ettei mene ikuiseen looppiin
        continue
#nyt ohjelma toimii

print ("Oikein - hienoa, arvasit vihdoin, luku on todellakin:", arvottuluku)

print ("Kiitos kun pelasit!")
