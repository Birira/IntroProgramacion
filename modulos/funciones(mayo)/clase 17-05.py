def esprimo(num):

    for d in range(2,num):
        if num % d == 0:
            return False
    return True

def primos(lista):
    contador = 0
    for n in lista:
        if esprimo(n):
            contador += 1

    return contador

lista = [1,7,8,5,13]
print(primos(lista))

