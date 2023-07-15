#escriba un PROCEDIMIENTO que recibe una matriz con numeros y modifique la misma matriz, pero con sus valores
#al cuadrado. Considere que debe cambiar los valores de la misma matriz, no crear una matriz nueva.
'''
def procedimiento(x1):
    for f in range(len(x1)):
        for c in range(len(x1)):
            x1[f][c] = (x1[f][c])**2


matriz = [[1,1,1,1,1],
          [0,0,0,0,0],
          [3,3,3,3,3],
          [0,0,0,0,0],
          [2,2,2,2,2]]

print(matriz)
procedimiento(matriz)
print(matriz)
'''

#Genere un tablero de 9x9 con valores aleatorios entre 1 y 9 y muestre la matriz. 
#Luego, escriba un procedimiento que permita rotar la matriz de 3 formas: 90°, 180° y 270°.
#La función debe funcionar con cualquier tamaño de matriz. Pruebe con una de 3x3 para depurar el codigo.

def rotarM90(x1):
    aux = [[1,2,3],[4,5,6],[7,8,9]]
    for f in range(len(x1)):
        for c in range(len(x1)):
            aux[c][len(x1)-1-f] = x1[f][c]
    print(aux)

def rotarM180(x1):
    aux = [[1,2,3],[4,5,6],[7,8,9]]
    for f in range(len(x1)):
        for c in range(len(x1)):
            aux[len(x1)-1-f][len(x1)-1-c] = x1[f][c]
    print(aux)

def rotarM270(x1):
    aux = [[1,2,3],[4,5,6],[7,8,9]]
    for f in range(len(x1)):
        for c in range(len(x1)):
            aux[len(x1)-1-f][c] = x1[c][f]
    print(aux)
    
matriz1 = [[1,2,3],[4,5,6],[7,8,9]]

print(matriz1)
rotarM90(matriz1)
rotarM180(matriz1)
rotarM270(matriz1)

