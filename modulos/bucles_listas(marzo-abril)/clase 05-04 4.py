#El digito aparece una x cantidad de veces en un numero

from random import *

R = randint(10, 999999)

RR = R
x1 = 1
print(R)
while x1 != 0:
    
    if R == 0:
        print("El digito no aparece en el numero")
    
    R = RR
    N = int(input("Ingrese un numero: "))

    if 0 > N or N > 9:
        print("El numero ingresado no es valido")
    cont = 0
    while R != 0:
        re = R%10
        R = R//10
        if re == N:  
            x1 = 0
            cont = cont + 1

print("El digito "+ str(N) +" aparece en el numero", RR, cont, "veces")
            