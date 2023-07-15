'''def FiltradorPares(lista):
    pares = []
    for f in lista:
        if f%2 == 0:
            pares.append(f)
    return pares

def FiltradordeImpares(lista):
    impares = []
    for f in lista:
        if f%2 != 0:
            impares.append(f)
    return impares

def SumadeLista(lista):
    sum = 0
    for i in lista:
        sum += int(i)
    return sum

def Serie(y,x):
    for _ in range(y+x):
        t = x+y
        x = y
        y = t
    return t

def Sumador(Z):
    sum = 0
    while Z != 0:
        N = Z % 10
        Z //= 10
        sum += N
    return sum

print(Sumador(Serie(SumadeLista(FiltradorPares([1,4,3,2])),SumadeLista(FiltradordeImpares([1,4,3,2])))))'''

#Parte 2

def sumadiagonal(matriz):
    sum = 0
    cont = 0
    for f in matriz:
        for c in matriz:
            if cont > 4:
                break
            sum += matriz[cont][cont]
            cont += 1
    return sum

def sumadiagonalInversa(matriz):
    sum = 0
    cont = -1
    cont2 = 0
    for f in matriz:
        for c in matriz:
            if cont <-5:
                break
            sum += matriz[cont][cont2]
            cont += -1
            cont2 += 1
    return sum
    
def triangular(matriz):
    var = False
    for f in matriz:
        for c in matriz:
            if matriz[1][0] == 0 and matriz[2][0] == 0 and matriz[3][0] == 0 and matriz[4][0] == 0 and matriz[2][1] == 0 and matriz[3][1] == 0 and matriz[3][2] == 0 and matriz[4][1] == 0 and matriz[4][2] == 0 and matriz[4][3] == 0:
                var = True
    return var

matriz = [[1,4,2,5,6],[0,1,4,8,-1],[0,0,1,4,3],[0,0,0,1,3],[0,0,0,0,1]]

print(triangular(matriz))