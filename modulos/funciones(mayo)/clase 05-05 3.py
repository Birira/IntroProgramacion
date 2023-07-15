def divisores(v):
    l = []
    for i in range(1,v):
        if v % i == 0:
            l.append(i)
    return l

x1 = int(input("Ingrese un valor: "))
print(divisores(x1))