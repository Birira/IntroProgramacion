print("Bienvenido a la pizzeria Mama Juana")

x1 = int(input("Ingrese cuantas pizzas desea ordenar: "))

total = 0
suma_ing = 0
if x1 > 0:
    
    for pizza in range(x1):
        st = 1000
        ingredientes = int(input("Ingrese la cantidad de ingredientes: "))
        suma_ing += ingredientes
        print("Menu de ingredientes: \n")
        print("1.-Tomates($300)")
        print("2.-Piña($500)")
        print("3.-Pepperoni($400)")
        print("4.-Aceitunas($600) \n")
        nu_ing = 0
        while nu_ing < ingredientes:
            ing = int(input("Ingrese el ingrediente: "+ str(nu_ing + 1)))
            if ing < 1 or ing > 4:
                print("Error, ingrediente no valido")
            else:
                if ing == 1:
                    st += 300
                elif ing == 2:
                    st += 500
                elif ing == 3:
                    st += 400
                elif ing == 4:
                    st += 600
            nu_ing += 1 
        print("Subtotal", st)
        total += st
    print("Total",total)
    if x1%2==0 and suma_ing%2 == 0:
        print("Tiene 10% de descuento")
        print("Total", total - total/10)
    else:
        print("Total", total)

                

