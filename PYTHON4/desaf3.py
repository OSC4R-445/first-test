
def dataInput(nombresVend,montoVend,cantFact,cedula,genero):
    nombre=input("ingresa el nombre del vendedor: ")
    monto=float(input("ingres su monto total vendido: FLOAT: "))
    factura=int(input("ingresa su cantidad total de facturas: INT: "))
    cI=input("ingrese su numero de cuedula: ")
    sexo=input("Ingrese su genero: ")
    nombresVend.append(nombre)
    montoVend.append(monto)
    cantFact.append(factura)
    cedula.append(cI)
    genero.append(sexo)

    return nombresVend, montoVend, cantFact, cedula, genero

def dataPrint(nombresVend,montoVend,cantFact,cedula,genero):
    for i in range(len(nombresVend)):
        print(f"""        ===============
        vendedor: {nombresVend[i]}
        monto Total Vendido: {montoVend[i]}
        cantidad de facturas: {cantFact[i]}
        C.I: {cedula[i]}
        sexo: {genero[i]}""")
    print("        ===============")

def acumular_y_Avg(lista): #copiado de la clase2 :)
    acumulador1=0
    for i in range(len(lista)):
        acumulador1=acumulador1+lista[i]
    acumulador=acumulador1/len(lista) #esto tambien pero distinto jsjsjsjs
    return acumulador, acumulador1

def data_mayor(lista):
    aux=-1
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

def burbuja_algorithmx5(arreglo,arreglo2,arreglo3,arreglo4,arreglo5):
    for i in range(len(arreglo)):
        for j in range(len(arreglo)-1):
            if arreglo[j]<arreglo[j+1]:

                aux=arreglo[j]
                arreglo[j]=arreglo[j+1]
                arreglo[j+1]=aux

                aux2=arreglo2[j]
                arreglo2[j]=arreglo2[j+1]
                arreglo2[j+1]=aux2

                aux3=arreglo3[j]
                arreglo3[j]=arreglo3[j+1]
                arreglo3[j+1]=aux3

                aux4=arreglo4[j]
                arreglo4[j]=arreglo4[j+1]
                arreglo4[j+1]=aux4

                aux5=arreglo5[j]
                arreglo5[j]=arreglo5[j+1]
                arreglo5[j+1]=aux5

def busqueda_cedula(dato, arreglo):
    encontro=False
    i=0
    position=-1
    while i<len(arreglo):
        if arreglo[i]==dato:
            position=i
            encontro=True
        i=i+1
    return encontro, position

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

def buscar_for(dato, arreglo):
    encontro=False
    for i in range(len(arreglo)):
        if arreglo[i]==dato:
            encontro=True
            out=dato
    return encontro, out

def consultar(arreglo):
    print("Modulo para consultar vendedor")
    print("Ingresa el numero de cedula que desea buscar")
    dato=input()
    encontro, posicion=busqueda_cedula(dato, arreglo)
    if  posicion != -1 or encontro:
        print("Ya esta registrado: ", dato," En la posicion:", posicion)
    else:
        print("No esta registrado")

def menu():
    print(f"""
    1) Ingresar datos
    2) Mostrar datos
    3) Calcular monto total
    4) Monto menor y mayor
    5) Montos sobre 500
    6) Consultar vendedor
    7) Ordenar y ver vendedores
    8) Salir / Finalizar programa
          """)
    opcion=input()
    return opcion



#Main Body
nombresVend=[]
montoVend=[]
cantFact=[]
cedula=[]
genero=[]

while True:
    opcion=menu()
    match opcion:
        case "1": 
            print("|"*5,"ENTRADA DE DATOS","|"*5)
            nombresVend,montoVend,cantFact,cedula,genero=dataInput(nombresVend,montoVend,cantFact,cedula,genero)
            print("*"*20)

        case "2":
            print("|"*5,"MOSTRAR DATOS","|"*5)
            dataPrint(nombresVend,montoVend,cantFact,cedula,genero)
            print("*"*20)

        case "3":
            print("|"*5,"CALCULAR MONTO TOTAL","|"*5)
            avgVend,totVend=acumular_y_Avg(montoVend)
            print ("promedio vendido: ", avgVend)
            print ("Total vendido: ", totVend)
            print("*"*20)

        case "4":
            print("|"*5,"MONTO MENOR Y MAYOR","|"*5)
            datMay=data_mayor(montoVend)
            datMen=data_menor(montoVend)
            print ("mayor monto vendido: ", datMay)
            print ("menor monto vendido: ", datMen)
            print("*"*20)

        case "5":
            print("|"*5,"CANTIDAD DE MONTOS SOBRE 500","|"*5)
            over500=contar(montoVend)
            print ("cantidad de montos sobre 500: ", over500, "\n")
            print ("lista de montos sobre 500:")
            listado(montoVend,nombresVend)
            print("*"*20)

        case "6":
            print("|"*5,"CONSULTAR VENDEDOR","|"*5)
            consultar(cedula)
            print("*"*20)

        case "7":
            print("|"*5,"ORDENAR Y VER VENDEDORES","|"*5)
            burbuja_algorithmx5(montoVend,nombresVend,cantFact,cedula,genero)
            dataPrint(nombresVend,montoVend,cantFact,cedula,genero)
            print("*"*20)

        case "8":
            print("|"*5,"SALIR","|"*5)
            print("*"*5,"END OF PROGRAM","*"*5)

        case _:
            print("DATO INGRESADO NO VALIDO - LAS OPCIONES SON NUMEROS DEL 1 AL 8")

    if opcion=="8":
        break