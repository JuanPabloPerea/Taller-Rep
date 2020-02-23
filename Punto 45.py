import random
num = []
for i in range (11):
    if (len(num) < 10):
        num.append(random.randint(1,15))
maximo = max (num)
print("la posicion del maximo valor es: "+str(num.index(maximo)))
