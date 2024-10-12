#contador
def cargar():
    cant_productos=0 # contador general
    cant_precio1=0 #contador especifico

    while True:
        cant_productos=cant_productos+1
        nombre= input("Nombre del producto\n")
        precio=float(input("cuanto cuesta?\n"))
        if precio==1:
            cant_precio1=cant_precio1+1
        resp=input("precione espacio para detener")
        if resp==" ":
            break
    return cant_productos, cant_precio1

def imprimir (cant_productos, cant_precio1):
    print(f"se procesar {cant_productos} de productos, de los cuales {cant_precio1} cuestan 1$")

cantidad, cantidad1=cargar()
imprimir(cantidad, cantidad1)