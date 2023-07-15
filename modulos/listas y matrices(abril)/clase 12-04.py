#strings y listas
#cadena = "hola soy una cadena"

#for a in range(len(cadena)):
#    print(cadena[a])
#for a in range(len(cadena)):   
#    print(cadena[-a-1])

#for letra in cadena:
#   print(letra)

#premio = "Felicitaciones a matias por ser el mejor programador"
#premio = print(premio.replace("matias","Juan").replace("programador","matematico"))
#print(premio)

#print(premio.upper)
#print(premio.lower)
#print(premio.capitalize)
#print(premio.count("e"))

pizza = 2
ingredientes = 3
ingrediente_secreto = "pimienta"

#print(f"usted pidio {pizza} pizza de ingredientes {ingredientes} y el ingrediente secreto es {ingrediente_secreto}")
#print("Usted pidio {} pizzas de {} ingredientes y el ingrediente secreto es{}".format(pizza, ingredientes, ingrediente_secreto))
print("Usted pidio {:1.2f} pizza de {} ingredientes y el ingrediente secreto es {}".format(pizza, ingredientes, ingrediente_secreto))

pizza_comida = 1/3 + 555

print("Usted ha comido {:1.2f} de la pizza".format(pizza_comida))

#print("{:15.5f}".format(0,33))
#print("{:15.5f}".format(1782,21))
#print("{:15.5f}".format(818171,34))

#isalpha chequea que todos los caracteres sean letras(no espacios ni simbolos)
#cadena = "hola soy una cadena"
#print(cadena.isalpha())