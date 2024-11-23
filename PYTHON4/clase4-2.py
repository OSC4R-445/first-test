def validar_digitos(msj):

    while True:
        print(msj)
        dato=input()
        if dato.isdigit() and len(dato)>=7 and len(dato)<=8:
            return dato
        else:
            print("debe contener entre 7 y 8 digitos numericos unicamente.")

# Main body

cedula=validar_digitos("ingresa la cedula")
print(len(cedula))