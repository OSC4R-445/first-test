def cargar_string(msj, min, max):
    while True:
        print(msj)
        dato=input()
        if not (len(dato)>=min and len(dato)<=max):
            print("no cumple con la longitud establecida")
        else:
            return dato

def validar_positivo(msj):
    num=-1
    while not num>0:
        print(msj)
        num=int(input())
        if not num>0:
            print("El numbreo debe ser positivo")
        else:
            return num

def buscar(dato, arreglo):
    find=False
    i=0
    while not find and i<len(arreglo):
        if arreglo[i]== dato:
            find=True
        i+1
    return find

def cargar(arreglo1, arreglo2):
    print("carga de datos")
    while True:
        nombre=cargar_string("Ingrese el nombre", 2, 12)
        ci=validar_positivo("Ingrese la cedula")
        existe=buscar(ci,arreglo2)

        if existe:
            print("esta cedula ya esta registrada")
            continue
        else:
            arreglo1.append(nombre)
            arreglo2.append(ci)

        resp=input("Presione espacio para detener la carga")
        if resp== " ":
            break

def imprimir(arreglo, nombre_arreglo, arreglo2, nombre_arreglo2):
    print(f"Datos a mostrar: {nombre_arreglo}, {nombre_arreglo2}")
    for i in range(len(arreglo)):
        print(f"{arreglo[i]} -> {arreglo2[i]}")

# def imprimir(arreglo, nombre_arreglo):
#     print(f"Datos a mostrar: {nombre_arreglo}")
#     for i in range(len(arreglo)):
#         print(f"{arreglo[i]}")

def validar_digitos(msj):
    while True:
        print(msj)
        dato=input()
        if dato.isdigit() and len(dato)>=7 and len(dato)<=8:
            return dato
        else:
            print("debe contener entre 7 y 8 digitos numericos unicamente.")

# Main body
nombres=[]
cedulas=[]

cargar(nombres, cedulas)
imprimir(nombres,"Nombres",cedulas,"Cedulas")
# imprimir(nombres, "Nombres")
# imprimir(cedulas, "Cedulas")