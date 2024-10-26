teams = ["Yankees", "Cardenales", "Magallanes"]
monts = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
venezuelaStates = ["Amazonas", "Anzoátegui", "Apure", "Aragua", "Barinas", "Bolívar", "Carabobo", "Cojedes", "Delta Amacuro", "Dependencias Federales", "Distrito Federal", "Falcón", "Guárico", "Lara", "Mérida", "Miranda", "Monagas", "Nueva Esparta", "Portuguesa", "Sucre", "Táchira", "Trujillo", "Vargas", "Yaracuy"]
dolars = [39.56, 40.41, 41.24, 42.34]

def cargar(arreglo):
    i=0
    while i<len(arreglo):
        print("Ingresa el nombre")
        dato = input()
        arreglo[i] = dato
        i=i+1

def cargar_for(lista):
    for i in range(len(lista)):
        print(f"Ingrese el dato a cargar")
        dato= input()
        lista[i]=dato

def imprimidos(lista):
    for dato in lista:
        print(dato)

#cuerpo principal

nombres=("","","","","")
print(nombres)
cargar(nombres)
print(nombres)