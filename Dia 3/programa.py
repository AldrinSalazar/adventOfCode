x = 0;
y = 0;
xx = 0;
yy = 0;
p = True;
posiciones = ["0x0"]

with open("input1.txt") as archivo:
    for linea in archivo:
        for caracter in linea:
            if caracter == "^":
                if p:
                    y += 1
                else:
                    yy += 1
            elif caracter == "v":
                if p:
                    y -= 1
                else:
                    yy -= 1
            elif caracter == ">":
                if p:
                    x += 1
                else:
                    xx += 1
            elif caracter == "<":
                if p:
                    x -= 1
                else:
                    xx -= 1
            else:
                break
            p = not p
            posiciones.append(str(x)+"x"+str(y))
            posiciones.append(str(xx)+"x"+str(yy))

posiciones = set(posiciones)
print("Casas unicas: "+str(len(posiciones)))
input()
