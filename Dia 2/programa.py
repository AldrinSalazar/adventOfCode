def paper(l, w, h):
    minimo = min(l*w, w*h, h*l)
    papel = 2*l*w + 2*w*h + 2*h*l + minimo
    return papel

def lazo(l, w, h):
    volumen = l*w*h
    lista = []
    lista.append(l)
    lista.append(w)
    lista.append(h)
    lista.sort()
    perimetro = 2*(lista[0]+lista[1])
    return volumen+perimetro

total = 0

with open("input1.txt") as archivo:
    for linea in archivo:
        lista = linea.split("x")
        total = total + lazo(int(lista[0]), int(lista[1]), int(lista[2]))

print("Total:"+str(total))
input()
