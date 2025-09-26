# Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa,
# onko annettu vuosi karkausvuosi. Vuosi on karkausvuosi,
# jos se on jaollinen neljällä. Sadalla jaolliset vuodet
# ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.


print("Tällä ohjelmalla tsekataan onko vuosi karkausvuosi!")
vuosi = input("Anna vuosiluku, minä kerron, jos se on karkausvuosi: ")
vuosi_int = int(vuosi)

if vuosi_int % 4 == 0 or vuosi_int % 100 == 0 and vuosi_int % 400 == 0:
    print ("hiphei, löysit karkausvuoden!")
else:
    print ("vuosi on ihan tavallinen vuosi")