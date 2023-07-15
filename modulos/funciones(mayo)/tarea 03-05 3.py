def matrizaddfile(m, n = 2):
    with open(f"{n}.txt", "w" ) as archivo:    
        for i in range(3):
            for j in range(3):
                archivo.write(str(m[i][j])+ " ")
            archivo.write("\n")
            
matriz = []

for i in range(3):
    matriz.append([0]*3)
matriz = [["nombre", "apellido", 456789022],["matias", "greco", 9856298982],["jose", "canseco", 896298692]]
nombre = input("Ingrese el nombre del archivo: ")
matrizaddfile(matriz, nombre)

#print(f"El numero existe en {n}{m}")
#matriz[f][c] = int(input("Ingrese un numero para el indice %d, %d: " %(f,c)))