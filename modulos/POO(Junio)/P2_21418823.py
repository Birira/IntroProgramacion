from random import *

def Matriz(n,m):
    l = []
    l_str = ""
    for i in range(n):
        l.append([0]*m)

    for i in range(n):
        for j in range(m):
            l[i][j] = randint(0,20)
    
    for i in range(len(l)):
        if i > 0:
            l_str+="\n"
        for j in range(len(l[i])):
            l_str += str(l[i][j])+" "
    with open(f"matriz_{n}_por_{m}.txt", "w") as archivo:
            archivo.write(l_str)
    archivo.close()
    return l_str
def LeerArchivo(x1,x2):
    with open(f"matriz_{x1}_por_{x2}.txt", "r") as file:
        return file.read()

x1 = int(input("Ingrese un valor para N: "))
x2 = int(input("Ingrese un valor para M: "))
print("la matriz es la siguiente: ")
print(Matriz(x1,x2))
print("Fin de la escritura")
print("comenzando lectura del archivo: "+ f"matriz_{x1}_por_{x2}.txt")
print(LeerArchivo(x1,x2))
print("fin de la lectura de archivo: "+ f"matriz_{x1}_por_{x2}.txt")