def procesar():
    cont_nike=0 #contador especifico para la marca nike
    acum_nike=0 #acumulador especifico de los precios de los zapatos
    cont_adidas=0
    acum=adidas=0
    while True:
        marca=input("Ingrese la marca a procesar").lower()
        precio=float(input("Ingrese el precio de la marca"))
        if marca=="nike":
            cont_nike=cont_nike+1
            acum_nike=acum_nike+precio
        if marca=="adidas":
            cont_adidas=cont_adidas+1
            acum_adidas=acum_adidas+precio
        if marca=="":
            b=0
        #controlar el ciclo
        resp=input("Presione espacio para dentener")
        if resp==" ":
            break
    return cont_nike, acum_nike

def promediar(acum, cont):
    if cont>0:
        promedio=acum/cont
    else:
        promedio=0
    return promedio

def calcular_n(cont_nike, acum_nike):
    prom_nike=promediar(acum_nike,cont_nike)
    return prom_nike

def calcular_a(cont_adidas, acum_adidas):
    prom_adidas=promediar(acum_adidas,cont_adidas)
    return prom_adidas
    
def imprimir(prom_nike):
    print(f"el promedio de precios de zapatos nike es: {prom_nike}")

#cuerpop principal
c_n,a_n=procesar()
p=calcular_n(c_n,a_n)
print(p)