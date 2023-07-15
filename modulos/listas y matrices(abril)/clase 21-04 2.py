from random import *

l1 = []
l_ordenada = []
for i in range(1,5):
    x1 = randint(0,20)
    l1.append(x1)
    l1.sort()
print(l1)

l_ordenada = (l1[0]-1), (l1[1]-1), (l1[2]-1), (l1[3]-1)

print(l_ordenada)