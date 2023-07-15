#Tuplas
'''
una tupla es una estructura de datos que nos permite almacenar una secuencia, pero es inmutable.
Su principal uso es que nos permiten almacenar valores que dados su naturaleza deben ir juntos

el tipo de dato tupla se declara como 'tuple' y una vez que ha sido creada, no puede ser modificada

cuando una tupla tiene $2$ elementos hablamos de una 2-tupla. Cuando tiene n elementos hablamos de n-tupla.
'''

'''

tupla1 = ["javier", "gonzales"]

print(tupla1, type(tupla1))


tupla1 = ["nombre", "apellido", "telefono"]

n, a, t = tupla1
print(n,a,t)

def funcion():
    valor = 10 + 20
    valor2 = valor/2
    return valor, valor2

tupla_retorno1 = funcion()
print(tupla_retorno1, type(tupla_retorno1))

valor1, valor2 = funcion
print(valor1, valor2)
'''
l1 = ["sdssdsdsd","fdfdf","34fer"]
l2 = []