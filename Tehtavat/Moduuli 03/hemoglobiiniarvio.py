#Kirjoita ohjelma, joka kysyy käyttäjän biologisen
# sukupuolen ja hemoglobiiniarvon (g/l). Ohjelma ilmoittaa,
# onko hemoglobiiniarvo alhainen, normaali vai korkea.
from selectors import SelectSelector

# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

sukupuoli = input("Kerro sukupuolesi (mies tai nainen)")
h_arvo = input("Mikä on mitattu hemoglobiiniarvosi? (g/l)")
h_arvo_int = int(h_arvo)

#ylä ja ala raja-arvot
matala_h_arvo_nainen = 117
korkea_h_arvo_nainen = 175

matala_h_arvo_mies = 134
korkea_h_arvo_mies = 195

if sukupuoli == "nainen" and h_arvo_int < matala_h_arvo_nainen or sukupuoli == "nainen" and h_arvo_int > korkea_h_arvo_nainen:
    print ("hemoglobiiniarvosi perusteella lisätutkimus on tarpeen, soita 121-1234")

elif sukupuoli == "mies" and h_arvo_int < matala_h_arvo_mies or sukupuoli == "mies" and h_arvo_int > korkea_h_arvo_mies:
    print ("hemoglobiiniarvosi perusteella lisätutkimus on tarpeen, soita 121-1234")

else:
    print("hienoa, hemoglobiiniarvosi on normaali")