import math

# Kirjoita ohjelma, joka kysyy käyttäjältä massan
# keskiaikaisten mittojen mukaan leivisköinä, nauloina
# ja luoteina. Ohjelma muuntaa syötteen täysiksi
# kilogrammoiksi ja grammoiksi
# sekä ilmoittaa tuloksen käyttäjälle.

#Yksi leiviskä on 20 naulaa.
#Yksi naula on 32 luotia.
#Yksi luoti on 13,3 grammaa.
#Esimerkki ohjelman toiminnasta:

luoti_str = input("Ole hyvä ja anna Luodit ")
luoti = float(luoti_str) \
#luotigramma_int = 13

naula_str = input("Ole hyvä ja anna Naulat ")
naula = float(naula_str) \
#naulagramma = 32 * luoti

leiviska_str = input("Ole hyvä ja anna Leiviskät ")
leiviska = float(leiviska_str) \
#leiviskagramma_int = 20 * naula


#luoti = 13
#naula = 32 * luoti
#leiviska = 20 * naula

grammat = (luoti * 13.3) + (naula * (32 * luoti)) + (leiviska * (20 * 32 * 20))

print("Näiden paino on: ")
print((grammat) , "grammaa")
print((grammat / 1000) , "kiloa")

# nyt jo pitkällä, vikaksi pitää tehdä
# näytä kg ja g, eli ensin katsotaan kuinka monta 1000
# menee lukuun ja sitten loput on grammoja
#
# ja jos jaksaa, niin nätiksi :)
#
#print(leiviskaekanumero + tokanumero + kolmasnumero)
#numerosumma = (ekanumero + tokanumero + kolmasnumero)
#print("antamiesi numeroiden tulo on:")
#print(ekanumero * tokanumero * kolmasnumero)

#print("atamiesi numeroiden keskiarvo on:")
#print(f"{numerosumma / 3:.2f}")