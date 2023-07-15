def fibo(x1):
    lista = []
    lista.append(1)
    lista.append(1)
    for i in range(2, x1):
        lista.append(lista[i-1] + lista[i-2])
    return(lista)
    

x1 = int(input("Ingrese un numero: "))
print(fibo(x1))

