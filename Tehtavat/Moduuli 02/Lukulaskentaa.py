import math

# Kirjoita ohjelma, joka kysyy kolme kokonaislukua.
# Ohjelma tulostaa lukujen summan, tulon ja keskiarvon


ekanumero_str = input("Ole hyvä ja anna kokonaisluku ")
ekanumero = int(ekanumero_str)

tokanumero_str = input("Ole hyvä ja anna toinen kokonaisluku ")
tokanumero = int(tokanumero_str)
kolmasnumero_str = input("Ole hyvä ja anna toinen kokonaisluku ")
kolmasnumero = int(kolmasnumero_str)

print("antamiesi numeroiden summa on:")
print(ekanumero + tokanumero + kolmasnumero)
numerosumma = (ekanumero + tokanumero + kolmasnumero)
print("antamiesi numeroiden tulo on:")
print(ekanumero * tokanumero * kolmasnumero)

print("atamiesi numeroiden keskiarvo on:")
print(f"{numerosumma / 3:.2f}")
# paras olisi, että ohjelma ymmärtää automaattisesti kuinka monta numeroa
# koostaa numerosumman, jokin funktio joka tarkastaa asian osaisi tämän tehdä

##(f"{math.pi:.5f}")