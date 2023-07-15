import matplotlib.pyplot as plt
import csv
from random import *
import random

class Matrizfinal():
    def __init__(self, pil1, pil2, teams, loops,record,estimado,contador):
        self.vueltas = loops
        self.pilotos1 = pil1
        self.pilotos2 = pil2
        self.equipos = teams
        self.record = record
        self.estimado = estimado
        self.cont = contador
    def MatrizResultante(self):
        matriz = [["piloto","equipo"]]

        for i in range(1, int(self.vueltas)+1):
                matriz[0].append(f"L{i}")
        for j in range(1, int(len(self.pilotos1))):
                matriz.append([self.pilotos1[j]])                   #la clase matrizfinal toma los datos de
                matriz.append([self.pilotos2[j]])                   # los pilotos, sus equipos, la cantidad de vueltas, los tiempos record y estimado,
        for c in range(1, int(len(self.equipos))):                  # los ordena y crea un numero aleatorio por la cantidad de vueltas que haya
                self.cont += 1                                      # ademas agregue un contador para ayudarme al colocar los datos de los equipos, ya que se estaban ingresando mal si lo hacia con el "c" del for    
                matriz[self.cont].append(self.equipos[c])
                self.cont += 1
                matriz[self.cont].append(self.equipos[c])
        for l in range(1, len(matriz)):
            for d in range(1,len(matriz[0])-1):
                    if l == 1:
                        f1 = int((float(self.record[l]))*100)
                        f2 = int((float(self.estimado[l]))*100)
                    else:
                        f1 = int((float(self.record[l-1]))*100)
                        f2 = int((float(self.estimado[l-1]))*100)
                    val = randint(f1,f2)
                    val = val/100
                    matriz[l].append(val)
        return matriz

def isfloat(x1):
    try:
        float(x1)               #aqui es donde se comprueban los datos finales de cada carrera y pregunta si son float, si es asi se agrega a la lista
        return True
    except ValueError:
        return False

def Grafica(n_carrera,pista1,pista2,pista3,pista4,pista5,pista6, nombres):
    plt.plot(n_carrera,pista1, label = "hamilton")
    plt.plot(n_carrera,pista2, label = "russell")
    plt.plot(n_carrera,pista3, label = "max")
    plt.plot(n_carrera,pista4, label = "checo")
    plt.plot(n_carrera,pista5, label = "kevin")
    plt.plot(n_carrera,pista6, label = "mick")                              #aqui es donde se crea el grafico

    plt.xlabel("pistas")
    plt.ylabel("tiempo")
    plt.legend(nombres)
    plt.show()

'''
arriba: -clase para crear la matriz de cada archivo
        -funcion para encontrar los ultimos valores(tiempos) de cada competidor
        -funcion para crear la grafica

abajo: -archivos .csv(tracks y equipos)
'''

random.seed(25)
x1 = []
with open("tracks.csv") as archivo:
    reader = csv.reader(archivo, delimiter=",")       
    for row in reader:
        x1.append(row)

shortname = []
km = []
record = []
estimado = []
vueltas = []
for f in range(len(x1)):
    for c in range(len(x1[f])):
        if c == 2:
            shortname.append(x1[f][c])
        elif c == 4:                            #division de los datos del archivo tracks.csv
            km.append(x1[f][c])
        elif c == 6:
            record.append(x1[f][c])
        elif c == 7:
            estimado.append(x1[f][c])
        elif c == 9:
            vueltas.append(x1[f][c])
archivo.close()

c1 = []
with open("equipos.csv") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        c1.append(row)

equipos = []
pilotos1 = []
pilotos2 = []
l = []
for i in range(len(c1)):
    for h in range(len(c1[i])):                 #division de los datos del archivo equipo.csv
        if h == 0:
            equipos.append(c1[i][h])
        elif h == 1:
            pilotos1.append(c1[i][h])
        elif h == 3:
            pilotos2.append(c1[i][h])
f.close()

'''
Matriz resultante
'''

cont = 0
for i in range(1, len(vueltas)):
    res = Matrizfinal(pilotos1, pilotos2, equipos, vueltas[i], record, estimado, cont)      
    var = res.MatrizResultante()
    with open(f"resultado_"+shortname[i]+".csv", "w", newline ="") as file:           #creacion de los archivos
        writer = csv.writer(file)
        writer.writerows(var)
file.close()

l = []
for i in range(1, len(vueltas)):
    with open(f"resultado_"+shortname[i]+".csv") as file:  #abrir archivos finales
        lector = csv.reader(file)
        for row in lector:
            l.append(row)
file.close()

datos_ultima_vuelta = []
for i in range(len(l)):
    if isfloat(l[i][-1]) == True:               #Junta los tiempos finales de cada carrera y competidor
        datos_ultima_vuelta.append(l[i][-1])

hamilton = []
russell = []
Max = []
checo = []
kevin = []
mick = []

for i in range(len(datos_ultima_vuelta)):
    if i == 0 or i == 6 or i == 12 or i ==18 or i == 24:
        hamilton.append(float(datos_ultima_vuelta[i]))
    if i == 1 or i == 7 or i == 13 or i == 19 or i == 25:
        russell.append(float(datos_ultima_vuelta[i]))
    if i == 2 or i == 8 or i == 14 or i == 20 or i == 26:
        Max.append(float(datos_ultima_vuelta[i]))                   #Asigna los tiempos a cada competidor
    if i == 3 or i == 9 or i == 15 or i == 21 or i == 27:
        checo.append(float(datos_ultima_vuelta[i]))
    if i == 4 or i == 10 or i == 16 or i == 22 or i == 28:
        kevin.append(float(datos_ultima_vuelta[i]))
    if i == 5 or i == 11 or i == 17 or i == 23 or i == 29:
        mick.append(float(datos_ultima_vuelta[i]))

sn = []
names = []
for i in range(1,len(shortname)):
    sn.append(shortname[i])
for j in range(1, len(pilotos1+pilotos2)):
    if j < 7:
        names.append(l[j][0])

Grafica(sn, hamilton, russell, Max, checo, kevin, mick, names)