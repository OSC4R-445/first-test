def loadString(msj, min, max):
    while True:
        print(msj)
        dato=input()
        if not (len(dato)>=min and len(dato)<=max and dato.isalpha()): # 'min length y max lenght' para el asegurarse que el 'dato' a retornar sea string y tenga el tamanio correcto (nombre)
            print("debe ser letras y una cantidad de caracteres entre:", min,"y",max)
        else:
            return dato

def searchCI(dato, arreglo): # con esto evitamos repetir pacientes con el uso de su cedula (en el modulo 'load()')
    encontro=False
    i=0
    position=-1
    while i<len(arreglo):
        if arreglo[i]==dato:
            position=i
            encontro=True
        i=i+1
    return encontro, position

def validDigitsCI(msj):
    # '.isdigit()' y 'len()' lo empleamos para evitar que se coloque una cedula incorrecta
    while True:
        print(msj)
        dato=input()
        if dato.isdigit() and len(dato)>=7 and len(dato)<=8:
            return dato
        else:
            print("debe contener entre 7 y 8 digitos numericos unicamente.")

def validDigitRange(msj,min,max,msj2):
    # lo usamos para validar la edad y el monto cancelado con su 'min' 'max' correspondiente y usamos 'msj2' para que el user vea los requisitos en caso de que se ingrese un valor incorrecto
    while True:
        print(msj)
        dato=input()
        if dato.isdigit():
            print("contiene solo numeros")
            dato=int(dato)
            if dato>=min and dato<=max: # edad / monto cancelado
                return dato # el ciclo se rompe con "return"
            else:
                print(msj2)
        else:
            print("debe ingresar solo numeros entre:",min,"y",max)

def validDigitRangeForDiagnostic(msj):
    while True:
        print(msj)
        dato=input()
        if len(dato)>=15:
            return dato
        else:
            print("debe contener al menos 15 caracteres")

def validKey(msj,msj2):
    while True:
        print(msj)
        dato=input().upper()
        if dato=="F" or dato=="M":
            return dato
        else:
            print(msj2)

def load(arreglo1,arreglo2,arreglo3,arreglo4,arreglo5,arreglo6):
    print("carga de datos")
    while True:
        nombre=loadString("Ingrese el nombre", 3, 25)
        ci=validDigitsCI("Ingrese la cedula")
        existe,ciPos=searchCI(ci,cedulas)
        edad=validDigitRange("Ingrese la edad",1,120,"el numero debe ser mayor a 0 y menor a 121")
        sexo=validKey("Ingrese el genero, femenino o masculino (F/M)","Genero femenino o masculino (F/M)")
        diagnostico=validDigitRangeForDiagnostic("Ingrese el diagnostico")
        montoCancelado=validDigitRange("Ingrese el monto cancelado",0,9**99,"ingrese un numero positivo")
        if existe:
            print("esta cedula ya esta registrada")
            continue
        else:
            arreglo1.append(nombre)
            arreglo2.append(ci)
            arreglo3.append(edad)
            arreglo4.append(sexo)            
            arreglo5.append(diagnostico)            
            arreglo6.append(montoCancelado)
            
        resp=input("Presione espacio para detener la carga de usuarios y regresar al menu")
        if resp== " ":
            break

def dataPrint():
    for i in range(len(nombres)):
        print(f"""        ===============
        nombre: {nombres[i]}
        C.I: {cedulas[i]}
        edad: {edades[i]}
        sexo: {sexos[i]}
        diagnsotico: {diagnosticos[i]}
        montos cancelados: {montosCancelados[i]}""")
    print("        ===============")

def calcAverageYAcum(lista): #copiado del desaf3 de la copia de la clase 2 :)
    acumulador=0
    for i in range(len(lista)):
        acumulador=acumulador+lista[i]
    average=acumulador/len(lista)
    return average, acumulador

def menu():
    print(f"""
    1) Ingresar datos
    2) Mostrar datos
    3) Mostrar dato por C.I
    4) Calcular promedio del monto total cancelado
    5) Mostrar paciente de  menor y mayor edad
    6) Salir / Finalizar programa
    
          """)
    opcion=input()
    return opcion

def detMin(arreglo):
    menor=121
    for i in range(len(arreglo)):
        if arreglo[i]<menor:
            menor=arreglo[i]
    return menor

def detMax(lista):
    mayor=-1
    for i in range(len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
    return mayor

# Main body
nombres=[]
cedulas=[]
edades=[]
sexos=[]
diagnosticos=[]
montosCancelados=[]

while True:
    opcion=menu()
    match opcion:
        case "1":
            load(nombres,cedulas,edades,sexos,diagnosticos,montosCancelados)
        
        case "2":
            dataPrint()
        
        case "3":
            datoCI=input("Ingrese la cedula del paciente")
            find,numCI=searchCI(datoCI,cedulas)
            if find:
                print(f"""        ===============
        nombre: {nombres[numCI]}
        C.I: {cedulas[numCI]}
        edad: {edades[numCI]}
        sexo: {sexos[numCI]}
        diagnsotico: {diagnosticos[numCI]}
        montos cancelados: {montosCancelados[numCI]}
        ===============""")
            else:
                print("numero no registrado")
        
        case "4":
            avg,acum=calcAverageYAcum(montosCancelados)
            print(f"El promedio del monto pagado pr los pacienteses: {avg}")

        case "5":
            maxAge=detMax(edades)
            minAge=detMin(edades)
            print("edad mayor: ",maxAge)
            print("edad menor: ",minAge)

        case "6":
            print ("""
    End of program.
                   """)
            
        case _:
            print("DATO INGRESADO NO VALIDO - LAS OPCIONES SON NUMEROS DEL 1 AL 6")

    if opcion=="6":
        break