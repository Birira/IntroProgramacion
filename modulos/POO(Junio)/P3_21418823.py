while True:
    def Matriz(m1,m2):
        l = []   
        for i in range(len(m1)):
            l.append([0]*2)
        for i in range(len(m1)):
            for j in range(len(l[i])):
                if j % 2 == 0:
                    l[i][j] = m1[i]
                else:
                    selec = int(input(f"Que nombre desea darle a {m1[i]}, use numeros del 1 al 6 \n, {m2}: "))
                    while m2[selec-1] == "N/A" or selec > 6 or selec < 1:
                        selec = int(input("Ingrese un numero valido para el animal: "))
                    l[i][j] = m2[selec-1]
                    m2[selec-1] = "N/A"      
        return l

    Animal = ["Perro", "Gato", "Gallina", "Oveja", "Vaca", "Cerdo"]
    Nombre = ["Piggy", "Nerón", "Margarita", "Manchitas", "Mimun", "Carlota"]

    res = (Matriz(Animal,Nombre))
    print(res)
    val = ""
    x1 = input("Ingrese el nombre del animal: ")
    for f in range(len(res)):
        for c in range(len(res[f])):
            if x1 == res[f][c]:
                print(f"{res[f][c]}, esta en la posicion: ",f+1,c+1)
                print(f"{res[f][c]} es un(a) {res[f][c-1]}")
            if c != 1 and f > 1:
                if len(res[f-1][1]) > len(res[f][1]):
                    val = res[f-1][0]
                else:
                    val = res[f][0]
    print("Quien tiene el nombre mas largo es el(la) "+ val)
    
    ver = int(input("Desea salir? (1 para si, 0 para no): "))
    if ver == 1:
        break
    
    