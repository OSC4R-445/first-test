def acumular(lista):
    acumulador=0
    for i in range(len(lista)):
        acumulador=acumulador+lista[i]
    return acumulador

def promediar(sumatoria, arreglo):
    promedio = sumatoria/len(arreglo)
    return promedio

def contar(arreglo):
    contador=0
    for n in arreglo:
        if n<10:
            contador=contador+1
    return contador

def porcentaje(conte,contg):
    porc=conte/contg*100
    return porc

def print_select(lista):
    print ("listado de notas inferioresa a 10 puntos")
    for n in lista:
        if n<10:
            print(n)

def load_dat(arreglo):
    print("carga de datos")
    for i in range(len(arreglo)):
        print("ingrese el dato")
        num=int(input("Ingrese el dato"))
        arreglo[i]=num


#Main body 

notas=[13,12,20,10,9,5,7]
notass=[0]*7

suma=acumular(notas)

prom=promediar(suma,notas)
#contar no aprobados
efes=contar(notas)

porc=porcentaje(efes,notas)

print_select(notas)

