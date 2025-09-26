#Kirjoita while-toistorakennetta käyttävä ohjelma, joka
# tulostaa kolmella jaolliset luvut väliltä 1..1000.

number = 1
Max_number = 1000
while number % 3 and number <= 1000:
    print ("kolmella jaollinen:" number)
    number += 1

print ("nyt on kaikki kolmijaolliset tulostettu")
