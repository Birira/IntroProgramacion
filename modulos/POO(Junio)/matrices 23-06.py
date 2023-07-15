'''def indices(edades,familias,aviones,a,b):
    l = []
    for f in range(len(edades)):
        for c in range(len(edades[f])):
            if f == a and c == b:
                l.append(edades[f][c])
                l.append(familias[f])
                l.append(aviones[c])
    return l

'''
edades_por_familia_y_avion = [[17, 3, 50, 4, 85, 5, 26, 85, 19, 40],
 [66, 45, 55, 65, 8, 97, 39, 33, 89, 62],
 [74, 28, 44, 64, 10, 83, 2, 87, 74, 42],
 [72, 29, 20, 61, 63, 87, 86, 17, 68, 79],
 [79, 8, 18, 68, 31, 88, 21, 64, 96, 64],
 [88, 99, 50, 41, 16, 90, 71, 72, 68, 78],
 [76, 57, 5, 47, 8, 47, 97, 86, 52, 5],
 [77, 78, 9, 40, 29, 79, 25, 44, 66, 88],
 [98, 48, 75, 63, 6, 3, 57, 10, 37, 54],
 [43, 18, 62, 86, 96, 83, 30, 88, 3, 94]]

'''

familia = ["soto", "perez", "abarza", "loyola", "cappuleto", "barbagelata", "valverde", "freire", "lavin", "rozales"]
aviones = ["LAN718", "LAN827", "SKY281", "IBERIA18", "LAN115", "LAN818", "LATAM811", "AIRCANADA181", "EMIRATES171", "SKY17"]

print(indices(edades_por_familia_y_avion, familia, aviones, 5,5))

'''
def mariposa(m):
    l = []
    for _ in range(len(m)):
        l.append([])
    for f in range(len(m)):
        for c in range(1, len(m[f])+1):
            l[f].append(m[-f-1][-c])
    return l

def espejo(m):
    l = []
    for _ in range(len(m)):
        l.append([])
    for f in range(len(m)):
        for c in range(1, len(m[f])+1):
            l[f].append(m[f][-c])
    return l
m =[["a","b","c"],["d","e","f"],["g","h","i"]]

print(mariposa(edades_por_familia_y_avion))
print(espejo(m))

