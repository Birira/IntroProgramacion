#Ficha de proteccion social
x1 = int(input("Ingrese el numero de habitantes de su hogar: "))
x2 = int(input("Ingrese el ingreso total del hogar: "))
x3 = int(input("ingrese el total de personas de la tercera edad: "))

z1 = x2/x1

if x3 == 0:
    if x1 <= 4:
        if z1 <= 60000:
            print("Su nivel socio economico es C3", int(z1))
        elif 60000 < z1 and z1 <= 100000:
            print("Su nivel socio economico es C2", int(z1))
        elif 100000 < z1 and z1 <=300000:
            print("Su nivel socio economico es C1", int(z1))
        elif z1 > 300000:
            print("Su nivel socio economico es AB", int(z1))
        
    else:
        if z1 <= 40000:
            print("Su nivel socio economico es C3", int(z1))
        elif 40000 < z1 and z1 <= 80000:
            print("Su nivel socio economico es C2", int(z1))
        elif 80000 < z1 and z1 <=250000:
            print("Su nivel socio economico es C1", int(z1))
        elif z1 > 250000:
            print("Su nivel socio economico es AB", int(z1))

else:
    print("Su nivel socio economico es C3", int(z1))


