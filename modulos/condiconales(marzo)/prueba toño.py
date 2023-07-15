#prueba toño
from random import *
d20 = "d20"
d10 = "d10"
d8 = "d8"
d6 = "d6"
d4 = "d4"

x2 = 1
while x2 != 0:
    x1 = input("Ingrese el dado: ")
    B = int(input("Desea agregar bonificadores?: "))
    
    if x1 == str(d20):
        print(randint(1, 20))  #la variable V puede cambiar, es solo un ejemplo
    elif x1 == str(d10):
        print(randint(1, 10))
    elif x1 == str(d8):
        print(randint(1, 8))
    elif x1 == str(d6):
        print(randint(1, 6))
    elif x1 == str(d4):
        print(randint(1, 4))

    TB = int(x1 + B)
    print(int(TB))