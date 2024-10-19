def procesar():
    acumulador = 0 #suma montos, acumulador general
    contador = 0 #contador general para todos los montos
    while True:
        print("Ingresa el monto a sumar")
        monto = float(input()) #acumulador del monto
        acumulador = acumulador+monto #variable que tiene el valor que quiero sumar/acumular
        contador = contador+1
        resp = input("Presione espacio para detener")
        if resp == " ":
            break
    return acumulador, contador
def promediar(acumulador, contador):
    if contador>0:
        promedio = acumulador/contador
    else:
        promedio = 0
    return promedio
def imprimir(contador, acumulador, promedio):
    print(f"La sumatoria de los montos es {acumulador}")
    print(f"La cantidad de montos procesados es {contador}")
    print(f"El promedio de los montos procesados es {promedio}")
#cuerpo principal
suma_montos, cont_montos = procesar()
promedio_montos = promediar(suma_montos, cont_montos)
imprimir (cont_montos, suma_montos, promedio_montos)