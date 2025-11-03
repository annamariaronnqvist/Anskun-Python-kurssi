def tervehdi():
    print("Moi!")
    return

print("onpas kiva päivä, eikö?")
tervehdi()
print("tämän jälkeen on aika siirtyä seuraavaan settiin")

def tervehdi(kerrat):
    for i in range(kerrat):
        print("Hyvää päivää " + str(i+1) + ". kerran")

    return
print ("Päivää alkaa tervehdyksillä.")
#tämä voisi olla myös muuttuja, jota kutsutaan, jota pyydetään käyttäjältä
tervehdi(5)
print("tervehditään lisää")
tervehdi(14)
print("tervehditään lisää")
tervehdi(20)
print("nyt on tervehditty todella monta kertaa!")