luku = input("Anna luku, tyhjä lopettaa:")

pieni = luku
suuri = luku

while luku != "":
    numero = int(luku)

    #vertaillaan pientä ja suurta"
    if pieni == luku  or numero < pieni:
        pieni = numero

    if suuri == luku or numero > suuri:
        suuri = numero

    luku = input("Anna luku, tyhjä lopettaa:")

print (f"pienin luku on {pieni}")
print (f"suurin luku on {suuri}")
