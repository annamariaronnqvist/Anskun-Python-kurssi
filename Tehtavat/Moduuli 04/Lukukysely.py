#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

number_given = (input("Anna minulle kokonaisluku"))
end_code = "loppu"

while (number_given != end_code):
    print("syötä mikä tahansa numero, niin jatkan:"),
    number_given = (input("Anna minulle kokonaisluku"))
print ("Leikki loppui tähän, nyt pitää keksiä miten min ja max käyttäytyy")
print ("pienin numero oli ", min(number_given))

#print(max(int_number_given), "oli suurin lukusi")
#print(min(int_number_given), "oli pienin lukusi")




