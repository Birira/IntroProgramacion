x1 = ["Matematicas", "Fisica", "quimica", "lenguaje"]
N = []

for _ in x1:
    x2 = float(input("Ingrese su nota de: "))
    N.append(x2)

print("Las notas ingresadas son: ", N)

sumN = 0

for N in N:
    sumN += N
    P = sumN/4

print("Promedio", P)