#ordenamiento de la burbuja

l = [5,1,4,2,8]

def burbuja(lista):
    for j in range(len(lista)-2):
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
    print(lista)


burbuja(l)

#x1 = int(input("Ingrese los valores: "))