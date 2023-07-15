from random import *

R = randint(100, 9999)

RR = R
x1 = 1
while x1 != 0:
    
    if R == 0:
        print("El digito no aparece en el numero")
    
    R = RR
    N = int(input("Ingrese un numero: "))

    if 0 > N or N > 9:
        print("El numero ingresado no es valido")

    while R != 0:
        re = R%10
        R = R//10
        if re == N:
            print("El digito "+ str(N) +" aparece en el numero", RR)
            x1 = 0
            break
        


        


