from random import *
with open("a.txt", "w") as archivo:
    for a in range(1,20):
        archivo.write(str(randint(1,100)))
