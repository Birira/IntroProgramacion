x2 = 1
while x2 != 0:
    x1 = input("Ingrese el codigo de la competencia: ")
    if len(x1) < 10:
        print("El codigo es invalido")
    elif int(x1[8]) == 0 or int(x1[9]) == 0:  
        print("Codigo invalido")
    elif  int(x1[8]) * int(x1[9]) + 10 != len(x1):
        print("codigo invalido")
    else:
        x2 = 0

a = ""

T = ""

com = ""

clavados = ""

a = x1[0:4]

mes = x1[4:6]

dia = x1[6:8]

com = x1[8]

clavados = x1[9]

M = int(mes)
D = int(dia)

print("Año: "+ a + "\n")

if M >= 10 or M <= 4:
    print("Temporada: verano" + "\n")
elif M == 5 and D < 21:
        print("Temporada: Verano" + "\n")   
else:
    print("Temporada: invierno" + "\n")

l = int(com) * int(clavados)
i = 10
F = l + 10
P = 0
Pa = 0
CG = 0

while i < F :
    for x in range(int(clavados)):
        P += int(x1[i])
        i = i +1
    Pt = P/int(clavados)
    P = 0
    if Pt > Pa:
        Pa = Pt
        CG += 1

print("Cantidad de competidores: "+ com + "\n")
print("Cantidad de clavados: "+ clavados + "\n")
print("Gano el competidor: " + str(CG) + "\n")
print("Con promedio: "+ str(Pa) + "\n")