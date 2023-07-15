numero = int(input("Ingrese un numero: "))

if numero%2 == 0 and 2 <= numero <= 5:
    print("no es extrano")

elif numero%2 == 0 and  6 <= numero <=20:
    print("Extrano")

elif numero%2 == 0 and numero<20:
    print("No es extrano")

else:
    print("extrano")
