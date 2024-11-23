def validar_positivo(msj):
    num=-1
    while not num>1:
        print(msj)
        num=int(input())
        if not num>1:
            print("El numbreo debe ser positivo")
        else:
            return num

def cargar(arreglo):
    while True:
        print("carga de datos")
        edad=validar_positivo("Ingrese la edad")
        arreglo.append(edad)
        resp=input("Presione espacio para detener la carga")
        if resp== " ":
            break

def imprimir(arreglo, nombre_arreglo):
    print(f"Datos del arreglo {nombre_arreglo}")
    for i in range(len(arreglo)):
        print(arreglo[i])

#Cuerpo principal
edades=[]
cargar(edades)
imprimir(edades, "Edades")