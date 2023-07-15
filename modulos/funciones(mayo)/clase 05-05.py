"""def lista(x1):
    j = []
    for i in x1:
        j.append((i + ":", (ord(i))))
    return j 
x1 = input("Ingrese un valor: ")

print(lista(x1))"""

print('Porfavor seleccione valores para calcular')
dato1 = input('ingrese el valor 1:' )
dato2 = input('ingrese el valor 2:' )
operador = input('ingrese el operador suma , resta , multiplicacion , division:')

def calculo(dato1,dato2,operador):
    if operador == 'suma':
           print(f"el resultado de la suma es : {int(dato1) + int(dato2)}!")
    elif operador == 'resta':
            print(f"el restultado de la resta es : {int(dato1) - int(dato2)}!")
    elif operador == 'multiplicacion':
            print(f"el restultado de la multiplicacion es : {int(dato1) * int(dato2)}!")
    elif operador == 'division':
            print(f"el restultado de la division es : {int(dato1) / int(dato2)}!")

calculo(dato1, dato2, operador)