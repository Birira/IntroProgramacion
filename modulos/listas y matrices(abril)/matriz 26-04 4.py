from random import *
matriz = []

for i in range(5):
  matriz.append([0]*5)

for f in range(5):
  for c in range(5):
    matriz[f][c] = randint(0,1000)

for f in range(2):
   for c in range(2):
       s = matriz[f][c]
       for m in range(2):
            for n in range(2):
                if s == matriz[m][n] and (f != m and c != n):
                    matriz[m][n] = randint(0,3)

print(matriz)