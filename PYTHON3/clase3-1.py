def cargar():
    mayor=0
    menor=101
    nmayor=""
    nmenor=""
    while True:
        nombre=input("ingresa el nombre\n ")
        nota=int(input("ingrese la nota\n "))
        if nota>mayor:
            mayor=nota
            nmayor=nombre
        if nota<menor:
            menor=nota
            nmenor=nombre
        resp=input("presione espacio para detener")
        if resp==(" "):
            break
    return mayor, menor, nmayor, nmenor


#cuerpo principal
nota_mayor, nota_menor, nombre_mayor, nombre_menor=cargar()
print(f"la nota mayor es {nota_mayor}, y su nombre es {nombre_mayor}")
print(f"la nota menor es {nota_menor}, y su nombre es {nombre_menor}")
