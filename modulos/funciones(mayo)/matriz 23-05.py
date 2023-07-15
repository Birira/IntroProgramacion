def juego(p1):
    matriz = [[0,0,0,0,0,0],
            [1,1,1,1,1,0],
            [0,0,0,0,1,0],
            [0,1,0,0,1,0],
            [0,1,0,1,1,0],
            [0,1,0,0,0,0]]
    while True: 
        pj = p1

        f = int(input("Fila: "))
        c = int(input("columna: "))

        matriz[f][c]

        if matriz[f][c] == 0:
            matriz[f][c] = pj[0]
            print(matriz)
        else:
            print("No se puede agregar el persona ahi ya que no está disponible")

        d1 = input("desea agregar otro personaje? ('n', para salir): ")
        if d1 == "n":
            break
        else:
            p1 = input("otro nombre: ")

    return matriz

x1 = input("Nombre del personaje: ")

print(juego(x1))


'''
construir las funciones LoadGame() y SaveGame() las cuales:

SaveGame(matriz): recibe la matriz y la guarda  en un archivo de texto con el mismo formato mostrado.
y loadGame(matriz): carga en la matriz el juego guardado, con sus correspondientes posiciones en 0s y 1s
'''

