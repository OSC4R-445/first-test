def cargar(arreglo1,arreglo2,dato1,dato2):
    for i in range(len(arreglo1)):
        print(f"ingrese el {dato1}")
        valor1=input()
        print(f"ingrese el {dato2}")
        valor2=input()
        arreglo1[i]=valor1
        arreglo2[i]=valor2

def buscar_for(dato, arreglo):
    encontro=False
    for i in range(len(arreglo)):
        if arreglo[i]==dato:
            encontro=True
    return encontro 

def consultar(arreglo):
    print("Modulo para consultar datos")
    print("Ingresa el nombre del pais")
    country=input()
    existe=buscar_for(country,arreglo)
    if existe:
        print("Ya esta registrado")
    else:
        print("No esta registrado")

def imprimir(arreglo1,arreglo2,dato1,dato2):
    for i in range(len(arreglo1)):
        print(f"{dato1}: {arreglo2[i]} {dato2}: {arreglo2}")

def opciones():
    print("-"*10,"MENU","-"*10)
    print("1) Registrar datos")
    print("2) Ver listado")
    print("3) Buscar")
    print("4) Terminar")
    print("5) ERROR - DATO INGRESADO NO VALIDO")
    opcion=input()
    return opcion

#Main body
paises=[""]*5
ciudades=[0]*5

while True:
    opcion=opciones()
