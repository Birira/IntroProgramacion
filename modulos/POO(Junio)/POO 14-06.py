'''
El juego consiste en que 2 jugadores lanzan un dado y el valor del dado se
suma al puntaje del jugador.

El juego termina cuando los dos jugadores han realizado 4 lanzamientos del dado o cuando uno de ellos obtiene 18 puntos en 3 lanzamientos

Programe el juego usando clases. Para esto debe implementar las sig, 2 clases:

jugador: Contiene un nombre y su puntaje (el cual parte de 0). Y el metodo lanzar() que producira un aleatorio de 1 a 6
Juego: Contiene el atributo de jugador1 y jugador2 que serán de tipo jugador, una lista con los puntajes obtenidos por
cada jugador, y el turno correspondiente.

La clase juego contiene los siguientes métodos:

str: Muestra los nombres de los jugadores y el puntaje de cada uno de ellos..
iniciar_juego: Inicia el juego con puntajes en cero
jugar(): Ejecuta un juego (invoca al método lanzar del jugador al cual tiene el turno).
Mostrar_rendimiento(): produce un gráfico en matplotlib de todos los lanzamientos de cada uno de los jugadores.
'''
import matplotlib.pyplot as plt
from random import randint

class Jugador():
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntaje = 0
    def __str__(self):
        return f"J1 = {self.nombre} \npuntaje = {self.puntaje}"
    def Lanzar(self):
        return randint(1,6)

class Juego():
    def __init__(self,j1,j2):
        self.j1 = j1
        self.j2 = j2
        self.l = [[],[]]
    def __str__(self):
        return f"J1 = {self.j1.nombre} \nj2 = {self.j2.nombre}"
    def Inicio(self):
        print("empezo")
    def jugar(self):
        self.select = randint(1,2)
        if self.select == 1:
            dado = self.j1.Lanzar()
            self.l[0].append(dado)
            self.select = 2
            self.j1.puntaje += dado
            print (f"Jugador 1 saco un dado de{dado}")
        else:
            dado = self.j2.lanzar()
            self.l[1].append(dado)
            self.turno = 0
            self.j.puntaje += dado
            print (f"Jugador 2 saco un dado de{dado}")
    def juegoTerminado(self):
        pass
    def ganador(self):
        pass
    def Mostrarpuntaje(self):
        pass

 
if __name__ == "__main__":
  gaspar = Jugador("Gaspar")
  pineida = Jugador("Pineida")

  game = Juego(gaspar, pineida)

game.jugar()
