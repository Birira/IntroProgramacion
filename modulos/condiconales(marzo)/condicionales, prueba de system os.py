from os import system
from re import X
import time

x=1
while(x != 99):
	time.sleep(5)
	system("cls")
	x = int(input("Ingrese la nota obtenida: "))
	if (x > 7 or x<2) and x != 99  :
		print("Nota invalida")
		time.sleep(5)
		system("cls")
	elif 7 >= x >= 6:
		print("Muy bueno")
	elif 6 > x >= 5:
		print("Bueno")
	elif 4 <= x < 5:
		print("Regular")
	elif 3 <= x < 4:
		print("Malo")
	elif 0< x < 3:
		print("Muy malo")
	elif x == 99 :
		print("Hasta luego")
		break
