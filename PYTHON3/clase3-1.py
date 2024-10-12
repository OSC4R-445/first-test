def cargar():
    aprobado=0
    reprobado=0
    mayor=0
    menor=101
    nmayor=""
    nmenor=""

    while True:
        nombre=input("ingresa el nombre\n ")
        nota=int(input("ingrese la nota\n "))
        if nota>79:
            aprobado=aprobado+1
        else:
            reprobado=reprobado+1
        if nota>mayor:
            mayor=nota
            nmayor=nombre
        if nota<menor:
            menor=nota
            nmenor=nombre
        resp=input("presione espacio para detener")
        if resp==(" "):
            break
    return mayor, menor, nmayor, nmenor, aprobado, reprobado


#cuerpo principal
nota_mayor, nota_menor, nombre_mayor, nombre_menor, aprobados, reprobados=cargar()
print(f"la nota mayor es {nota_mayor}, y su nombre es {nombre_mayor}")
print(f"la nota menor es {nota_menor}, y su nombre es {nombre_menor}")
print(f"la cantidad de estudiantes aprobados es {aprobados}, la cantidad de reprobados es {reprobados}")