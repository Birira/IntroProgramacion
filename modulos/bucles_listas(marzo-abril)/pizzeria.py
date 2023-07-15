#pizzeria

pizza= 1000

print("Bienvenido a la pizzeria Mama Juana")

x1 = int(input("Ingrese cuantas pizzas desea ordenar: "))

d1 = x1%2

for i in range(x1):
    

    x2 = int(input("Ingrese la cantidad de ingredientes: "))

    while x2 > 0:
        
        if x2 > 0:
            print("Menu de ingredientes: \n")
            print("1.-Tomates($300)")
            print("2.-Piña($500)")
            print("3.-Pepperoni($400)")
            print("4.-Aceitunas($600) \n")
        
        x3 = int(input("Ingrese el ingrediente que desea llevar: "))

        
        if x3 <= 4:
            
            if x3 == 1:
                    pizza = pizza + 300
                
                    print("subtotal:",pizza)
            elif x3 == 2:
                    pizza = pizza + 500
                    
                    print("subtotal:",pizza) 
            elif x3 == 3:
                    pizza = pizza + 400
                    
                    print("subtotal:",pizza)
            elif x3 == 4:
                    pizza = pizza + 600
                    
                    print("subtotal:",pizza)
            pizza += pizza
            x2 = x2-1

        print("total a pagar", pizza)
                
if d1 == 0:
    print("¡Tiene un 10% de descuento!")
    print(pizza - pizza/10)
        