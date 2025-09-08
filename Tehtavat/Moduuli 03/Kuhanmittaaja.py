# Kirjoita ohjelma, joka kysyy
# kalastajalta kuhan pituuden senttimetreinä.
# Jos kuha on alamittainen, ohjelma käskee laskea
# kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
# montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
# Kuha on alamittainen, jos sen pituus on alle 37 cm.
import math
kuhanpituus = input("Kerropa sentteinä kuinka pitkän kuhan sait!")
kuhanpituus_int =int(kuhanpituus)
kasvuvara = (37 - kuhanpituus_int)

if kasvuvara <= 0:
    print(f"saitpa hienon kalan, se on parasta uunissa laitettuna!")
else:
    print(f"heitäpä kala takaisin järveen kasvamaan, se on {kasvuvara} senttiä liian lyhyt!")