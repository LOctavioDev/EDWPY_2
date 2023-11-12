numero_elementos = int(input())
arreglo = []
aux = 0

print("==========")

for i in range(numero_elementos):
    arreglo.append(int(input()))

print(arreglo)    


# ----------METODO DE BURBUJA----------#

for i in range(numero_elementos - 1):
    for j in range(numero_elementos - 1, 0, -1):
        if arreglo[j] < arreglo[j - 1]:
            arreglo[j], arreglo[j - 1] = arreglo[j - 1], arreglo[j]


print(arreglo)