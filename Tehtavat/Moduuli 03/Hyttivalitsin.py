# Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan
# (LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti. Tehtävässä on käytettävä if/elif/else-toistorakennetta.
# LUX on parvekkeellinen hytti yläkannella.
# A on ikkunallinen hytti autokannen yläpuolella.
# B on ikkunaton hytti autokannen yläpuolella.
# C on ikkunaton hytti autokannen alapuolella.
# Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.

hyttiluokka = input("Haluatko hytin LUX, A, B tai C kuvauksen?")

if hyttiluokka == "A":
    print(f"A hytti on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == "B":
    print("B hytti on ikkunaton hytti autokannen yläpuolella")
elif hyttiluokka == "C":
    print("C hytti on ikkunaton hytti autokannen alapuolella, tämän halvemmaksi ei mene")
elif hyttiluokka == "LUX":
    print("LUX hytti on parasta mitä rahalla saa, se on parvekkeellinen hytti yläkannella")
else:
    print("tarkistatko valintasi, se ei vastaa mitään hyttiluokkaa")