def agenda_diccionario(nombre):
    x2 = int(input("Ingrese su telefono: "))
    x3 = input("Ingrese su Direccion: ")
    
    diccionario = {"nombre":nombre, "telefono":x2, "direccion":x3}
    
    return diccionario


x1 = input("Ingrese su nombre: ")

print("llamando a",x1, agenda_diccionario(x1))


