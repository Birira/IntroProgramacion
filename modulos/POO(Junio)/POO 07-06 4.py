'''
Defina la clase Punto(x,y) la cual almacena dos valores los cuales representan su posición en el plano cartesiano. 
Defina los métodos especiales de suma, resta, multiplicación y división, los cuales realizarán operaciones punto 
a punto (es decir, retornarán un nuevo punto en el plano cuya componente x será la suma de las x anteriores)
'''
class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def operacion(self):
        def __add__(self, otro):
            sum = Punto(self.x+otro.x, self.y+otro.y)
            return sum
        def __sub__(self, otro):
            sub = Punto(self.x-otro.x), (self.y-otro.y)
            return sub
        def __mul__(self,otro):
            return Punto(self.x*otro.x, self.y*otro.y)
        def __truediv__(self, otro):
            return Punto(self.x/otro.x, self.y/otro.y)

p1 = Punto(1,1)
p2 = Punto(5,2)
print(p1*p2)