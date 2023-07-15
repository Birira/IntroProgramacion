#Clase 17-03
#Dado el monto de una compra y el monto pagado, 
#los cuales ingresados por el usuario, calcule el vuelto
#y muestrelo por pantalla

compra = int(input("Ingrese el precio de la compra: "))
pago = int(input("Ingrese su pago: "))

vuelto = pago-compra

print("El vuelto es de "+ str(vuelto))

if pago < compra:
    print("Su pago es insuficiente")

if pago >= compra:

 M500 = (vuelto//500)
 print("Monedas de 500:", M500)
 vuelto = vuelto-500*M500 

if vuelto >= 100:
    M100 = (vuelto//100)
    print("Monedas de 100:", M100)
    vuelto = vuelto-100*M100

if vuelto >= 50:
 M50 = (vuelto//50)
 print("Monedas de 50:", M50)
 vuelto = vuelto-50*M50

if vuelto >= 10:
 M10 = (vuelto//10)
 print("Monedas de 10:", M10)
 vuelto = vuelto-10*M10

print("El ajuste de sencillo es:", vuelto)

 