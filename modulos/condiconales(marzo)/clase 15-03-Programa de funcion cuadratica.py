from math import sqrt

a = int(input("Ingrese un valor de a: "))
b = int(input("Ingrese un valor de b: "))
c = int(input("Ingrese un valor de c: "))

x1:int = (-b+sqrt(b**2-(4*a*c)))/(2*a)
x2:int = (-b-sqrt(b**2-(4*a*c)))/(2*a)
print("el resultado de la ecuacion es: ")
print(x1)
print(x2)

#Ejemplos: a=10, b=2, c=6, no tiene solución
# a=-1, b=4, c=-3, tiene solución

#Utilizar 0.5 para raices cuadradas
