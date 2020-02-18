bas = 45
alt = 3
def tri(bas,alt):
    sol = (bas*alt)/2
    print (sol)
tri(bas,alt)

Valorp = input("ingrese el valor del producto: ")
Valor = float(Valorp)
def Iva(Valor):
    s = Valor * 0.16
    sol = s+Valor
    print (sol)
Iva(Valor)

numero = input("ingrese un numero: ")
x = float(numero)
def May(x):
    if (x > 100):
        print("el numero es mayor que 100")
    elif (x < 100):
        print("el numero es menor a 100")
    elif (x == 100):
        print("el numero es 100")
May(x)


list = ["lunes", "martes" , "miercoles" ,"jueves" ,"viernes" ,"sabado" ,"domingo"
        ]
dia = input ("ingrese un dia de la semana: ")
def Sem(dia):
    for i in dia:
        print(dia)
print (dia)

    

    

