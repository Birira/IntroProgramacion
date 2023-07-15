#Escriba un programa que llene una lista con 10 numeros enteros aleatorios y le pregunte al usuario si 
#está conforme con esos números. Si el usuario no está conforme, deberá generar nuevamente una lista con 10 
#números aleatorios nuevos y volver a preguntarle hasta que el usuario esté conforme. utilice un ciclo while

from random import randint

r = ""
while r != "si":
    x2 = []
    for a in range(10):
        x1 = randint(1,9)
        x2 += str(x1)

    x2.sort()
    x2.reverse()
    print(x2)

    r = input("Esta de acuerdo con los numeros?: ")


