from random import *
g = 0
with open("a.txt", "w") as archivo:
    for a in range(0,20):
        archivo.write(str(randint(1,100))+ "\n")

with open("a.txt", "r") as archivo:
    l = archivo.readlines()
    
    for h in l:
        g += int(h)

print(l)

print(g)