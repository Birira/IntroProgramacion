import getpass
from os import system
import time

def juego(J1,J2, intento):
        print("Ahora juega propondedor ",J1)

        cd = 0

        l = []

        #p1 = input("Ingrese una palabra: ")
        p1 = getpass.getpass("Ingrese una palabra: ")
        alfabeto = "abcdefghijklmnopqrstuvwxyz"
        
        for i in p1:
            v = i in alfabeto
            if v == False:
                break

        while v == False or len(p1) > 20:
            p1 = getpass.getpass("ingrese una palabra valida(sin numeros, mayusculas o menor a 20 caracteres): ")
            for i in p1:
                v = i in alfabeto
                if v == False:
                    cd += 1
                    break
            
            if cd == 2:
                break

        if cd == 2:
            puntaje = 0
            return puntaje, cd

        else:

            for i in p1:
                l.append(i)

            l2 = []

            for j in range(len(l)):
                l2.append("_")

            print("Ahora juega Adivinador", J2)

            y = intento
            
            contador = 0

            while y != 0:
                sw = 0
                r1 = input("Ingrese una letra: ")

                for x in range(len(l)):
                    if r1 == l[x]:
                        l2[x] = r1
                        sw = 1
                print("La letra esta en:", l2)
                    
                if sw == 0:
                    y = y - 1
                    print("No encontro la letra,te quedan", y, "intentos")
                    print(l2)
                    contador += 1

                if l == l2:
                    print("Ganaste, la palabra era", l2)
                    break

            if y == 0:
                print("Perdiste, la palabra era", l)

            puntaje = (1-contador/intento)*len(p1)
            return puntaje, cd
            #return print("su puntaje es:",puntaje)

system("cls")
print("Bienvenido al juego de adivina-palabra")

jugador1 = input("Ingrese el nombre del primer jugador: ")
jugador2 = input("Ingrese el nombre del segundo jugador: ")

intentos = int(input("Ingrese la cantidad de intentos: "))

rondas = int(input("Ingrese la cantidad de palabras a adivinar: "))

j1 = 0
j2 = 0

l = []

for z in range(rondas*2):
    
    if z % 2 != 0:
        l = (juego(jugador2, jugador1, intentos))
        j1 += l[0]
    else:
        l = (juego(jugador1, jugador2, intentos))
        j2 += l[0]
    
    if l[1] == 2:
        
        break
    time.sleep(5)
    system("cls")
    
if l[1] != 2:
    print(j1,j2)

    if j1 > j2:
        print("Gana",jugador1, "con", j1)
    elif j1 == j2:
        print("empate")
    else:
        print("gana",jugador2, "con", j2)
elif z % 2 != 0:
    print("gana", jugador1, ", porque ingreso mal la palabra",jugador2)
else:
    print("gana", jugador2, ", porque ingreso mal la palabra",jugador1)