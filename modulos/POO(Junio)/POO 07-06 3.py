#Metodos especiales
'''
Definen como los objetos de la clase se comportaran frente a situaciones propias del lenguaje, como conversion
de tipo u operadores.
Por ejemplo , para definir como nuestro objeto se comportara al convertirse en str, utilizamos el metodo especial
utilizamos el método especial __str__(), el cual retornará el string que queremos que represente.
Otros métodos especiales definen como nuestro objeto se comportará frente a operadores,
como triangulo1 + triangulo2
'''
class Triangulo:
    def __init__(self, l1,l2,l3):
        self.lado1 = l1
        self.lado2 = l2
        self.lado3 = l3

    def calcularP(self):
        var = 0
        var = self.lado1 + self.lado2 + self.lado3
        return var
    def __str__(self):          #define como se va a comportar cuando se convierta en str
        return f"T({self.lado1},{self.lado2},{self.lado3})"
        
    def __add__(self, otro): # define como se comporta el objeto frente al operador suma +
        return Triangulo(self.lado1 + otro.lado1, self.lado2+otro.lado2, self.lado3 + otro.lado3)

t1 = Triangulo(3,4,5)
print(t1.calcularP())

t2 = Triangulo(6,7,8)
print(t2.calcularP())

print(t1+t2)