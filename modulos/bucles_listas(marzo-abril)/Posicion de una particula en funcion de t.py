#Posicion de una particula en funcion del tiempo
z2 = 1
while z2 != 0:

    x1 = int(input("Ingrese un valor para tiempo( en segundos): "))
    
    Vi = 10
    print("La velocidad inicial es de ", int(Vi),"m/s")
    Vf = 20
    print("La velocidad final es de ", int(Vf), "m/s")

    a = (Vf - Vi)/x1
    print("La aceleracion es", int(a))

    x2 = Vi * x1 + (a*(x1)**2)/2
    print("La posicion es de ", int(x2))