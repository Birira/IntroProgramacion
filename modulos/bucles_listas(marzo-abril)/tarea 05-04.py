from random import * 

R = randint(1, 100)

for I in range(1, 10):
    U = int(input("Ingrese un numero: "))
    if U > R:
        print("El numero es menor")
    elif U < R:
        print("El numero es mayor")
    elif U == R: 
        print("Correcto, el numero es ", R)
        break

if I == 10:
 print("Fallaste 10 veces")
