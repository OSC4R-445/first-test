def procesar():
    cont_nike=0 #contador especifico para la marca nike
    acum_nike=0 #acumulador especifico de los precios de los zapatos
    cont_adidas=0
    acum_adidas=0
    while True:
        marca=input("Ingrese la marca a procesar").lower()
        precio=float(input("Ingrese el precio de la marca"))
        if marca=="nike":
            cont_nike=cont_nike+1
            acum_nike=acum_nike+precio
        if marca=="adidas":
            cont_adidas=cont_adidas+1
            acum_adidas=acum_adidas+precio
        #controlar el ciclo
        resp=input("Presione espacio para dentener")
        if resp==" ":
            break
    return cont_nike, acum_nike,acum_adidas, acum_adidas

#modulo para calcular promedios
def promediar(acum, cont):
    if cont>0:
        promedio=acum/cont
    else:
        promedio=0
    return promedio

#modulo para calcular porcentajes
def porcentaje(total_zapatos, cont2):
    porc=cont2/(cont1*100)
    return porc

#calculador de nike
def calcular_n(cont_nike, acum_nike):
    prom_nike=promediar(acum_nike,cont_nike)
    porc_nike=porcentaje()
    return prom_nike, porc_nike
    
#calculador de adidas
def calcular_a(cont_adidas, acum_adidas):
    prom_adidas=promediar(acum_adidas,cont_adidas)
    porc_adidas=porcentaje()
    return prom_adidas, porc_adidas
    
#calculador de zapatos
def totalzapatos(cont_nike,cont_adidas):
    cont_zapatos=cont_adidas+cont_zapatos

#printer
def imprimir(prom_nike,prom_adidas):
    print(f"el promedio de precios de zapatos nike es: {prom_nike}")
    print(f"el promedio de precios de zapatos nike es: {prom_adidas}")

#cuerpop principal
