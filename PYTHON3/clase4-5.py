num=0
while True:
    var=int(input("Indica cuantas notas va a procesar del estudiante"))

    for i in range(var):
        nota=float(input("Ingrese la nota {i+1}"))
    
    num=num+1
    
    resp=input("presione espacio para detener")
    if resp==" ":
        break