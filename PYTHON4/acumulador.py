def acumular(lista):
    acumulador=0
    for i in range(len(notas)):
        acumulador=acumulador+notas[i]
    return acumulador

def promediar(sumatoria,arreglo):
    promedio=sumatoria/len(arreglo)
    return promedio

#Cuerpo principal 
notas=[10,5,18,13,20,7,15]
numeros=[1250,215,230,20]
sumatoria=acumular(notas)
prom_notas=promediar(sumatoria,notas)
suma_numeros=acumular(numeros)

print(f"la sumatoria es {sumatoria}")
print(f"El promedio es {prom_notas}")