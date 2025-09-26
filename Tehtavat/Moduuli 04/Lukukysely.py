#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

number_given = int(input("Anna minulle kokonaisluku"))

while (number_given > 1 or number_given < 1):
      print("syötä mikä tahansa numero paitsi 1, niin jatkan:")
      number_given = int(input("Anna minulle kokonaisluku"))


print ("Leikki loppui tähän, nyt pitää keksiä miten min ja max käyttäytyy")

#print(min_number and max_number)




