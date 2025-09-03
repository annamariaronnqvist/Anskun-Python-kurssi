import math
import random

#rnumber = [random.randint(number1, number2) for x in range(times)]

print("Arvotaan seuraavaksi kolminumeroinen koodi (0-6)")
ekakoodi = random.randint(0,6)
tokakoodi = random.randint(0,6)
kolmaskoodi = random.randint(0,6)

print("lukkokoodi alla:")
print(ekakoodi, tokakoodi, kolmaskoodi)

#tähän pitäisi saada jokin looppi, mutta tällä saadaan koodi

print("Arvotaan seuraavaksi nelinumeroinen koodi (1-6)")
nelieka = random.randint(1,6)
nelitoka = random.randint(1,6)
nelikolmas = random.randint(1,6)
nelinelos = random.randint(1,6)

print("lukkokoodi alla:")
print(nelieka, nelitoka, nelikolmas, nelinelos)

#eli jotta tämä olisi nätti, minun tulisi saada tuo random ajamaan itsensä
#uudelleen ja sitten varmistaa, että se arpoo uuden numeron, joka voi olla myös
#sama kuin edellinen.



#Kirjoita ohjelma, joka arpoo ja tulostaa
# kaksi erilaista numerolukon koodia:
#kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
#nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
#Vihje: tutustu random.randint()-funktion käyttöön.

