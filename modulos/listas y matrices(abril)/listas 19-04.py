#listas

#l3 = ["hola", "chao",3.1415, 9, list()]
#print(l3[-1])

#append(x) nos permite agregar el valor de x al final de la lista

#l_vacia = list()
#l_vacia.append("hola")
#l_vacia.append(1.18)
#print(l_vacia)

#el operador + nos permite concatenar(unir) dos listas
#el * se usa para multiplicar una n cantidad de veces una string
#in se usa para saber si dentro de la lista se encuentra un valor n
#l1 = [1,2,3]
#l2 = [9,8,7]
#l3 = l1 + l2

#print(l3*3)

#print(7 in l3)

#slice y count se aplican de la misma manera [::]
#count(x) sirve para contar cuantas veces(x) aparece en la lista

#l = [1,2,3,9,8,7,4,1,3,10,]
#print(l.count(3))
#print(l.count(5))

#index sirve para retornar el indice de la primera aparicion del elemento x
#l = [1,2,3,9,8,7,4,1,3,10,0]
#print(l.index(3))
#if 4 in l:
#    print(l.index(4))

#remove(x) remueve la primera aparicion del elemento x en la lista

#l = [1,2,3,9,8,7,4,1,3,10,0]
#l.remove(3)
#print(l)

#podemos eliminar un elemento directamente con su indice atraves de "del"

#l = [1 ,2 ,3 ,9 ,8 , 7, 4, 1, 3, 10, 0]
#del l[5]
#print(l)

#lvacia = []
#lvacia.append(10)
#lvacia.append(20)
#lvacia.append("juan")

#print(lvacia)

# como podria insertar el elemento "pedro" al principio de la lista?
#lpedro = ["pedro"]
#lvacia = lpedro + lvacia
#print(lvacia) 

#la funcion insert(index, x) sirve para insertar el elemento x en la posicion index

#l = [1, 2, 3, 9, 8, 7, 1, 2, 3, 9, 8, 7, 1, 2, 3, 9, 8, 7]
#l.insert(3, "juan carlos")
#print(l)

#reverse invierte la lista
#sort ordena la lista en orden alfabetico o en orden numerico