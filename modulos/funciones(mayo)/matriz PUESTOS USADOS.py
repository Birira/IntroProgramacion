matriz = [[0,0,0,0,0,0],
          [1,1,1,1,1,0],
          [0,0,0,0,1,0],
          [0,1,0,0,1,0],
          [0,1,0,1,1,0],
          [0,1,0,0,0,0]]

while True: 
    pj = input("Nombre del personaje: ")

    f = int(input("Fila: "))
    c = int(input("columna: "))

    if matriz[f][c] == 1:
        print("No se puede agregar el persona ahi ya que no está disponible")
        f = int(input("ingrese otra posicion de la fila: "))
        f = int(input("ingrese otra posicion de la columna: "))

