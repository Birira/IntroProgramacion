from random import *

matriz = []

for i in range(3):
  matriz.append([0]*3)

for f in range(3):
   for c in range(3):
        matriz[f][c] = randint(0,1)

print(matriz)

for f in range(3):
   for c in range(3):
        if matriz[f][c] == 1:
           matriz[f][c] = 0
        else:
            matriz[f][c] = 1

print(matriz)
