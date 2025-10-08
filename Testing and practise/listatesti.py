nimet = ["Viiv","Ahmed","Pekka","Olga", "Mary"]
print(nimet[1:3])
#tulostaa aina lopetuspisteestä lasketun edellisen

print(nimet[:3])
#tulostaa alusta kakkoseen asti

print(len(nimet))

names = []
nimi = input("anna eka nimi tai lopeta Enterillä")

while nimi!= "":
    names.append(nimi)
    nimi = input("Anna Seuraava, tai lopeta enterillä")

print(names)

