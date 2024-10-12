def cargar():
    cantidad=0
    aprobado=0
    reprobado=0
    mayor=0
    menor=101
    nmayor=""
    nmenor=""
    suma_notas=0 #acumulador general notas
    suma_aprob=0 #acumulador especifico aprob
    suma_reprob=0 #acumulador especifico reprob

    while True:
        nombre=input("ingresa el nombre\n ")
        nota=int(input("ingrese la nota\n "))
        suma_notas=suma_notas+nota #acumulador general notas
        if nota>79:
            aprobado=aprobado+1
            suma_aprob=suma_aprob+nota #acumulador de notas aprobadas
        else:
            reprobado=reprobado+1
            suma_reprob=suma_reprob+nota #acumulador de notas reprobadas
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
    return mayor, menor, nmayor, nmenor, aprobado, reprobado, suma_aprob, suma_reprob, cantidad, suma_notas

def imprimir (mayor, menor, nmayor, nmenor, aprobado, reprobado, caprob, creprob, cant, totalnota):
    print(f"""
    la nota mayor es {mayor}, y su nombre es {nmayor}
    la nota menor es {menor}, y su nombre es {nmenor}
    la cantidad de estudiantes aprobados es {aprobado}, la cantidad de estudiantes reprobadoes es {reprobado}
    la sumatoria de las notas aprobadas es {caprob}, las reprobadas es {creprob}
    la cantidad de notas que hay es {cant}, y la suma de todas las notas es {totalnota}
""")
#cuerpo principal
nota_mayor, nota_menor, nombre_mayor, nombre_menor, aprobados, reprobados, cant_aprob, cant_reprob, cant_total=cargar()
imprimir(nota_mayor, nota_menor, nombre_mayor, nombre_menor, aprobados, reprobados, cant_aprob, cant_reprob, cant_total)