def multiplos(l, m=2):
    multi = []
    for i in l:
        if i%m == 0:
            multi += str(i)
    return multi

print(multiplos([3,4,5,6,7,8]))
