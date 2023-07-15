while True:
    class Pasajes():
        def __init__(self, nombre, apellido, born, ciudad_o, ciudad_f,fecha,hora):
            self.nombre = nombre
            self.apellido = apellido
            self.born = born
            self.ciudad_or = ciudad_o
            self.ciudad_fin = ciudad_f
            self.fecha = fecha
            self.hora = hora
        def Guardar(self):
            with open("Registro_de_ventas.txt", "a") as file:
                file.write(str([self.nombre, self.apellido, self.born, self.ciudad_or, self.ciudad_fin, self.fecha,self.hora]))
            file.close()
        def GuardarBoleta(self):
            with open("Boleta de "+self.nombre+self.apellido+".txt", "w") as archivo:
                archivo.write(str([self.nombre, self.apellido, self.born, self.ciudad_or, self.ciudad_fin, self.fecha,self.hora]))
            archivo.close()

    def CrearArchivos(lista):
        with open("archivos_de_ciudad.txt", "w") as archivo:
            var = archivo.write(str(lista))
        archivo.close()
        return var

    def Comprobar(ciudad_o, ciudad_f):
        if ciudad_f == ciudad_o or ciudad_f > 6 or ciudad_o > 6:
            return True
        else:
            return False
    def Leer(lista):
        with open("archivos_de_ciudad.txt", "r") as archivo:
            var = archivo.read()
        archivo.close()
        return var

    l = ["Santiago", "Concepcion", "Temuco", "Valdivia", "Osorno", "Puerto Montt"]
    CrearArchivos(l)

    nom = input("Ingrese el nombre del pasajero: ")
    apellido = input("Ingrese el apellido del pasajero: ")
    nacimiento = input("Ingrese la fecha de nacimiento del pasajero: ")

    var = True
    while var == True:
        o = int(input("Ingrese la ciudad de salida pasajero(ingrese numeros del 1 al 6)\n"+ Leer(l)+": "))
        f = int(input("Ingrese la ciudad de destino pasajero(ingrese numeros del 1 al 6)\n" + Leer(l)+": "))
        if Comprobar(o,f) == True:
            print("Datos erroneos")
            var == True
        elif Comprobar(o,f) == False:
            break

    origen = l[o-1]
    final = l[f-1]

    fecha = input("Ingrese la fecha de salida pasajero: ")
    hora = input("Ingrese la hora de salida pasajero: ")
    resultado = Pasajes(nom,apellido,nacimiento,origen,final, hora, fecha)
    resultado.Guardar()
    resultado.GuardarBoleta()
    aux = int(input("Desea ingresar otra boleta? (1 para si 0 para no)\n si desea ver el registro total de pasajes(2)\n si desea ver el ultimo pasaje ingresado(3):"))
    if aux == 0:
        break
    elif aux == 2:
        with open("registro_de_ventas.txt", "r") as archivo:
            boletas = archivo.read()
        print(boletas)
    elif aux == 3:
        with open(f"Boleta de "+nom+apellido+".txt", "r") as archivo:
            boleta = archivo.read()
        print(boleta)