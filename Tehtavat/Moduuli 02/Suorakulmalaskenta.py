import math

# Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden.
# Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
# Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.


suorakulmakanta_str = input("Ole hyvä ja anna suorakulmiosi kannan pituus kokonaislukuna:")
suorakulmakanta = int(suorakulmakanta_str)

suorakulmakorkeus_str = input("Ole hyvä ja anna suorakulmiosi korkeus kokonaislukuna:")
suorakulmakorkeus = int(suorakulmakorkeus_str)

print("Antamillasi arvoilla, suorakulmiosi piiri on:")
print(suorakulmakorkeus * 2 + suorakulmakanta * 2)
print("Ja suorakulmiosi pinta-ala on:")
print(suorakulmakorkeus * suorakulmakanta)
#tämä pitäisi myös toimia desimaalilla, muuten tämä ohjelma on aika tyhmä