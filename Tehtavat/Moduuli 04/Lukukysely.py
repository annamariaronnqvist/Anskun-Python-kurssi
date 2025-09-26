#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

number_given = int(input("Anna minulle kokonaisluku"))
#max_number_str = str(max(number_given))
#min_number_str = str(min(number_given))

while (number_given > 1 or number_given < 1):
      print("syötä mikä tahansa numero paitsi 1, niin jatkan:")
      number_given = int(input("Anna minulle kokonaisluku"))


#print ("suurin luku oli: 10")
#, "pienin luku oli:" min_str)

print ("Leikki loppui tähän, nyt pitää keksiä miten min ja max käyttäytyy")

#print(min_number and max_number)




