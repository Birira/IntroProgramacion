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

def moverse_arriba(r1, x1):
    for f in r1:
        for c in r1:
            if r1[f][c] == x1:
                print("el personaje si esta")

def moverse_derecha(r1, x1):
    for f in range(len(r1)):
        for c in range(len(r1)):
            if r1[f][c] == x1:
                posicion = 
            
                


x1 = input("Nombre del personaje: ")

r1 = juego(x1)

m1 = input("Hacia donde desea moverse: ")

if m1 == "w":
    print(moverse_arriba(r1, x1))
elif m1 == "d":
    print(moverse_derecha(r1, x1))




