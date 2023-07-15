from random import *

matriz = []

for i in range(5):
  matriz.append([0]*5)

for f in range(5):
   for c in range(5):
        matriz[f][c] = randint(0,1000)

g = int(input("Ingrese el indice de la fila: "))
k = int(input("Ingrese el indice de la columna: "))
s = input("Ingrese el valor por el cual desea reemplazar: ")
matriz[g][k] = s

print(matriz)