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

cantidad, cantidad1=cargar()
print(f"se procesar {cantidad} de productos, de los cuales {cantidad1} cuestan 1$")