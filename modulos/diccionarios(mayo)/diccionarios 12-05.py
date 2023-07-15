#Diccionarios
'''
Un diccionario es una estructura de datos de tipo coleccion que no permite acceso indexado por indice (no
permite acceso secuencial), sino que solo permite acceso por llaves, un diccionario es una manera de almacenar
datos relacionados de tipo llave>valor

un diccionario se declara como dict{} o utilizando {}
En un diccionario los elementos siguen un orden arbitrario

El diccionario almacena los elementos como llave->valor

agenda = {"matias":890080838, "gaspar":989485454, "sebastian":53983985,"Marco":934583795,"llave":"valor"}

print('el telefono de marco es', agenda["Marco"])

if "josele" in agenda:
    print('el telefono de marco es', agenda["josele"])
else:
    print("josele no estan en el diccionario")
'''

diccionario = {} #diccionario vacio

diccionario["llave"] = "valor"
diccionario["matias"] = 890080838
diccionario["Gaspar"] = 989485454

for elem in diccionario:
    print(elem, diccionario[elem])

for key in diccionario.keys:
    print(key, diccionario[key])

for value in diccionario.values:
    print(value, diccionario[value])

for item in diccionario.items:
    print(item, diccionario[item])