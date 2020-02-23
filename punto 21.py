#punto 21
semana = ["lunes", "martes" , "miercoles" ,"jueves" ,"viernes" ,"sabado" ,"domingo"
        ]
print("el nombre debe ponerse en minusculas")
dia = input ("ingrese un dia de la semana: ")
def Sem(dia):
    for i in semana:
        if (1 == semana.count(dia)):
            semana.remove(dia)
    print(semana)
Sem(dia)


    

    

