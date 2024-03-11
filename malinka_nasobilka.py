#importujeme knihovnu s funkcema pro náhodné generování čísel
import random 

def nasobeni(a, b):
    vysledek = a * b
    return vysledek

def vyhodnoceni(vysledek, porovnani):
    odpoved = False
    #převedeme funkci porovnani do integeru
    porovnani = int(porovnani)
    if vysledek == porovnani:
        print("No ty jsi ale šikulka, tebe snad vememe taky do Anglie")
        odpoved = True
    else:
        print("Á, chybička se ti vbloudila")
    return odpoved


spravne_odpovedi = 0
spatne_odpovedi = 0

for i in range(10):
    x = random.randint(1,10)
    y = random.randint(1,10)
    #pravý alt + b pro {}
    porovnani = input(f"{x} * {y} = ")
    vysledek = nasobeni(y, x)

    if vyhodnoceni(vysledek, porovnani):
        spravne_odpovedi += 1
    else:
        spatne_odpovedi += 1

    print(f"Správné odpovědi: {spravne_odpovedi}, špatné odpovědi: {spatne_odpovedi}")