def cargar(arreglo1, arreglo2, arreglo3):
    print("Carga de datos")
    for i in range(len(arreglo1)): 
        print("Ingrese el nombre")
        nombre=input()
        print("Ingrese la nota")
        nota=int(input())
        print("Ingrese la nota")
        nota2=int(input())
        arreglo1[i]=nombre
        arreglo2[i]=nota
        arreglo3[i]=nota2

def promedio(arreglo2, arreglo3):
    promedio=0
    for i in range(len(arreglo2)):
        promedio=()

    return promedio


def imprimir(arreglo1, arreglo2, arreglo3, promedio):
    print("Datos cargados ")
    for i in range(len(arreglo2)):
        print(f"Nombre: {arreglo1[i]} nota: {arreglo2[i]}, nota2: {arreglo3[i]}. Con un promedio de: {promedio}")

#Cuerpo principal 
notas=[0,0,0,0]
nombres=["","","",""]
notas2=[0]*4

cargar(nombres, notas, notas2)
imprimir(nombres, notas, notas2, promedio)