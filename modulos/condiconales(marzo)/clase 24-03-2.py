
numero = int(input("Ingrese un numero: "))

if numero>9999:
    print("El numero no esta en el rango")

if numero>= 1000:
    print(numero//1000)
   # x1 = numero//1000
    #x1 = numero//1000*1000
    numero = numero - numero//1000*1000

if numero>= 100:
    print(numero//100)
    x1 = numero//100
    x1 = x1*100
    numero = numero - x1

if numero>= 10:
    print(numero//10)
    x1 = numero//10
    x1 = x1*10
    numero = numero - x1

print(numero)


 