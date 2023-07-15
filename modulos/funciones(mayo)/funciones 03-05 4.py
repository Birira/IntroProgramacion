from random import *
def encontrar_minimo(l):
    menor = l[0]
    for m in l:
        if menor > m:
            menor = m
    return menor

print(encontrar_minimo([randint(1,1000) for _ in range(10)]))