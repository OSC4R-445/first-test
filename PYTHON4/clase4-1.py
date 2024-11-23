def validar_positivo(msj):
    

def cargar(arreglo):
    while True:
        print("carga de datos")
        edad=validar_positivo("Ingrese la edad")
        arreglo.append(edad)
        resp=input("Presione espacio para detener la carga")
        if resp== " ":
            break

def imprimir(arreglo, nombre, nombre_arreglo):
    print(f"Datos del arreglo {nombre_arreglo}")
    for i in range(len(arreglo)):
        print(arreglo[i])