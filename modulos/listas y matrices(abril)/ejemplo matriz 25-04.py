s = 0
matriz = []
filas = int(input("Ingrese el numero de sus filas: "))
columnas = int(input("Ingrsese el numero de sus columnas: "))

for i in range(filas):
  matriz.append([0]*columnas)
  #print(matriz)

for f in range(filas):
   for c in range(columnas):
        matriz[f][c] = int(input("Ingrese un numero para el indice %d, %d: " %(f,c)))

print(matriz)
#for f in range(3):
#   for c in range(2):
g = int(input("Ingrese el indice de la fila: "))
k = int(input("Ingrese el indice de la columna: "))
s = matriz[g][k]
print(s)