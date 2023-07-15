#una funcion es una manera de almacenar codigo en una seccion externa del codigo fuente principal
#Para delcarar una funcion utilizamos la palabra "def"
#ejemplo
#escribir una funcion que reciba 2 numeros como argumento y retorne la suma de ellos



''''
def suma(num1, num2):
    print("inicio de la funcion")
    resultado_suma = num1 + num2
    print("retornando el valor")
    return resultado_suma
nv = suma(10,20)
print(nv)    
'''
#la funcion puede no tener un return

def Saludar(nombre):
    print(f"Buenos dias {nombre}")

Saludar(input("Ingrese su nombre: "))