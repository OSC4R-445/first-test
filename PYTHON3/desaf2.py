def datos_de_entradas():
    print("##############")
    codigo = int(input("ingrese el codigo del articulo\n"))
    precio_unitario = float(input("ingrese el precio unitario\n"))
    cant = float(input("ingrese cantidad de producto\n"))
    print("##############")
    return codigo, precio_unitario, cant

def calculo_de_subtotal(precio_unitario, cant):
    subtotal = precio_unitario*cant
    return subtotal

def desc_if_cant_over6(cant, subtotal):
    if cant>6:
        desc = subtotal*.1
    else:
        desc = 0
    return desc

def total_a_pagar(subtotal, desc ):
    total = subtotal-desc
    return total

def print_mod(codigo, subtotal, desc, total):
    print("___________________________________________")
    print(f"|codigo de producto:          {codigo}   |")
    print(f"|precio subtotal:           {subtotal}   |")
    print(f"|descuento por tener +6 unidades: {desc} |")
    print(f"|total a pagar:             {total}      |")
    print("___________________________________________")

#cuerpo principal
codigo, precio_unitario, cant = datos_de_entradas()
subtotal = calculo_de_subtotal(precio_unitario, cant)
desc = desc_if_cant_over6(cant, subtotal)
total= total_a_pagar(subtotal, desc)
print_mod(codigo, subtotal, desc, total)
