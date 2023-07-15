#Multipliacion por suma

x1 = int(input("Ingrese un numero a: "))
x2 = int(input("Ingrese un numero b: "))

M = x1
while x2 != 1:
    x2 = x2 - 1
    x1 = x1 + M

print(x1)
