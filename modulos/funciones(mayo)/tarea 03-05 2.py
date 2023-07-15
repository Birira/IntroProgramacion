
def numeros(a):
    aa = int(a)
    l = ""
    re = ""
    while aa != 0:
        re = str(aa%10)
        aa = aa//10
        if int(re)%2 == 0:
            l += re
    with open("pares.txt", "w") as archivo:
        archivo.write(l)

numeros("231313198142329381")
