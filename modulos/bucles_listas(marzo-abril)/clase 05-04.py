#Obtiene el numero capicua
x1 = int(input("ingrese un numero: "))

R = str(x1)
re = ""
while x1 != 0:
    re += str(x1%10)
    x1 = x1//10
if R == re:
    print("El numero es capicua")
else:
    print("El numero no es capicua")
