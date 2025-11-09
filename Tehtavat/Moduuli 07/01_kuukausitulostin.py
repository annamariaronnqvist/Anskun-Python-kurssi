# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen
# ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina
# monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden
# mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.
from selectors import SelectSelector

vuodenajat = ("kevät", "kesä", "syksy", "talvi")
kuukausi = int(input("Anna kuukauden numero 1-12, kerron sinulle mihin vuodenaikaan se kuuluu."))

kevat = ("3", "4", "5")
kesa = ("6", "7", "8")
syksy = ("9", "10", "11")
talvi = ("12", "1", "2")

if kuukausi >=3 and kuukausi <=5:
    print(f"{kuukausi}. kuukausi on {kevat}.")
if kuukausi >=6 and kuukausi <=8:
    print(f"{kuukausi}. kuukausi on {kesa}.")
if kuukausi >=9 and kuukausi <=11:
    print(f"{kuukausi}. kuukausi on {syksy}.")
if kuukausi == 12 or kuukausi ==1 or kuukausi == 2:
    print(f"{kuukausi}. kuukausi on {talvi}.")

print(f"{kuukausi}. kuukausi on {vuodenajat}.")

#ihanasti tulostelee numerot ja kaikki kuukaudet :)

#for kuukausi = kevat:
 #   print ("Tämä on kevätkuukausi!")
  #  for kuukausi = kesa:
   #     print ("Tämä on kesäkuukausi!")
    #for kuukausi = syksy:
     #   print ("Tämä on syyskuukausi!")
    #for kuukausi = talvi:
     #   print ("Tämä on talvikuukausi")

    #else:
     #   print ("Tämä ei ole mikään kuukausi")

