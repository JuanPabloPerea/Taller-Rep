import random
sumatoria = 0
fila = 3
columna = 10
matriz = []
for i in range(3):
    matriz.append([])
    if (i == 0):
        for j in range (columna):
            numero = random.randint(1,20)
            matriz[i].append(numero)
    if (i == 1):
        for j in range (columna):
            numero = matriz[0][j]**2
            matriz[i].append(numero)
    if (i == 2):
        for j in range (columna):
            numero = matriz[0][j]+matriz[1][j]
            matriz[i].append(numero)
for i in range(fila):
    for j in range(columna):
        print("%d " % (matriz[i][j]), end = "")
    print("")
