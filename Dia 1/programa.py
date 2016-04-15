piso = 0
contador = 1
with open("input1.txt") as archivo:
    for linea in archivo:
        for caracter in linea:
            if caracter == "(":
                piso = piso+1
            elif caracter == ")":
                piso = piso-1
            if piso == -1:
                print("Basement at:"+str(contador))
            contador = contador+1

print(piso)
a = input()
