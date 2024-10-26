def cargar_for(lista):
    for i in range(len(lista)):
        dato=int(input("Ingrese el dato a cargar"))
        lista[i]=dato
    return lista

def det_menor(arreglo):
    menor=21
    for i in range(len(arreglo)):
        if arreglo[i]<menor:
            menor=arreglo[i]
    return menor

def det_mayor(lista):
    mayor=-1
    for i in range(len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
    return mayor

def imprimir_selec(lista,valor):
    print(f"Las posiciones donde se encuentran en el valor {valor} son")

#main body
notas=[0]*10
cargar_for(notas)
det_menor(notas)