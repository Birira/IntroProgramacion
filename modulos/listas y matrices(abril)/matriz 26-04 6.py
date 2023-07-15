from random import randint

matriz = []
for i in range(5):
    l_aux = []
    for j in range(5):
        l_aux.append(randint(1,1000))
    matriz.append(l_aux)
print(matriz)

num = int(input("Ingrese un numero: "))

existe = False

for n in range(len(matriz)):
    for m in range(len(matriz[n])):
        if matriz[n][m] == num:
            print(f"El numero existe en {n}{m}")
            existe = True

if not existe:
    print("El numero no existe")