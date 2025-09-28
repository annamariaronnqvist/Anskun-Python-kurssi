#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi
# niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

tuuma = int(input("anna minulle pituus sentteinä:"))
tuuma_cm = 2.54

while tuuma > 0:
    print ("pituus tuumina on:" f"{tuuma / tuuma_cm:.2f}")
    tuuma = int(input("annapa minulle toinen pituus. Jos haluat lopettaa, anna negatiivinen luku"))


print ("Tuumakaan ei voi olla negatiivinen, kiitos kun käytit minua!")