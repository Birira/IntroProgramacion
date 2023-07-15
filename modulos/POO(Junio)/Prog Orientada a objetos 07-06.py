'''
Existen muchos paradigmas de programacion. El que ya conocemos se llama paradigma imperativo.
Dentro de este, estan contenidos otros 3 paradigmas: Estructurado, procedimental y el modular.
'''
'''
El paradigma orientado a objetos basa su funcionamiento en la creacion de **clases**. Una clase
es una abstraccion de la realidad y se utiliza como plantilla que contiene datos o comportamiento.
Una clase se compone de propiedades y metodos. Las propiedades son los datos que almacena y los metodos
son comportamientos son las operaciones que estan asociadas a la clase.

Las clases se basan en la abstraccion, que consiste en una simplificacion de la realidad, tomando solo
aquellos elementos que nos son utiles.

El metodo principal de una clase se le llama constructor. Este metodo es invocado cada vez que se crea
un objeto de la clase.
En POO llamamos objeto a cada correspondiente a una clase. Un objeto es una instacia de una clase.
'''
'''
class persona:
    edad = 18
    nombre = "algo"

#De esta clase, se pueden instanciar diferentes objetos:

jorge = persona()
jorge.edad = 22
jorge.nombre = "Jorge Gonzales"

pedro = persona()
pedro.edad = 88
pedro.nombre = "Pedro Gonzales"

print(jorge.nombre)
print(pedro.nombre)

'''

class Persona:
    def __init__(self, argnombre, argedad):     #Un metodo es una funcion, pero que esta asociada a una clase
        self.nombre = argnombre           #Se accede a las propiedades usando self
        self.edad = argedad              
        print("construido objeto persona")
    
    def saludar(self):
        print(f"Hola mi nombre es {self.nombre} y mi edad es {self.edad}")

juan = Persona("Juan Perez", 48)
print(juan.nombre)
print(juan.edad)
juan.saludar()

#El . hace referencia a una propiedad o metodo de clase

'''
Todos los metodos asociados a una clase, llevan como primer argumento self.
Self hace referencia al objeto desde el cual se esta invocando el metodo(o funcion).
'''