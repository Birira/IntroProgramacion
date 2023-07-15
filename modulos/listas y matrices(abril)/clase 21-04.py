from random import *

l1 = []
for i in range(1,21):
    x1 = randint(0,1000)
    l1.append(x1)
    l1.sort()

print(l1)
print("El menor es ", l1[1],"El mayor es", l1[-1])



