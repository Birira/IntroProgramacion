producto = int(input("Precio de producto: "))
pago = int(input("pago: "))

vuelto = pago-producto

if pago >= producto:
    print("Su vuelto es: ",pago-producto)

if pago < producto:
    print("Su efectivo no es suficiente, porfavor ingrese", producto-pago)


