def procesar():
    cont=0 #contador especifico para la marca nike
    acum=0 #acumulador especifico de los precios de los zapatos
    while True:
        marca=input("Ingrese la marca a procesar").lower()
        precio=float(input("Ingrese el precio de la marca"))
        if marca=="nike":
            cont=cont+1
            acum=acum+precio
        #controlar el ciclo
        resp=input("Presione espacio para dentener")
        if resp==" ":
            break
    return cont, acum

def promediar(acum, cont):
    if cont>0:
        promedio=acum/cont
    else:
        promedio=0
    return promedio

def calcular(cont, acum):
    prom=promediar(acum,cont)
    return prom

def imprimir(prom_nike):
    print(f"el promedio de precios de zapatos nike es: {prom_nike}")