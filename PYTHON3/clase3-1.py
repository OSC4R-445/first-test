def cargar():
    cantidad=0
    aprobado=0
    reprobado=0
    mayor=0
    menor=101
    nmayor=""
    nmenor=""
    suma_aprob=0
    suma_reprob=0

    while True:
        nombre=input("ingresa el nombre\n ")
        nota=int(input("ingrese la nota\n "))
        if nota>79:
            aprobado=aprobado+1
            suma_aprob=suma_aprob+nota
        else:
            reprobado=reprobado+1
            suma_reprob=suma_reprob+nota
        if nota>mayor:
            mayor=nota
            nmayor=nombre
        if nota<menor:
            menor=nota
            nmenor=nombre
        cantidad=cantidad+1
        resp=input("presione espacio para detener")
        if resp==(" "):
            break
    return mayor, menor, nmayor, nmenor, aprobado, reprobado, suma_aprob, suma_reprob, cantidad

def imprimir (mayor, menor, nmayor, nmenor, aprobado, reprobado, caprob, creprob, cant):
    print(f"""
    la nota mayor es {mayor}, y su nombre es {nmayor}
    la nota menor es {menor}, y su nombre es {nmenor}
    la cantidad de estudiantes aprobados es {aprobado}, la cantidad de estudiantes reprobadoes es {reprobado}
    la sumatoria de las notas aprobadas es {caprob}, las reprobadas es {creprob}
    la cantidad de notas que hay es {cant}
""")
#cuerpo principal
nota_mayor, nota_menor, nombre_mayor, nombre_menor, aprobados, reprobados, cant_aprob, cant_reprob, cant_total=cargar()
imprimir(nota_mayor, nota_menor, nombre_mayor, nombre_menor, aprobados, reprobados, cant_aprob, cant_reprob, cant_total)

#print(f"la nota mayor es {nota_mayor}, y su nombre es {nombre_mayor}")
#print(f"la nota menor es {nota_menor}, y su nombre es {nombre_menor}")
#print(f"la cantidad de estudiantes aprobados es {aprobados}, la cantidad de reprobados es {reprobados}")