from random import *
#m = []
#for a in range(5):
#    l = []
#    for b in range(5):
#        l.append(randint(0,100))
#    m.append(l)
#print(m)

#m = []

#for x1 in range(3):
    #l = []
    #for x2 in range(3):
    #    num = int(input("Ingrese los numeros para la lista: "))
    #    l.append(num)
    #m.append(l)

#print(m)

m = []

for x1 in range(5):
    l = []
    for x2 in range(5):
        l.append(randint(1,100))
    
m.append(l)

print(l)

columna = int(input("Cuales indices desea reemplazar: "))

v = input("Ingrese el valor que desea reemplazar: ")

h:str = l[columna]

print(h)