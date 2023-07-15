#suma de numeros pares en intervalo

a = int(input("Ingrese el numero a: "))
b = int(input("Ingrese el numero b: "))

suma = 0
for numero in range(a,b):
  if numero % 2 == 0:
    suma += numero
  
print(suma)