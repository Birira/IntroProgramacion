#Maquina de helado

helado = 1000

Fruta = 0
M1 = input("Desea agregar M&M: ")
if M1 == "s":
   helado = helado + 500
elif M1 == "n":
    helado = helado

O1 = input("Desea agregar oreo: ")
if O1 == "s":
    helado = helado + 250

M2 = input("Desea agregar Mantecol: ")
if M2 == "s":
    helado = helado + 190

F1 = input("Desea agregar frutilla: ")
if F1 == "s":
    helado = helado + 320
    Fruta = Fruta + 1

P1 = input("Desea agregar platano: ")
if P1 == "s":
   helado = helado + 200
   Fruta = Fruta + 1

F2 = input("Desea agregar frambuesa: ")
if F2 == "s":
    helado = helado + 430
    Fruta = Fruta + 1

if Fruta >= 2:
    helado = helado-helado*30/100

print("El valor de su helado es de ",helado)