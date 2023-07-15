#listas tareas 19-04
#Escribir un programa que llene una lista con 8 numeros pedidos por teclado. Luego, muestre el primer y el último elemento de la lista. 
#Utilice un ciclo para pedir los números

x2 = ""
for a in range(8):
    x1 = int(input("Ingrese un numero: "))
    x2 += str(x1)

l1 = str(x2)
print(l1[0], l1[7])