#Construir la clase triangulo, cuyas propiedades sean el largo de cada uno de los lados, y defina
#un metodo para calcular el perimetro del triangulo (es decir la suma de sus lados)
#Luego instancia dos objetos de tipo triangulo llamados t1 y t2

class Triangulo:
    def __init__(self, l1,l2,l3):
        self.lado1 = l1
        self.lado2 = l2
        self.lado3 = l3

    def calcularP(self):
        var = 0
        var = self.lado1 + self.lado2 + self.lado3
        return var

t1 = Triangulo(3,4,5)
print(t1.calcularP())

t2 = Triangulo(6,7,8)
print(t2.calcularP())

print(t1+t2)