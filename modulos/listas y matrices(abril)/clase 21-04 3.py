from random import *
l1 = [0]*10

l1[0] = randint(0,99)
l1[1] = randint(0,99)

for x in range(2,len(l1)):
    l1[x] = l1[x-1] + l1[x-2]

print(l1)