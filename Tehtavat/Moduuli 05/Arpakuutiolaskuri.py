#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
#Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
#Käytä for-toistorakennetta.

import random
kuutioluku = int(input("kuinka monta arpaa haluat"))

# kerrotaan, että tarvitaan jokin luku 1 ja 6 väliltä
kuutiosilmat = [random.randint(1, 6)]
# aloitetaan alusta
count = 1

#annetaan testattava kokonaisuus listan numeroille
for numbers in kuutiosilmat:
    while count < (kuutioluku):
        #rakennetaan listaa
        kuutiosilmat.append(random.randint(1, 6))
        print(kuutiosilmat)
        #lisätään kierroksia, jotta saadaan looppia aikaiseksi
        count = count + 1
    break

print(sum(kuutiosilmat))