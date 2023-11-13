numero_elementos = int(input())
arreglo = []

print("==========")

for i in range(numero_elementos):
    arreglo.append(int(input()))

print(arreglo)

#---------ORDENAMINETO POR INSERCION---------#

for i in range(numero_elementos):
    pos = i
    aux = arreglo[i]
    
    while pos > 0 and arreglo[i-1] > aux:
        arreglo[pos] = arreglo[pos-1]
        pos-=1
arreglo[pos] = aux

print(arreglo)