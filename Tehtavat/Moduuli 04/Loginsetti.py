#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on
# syötetty viisi kertaa. Edellisessä tapauksessa tulostetaan Tervetuloa ja
# jälkimmäisessä Pääsy evätty. (Oikea käyttäjätunnus on python ja salasana rules).

#kerrotaan ohjelmalle mikä on oikea tunnus ja salasana
oikeatunnus_str = "python"
oikeasalasana_str = "rules"

#Pyydetään käyttäjältä kirjautumistiedot

print("Pyydän sinulta käyttäjätunnuksen ja salasanan")

tunnus = str(input("Syötä käyttäjätunnuksesi"))
salasana = str(input("Syötä salasanasi"))
count = 0

#seuraavaksi tarkistetaan syöte vasten oikeita tietoja.
#epätosi on kun tunnus ja salasana kummatkin tai jompikumpi ei täsmää

while tunnus != oikeatunnus_str or salasana != oikeasalasana_str:
    if tunnus != oikeatunnus_str:
        print("väärä käyttäjätunnus")
        #pyydetään käyttäjää antamaan tiedot uudelleen
        tunnus = str(input("Syötä käyttäjätunnuksesi"))
        salasana = str(input("Syötä salasanasi"))

    elif salasana != oikeasalasana_str:
        print("väärä salasana")
        # pyydetään käyttäjää antamaan tiedot uudelleen
        tunnus = str(input("Syötä käyttäjätunnuksesi"))
        salasana = str(input("Syötä salasanasi"))
    continue

print("Tervetuloa!")

