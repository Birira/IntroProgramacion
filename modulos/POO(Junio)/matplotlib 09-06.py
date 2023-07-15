import matplotlib.pyplot as plt

dias = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]

sueño = [3, 5.5, 4, 7, 8, 9, 9]
hsueno2 = [3,5,7,7,7,8,9]

plt.plot(dias,sueño, label = "Horas de sueno del pepe")
plt.plot(dias,hsueno2, label = "Horas de sueno del tilin")
plt.xlabel("Dias")
plt.ylabel("Horas")
plt.title("Horas de sueno")

plt.legend()
plt.show()