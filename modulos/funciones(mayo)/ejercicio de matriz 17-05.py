#dada una matriz de 3 x 3 que representa un tablero del gato, construya una funcion que determine si
# el tablero estas terminado si hay un ganador o si no quedan casillas para jugar

def juego(J1,J2):
    matriz = []

    for i in matriz:
        f = int(input("Ingrese un numero: "))
        c = int(input("Ingrese un numero: "))

        matriz[f-1][c-1] = 0

        for m in matriz:
            print(m)

jugador1 = input("Ingrese el nombre del primer jugador: ")
jugador2 = input("Ingrese el nombre del segundo jugador: ")

rondas = int(input("Ingrese la cantidad de rondas"))

for z in range(rondas*2):
    
    if z % 2 != 0:
        l = (juego(jugador2, jugador1))
    else:
        l = (juego(jugador1, jugador2))



