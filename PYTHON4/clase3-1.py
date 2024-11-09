def buscar(dato, arreglo):
    encontro=False 
    i=0
    while i<(len(arreglo)) and not encontro:
        print(f"Se esta buscando en la pos {i}")
        if arreglo[i]==dato:
            encontro=True
        i=i+1
    return encontro 

def buscar_for(dato, arreglo):
    encontro=False
    for i in range(len(arreglo)):
        if arreglo[i]==dato:
            encontro=True
    return encontro 

def buscar_contar(dato, arreglo):
    cantidad=0
    for valor in arreglo:
        if valor== dato:
            cantidad=cantidad+1 #es la única forma válida 
    return cantidad

def procesar():
    print("Ingrese el nombre que desea buscar")
    name=input()
    existe=buscar_for(name, nombres)
    if existe:
        print("YA está registrado")
    else:
        print("NO está registrado")

#Main body

nombres=["Oscar", "Maria", "David", "Jesus"]
print("ingresa el nombre que desea buscar")
nBuscar= input()

buscar(nBuscar,nombres)
