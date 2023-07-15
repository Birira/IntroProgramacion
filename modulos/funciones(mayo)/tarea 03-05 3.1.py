def matrizaddfile(m, n = "agenda"):
    with open(f"{n}.txt", "w" ) as archivo:    
        for i in range(len(m)):
            for j in range(len(m[i])):
                archivo.write(str(m[i][j])+ " ")
            archivo.write("\n")
            
matriz = [["nombre", "apellido", 456789022],["matias", "greco", 9856298982],["jose", "canseco", 896298692]]
matriz.append(["Vicente", "Pereira", 4234562345])
nombre = input("Ingrese el nombre del archivo: ")
matrizaddfile(matriz, nombre)