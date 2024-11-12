nombresVend=[""]*2
montoVend=[0]*2
cantFact=[0]*2

# a = int(input("cantidad de vendedores"))
# nombresVend=[""]*a
# montoVend=[0]*a
# cantFact=[0]*a

def dataInput(nombresVend,montoVend,cantFact):
    for i in range(len(nombresVend)):
        nombresVend[i]=input("ingresa el nombre del vendedor")
        montoVend[i]=float(input("ingres su monto total vendido"))
        cantFact[i]=int(input("ingresa su cantidad total de facturas"))
    return nombresVend, montoVend, cantFact

def dataPrint(nombresVend,montoVend,cantFact):
    for i in range(len(nombresVend)):
        print(f"""
        ===============
        vendedor: {nombresVend[i]}
        monto Total Vendido: {montoVend[i]}
        cantidad de facturas: {cantFact[i]}
        ===============
    """)

def acumularAvg(lista): #copiado de la clase2 :)
    acumulador=0
    for i in range(len(lista)):
        acumulador=acumulador+lista[i]
    acumulador=acumulador/len(lista) #esto tambien pero distinto jsjsjsjs
    return acumulador

def data_mayor(lista):
    aux=0
    for i in range(len(lista)):
        if aux<lista[i]:
            aux=lista[i]
    return aux

def data_menor(lista):
    aux=9**99
    for i in range(len(lista)):
        if aux>lista[i]:
            aux=lista[i]
    return aux


def contar(arreglo):
    contador=0
    for n in arreglo:
        if n>500: #antes era n<10
            contador=contador+1
    return contador

def listado(arreglo,arreglon):
    for n in range(len(arreglo)):
        if arreglo[n]>500:
            print(arreglon[n], arreglo[n])

#Main Body

nombresVend,montoVend,cantFact=dataInput(nombresVend,montoVend,cantFact)
dataPrint(nombresVend,montoVend,cantFact)

datMay=data_mayor(montoVend)
datMen=data_menor(montoVend)
avgVend=acumularAvg(montoVend)
over500=contar(montoVend)

print ("promedio vendido: ", avgVend)
print ("mayor monto vendido: ", datMay)
print ("menor monto vendido: ", datMen)
print ("cantidad de montos sobre 500: ", over500, "\n")
print ("lista de montos sobre 500:")
listado(montoVend,nombresVend)