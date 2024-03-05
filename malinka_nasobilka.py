import random #importujeme knihovnu s funkcema pro náhodné generování čísel


def nasobeni(a, b):
    vysledek = a * b
    return vysledek

#v odpovedi chyba
def vyhodnoceni(vysledek, porovnani):
    odpoved = False
    if vysledek == porovnani:
        print("No ty jsi ale šikulka, tebe snad vememe taky do Anglie")
        odpoved = True
    else:
        print("Á, chybička se vbloudila")
    return odpoved
   
for i in range(9):
    x = random.randint(1,10)
    y = random.randint(1,10)
    #pravý alt + bn pro {}
    porovnani = input(f"{x} * {y} = ")
    vysledek = nasobeni(y, x)
    vyhodnoceni(vysledek, porovnani)