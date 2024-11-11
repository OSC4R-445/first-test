def cargar(arreglo1,dato1,arreglo2,dato2):
    
    for i in range(len(arreglo1)):
        print(f"ingrese el {dato1}")
        valor1=input()
        print(f"ingrese el {dato2}")
        valor2=int(input())
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
    dato=input()
    existe=buscar_for(dato,arreglo)
    if existe:
        print("Ya esta registrado")
    else:
        print("No esta registrado")

def imprimir(arreglo1,dato1,arreglo2,dato2):
    print ("|"*10,"LISTADO","|"*10)
    for i in range(len(arreglo1)):
        print(f"{dato1}: {arreglo1[i]} {dato2}: {arreglo2[i]}")

def Menu():
    print("-"*10,"MENU","-"*10)
    print("1) Registrar datos")
    print("2) Ver listado")
    print("3) Buscar")
    print("4) Terminar")
    opcion=(input())
    return opcion

#Main body
paises=[""]*2
ciudades=[0]*2

while True:
    opcion=Menu()
    match opcion:
        case "1": 
            cargar(paises, "nombre del pais", ciudades, "cantidad  de ciudades")
        case "2": 
            imprimir(paises, "nombre del pais", ciudades, "numero de ciudades")
        case "3": 
            consultar(paises)
        case "4": 
            print("Bye Bye")
        case _: 
            print("ERROR - DATO INGRESADO NO VALIDO")
    if opcion=="4":
        break
