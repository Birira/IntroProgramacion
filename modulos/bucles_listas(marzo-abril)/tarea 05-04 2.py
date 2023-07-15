# Escribe un programa que pida una contraseña y luego pida repetir la misma contraseña. 
# Si el usuario se equivoca en escribir, la contraseña 3 veces. Su cuenta se bloquea y termina el programa. 

C = input("Ingrese una contraseña: ")

I = 1

CC = input("Ingrese nuevamente su contraseña: ")

if C == CC:
    print("Usuario aceptado")

else:
    print("Contrase;a incorrecta, vuelve a intentarlo")
    for I in range(1, 3):
        CC = input("Ingrese la contrase;a nuevamente: ")
        if C == CC:
            print("Usuario aceptado")
            I = 3
            break
        else:
            print("Contrase;a incorrecta, vuelve a intentarlo")

if I == 2:
    print("Usuario bloquedo")
    


