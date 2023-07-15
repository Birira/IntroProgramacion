from ast import arg


def sololetras(argumento):
    for caracter in argumento:
        if caracter.isnumeric() == False:
            print(caracter)

sololetras("abc38g6s4w3zgi93mc4d")