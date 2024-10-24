#Variables sucursales
monto_promedio_sucursales=0
monto_total_factura_sucursales=0

def entrada_sucursal():
    nombre_sucursal=input("cual es el nombre de la sucursal   ")
    ciudad_sucursal=input("cual es la ciudad de la sucursal   ")
    cantEmpleados_sucursal=int(input("cuantos empleados tiene la sucursal   "))
    return nombre_sucursal, ciudad_sucursal, cantEmpleados_sucursal

def calc(monto_total_factura, iva, monto_promedio):

    monto_base=float(input("cual es el monto base   "))
    cant_articulos=int(input("cuantos articulos se compraron   "))

    iva=monto_base*.16

    monto_total_factura=monto_base+iva
    monto_promedio=monto_total_factura/cant_articulos

    return monto_total_factura, iva, monto_promedio

def calc_menos1000(monto_total_factura, i, monto_menosDe1000, porc_monto_menosDe1000):
    if monto_total_factura<1000:
        monto_menosDe1000=monto_menosDe1000+1
        porc_monto_menosDe1000=(monto_menosDe1000/i)

    return monto_menosDe1000, porc_monto_menosDe1000

def promedio_sucursales(monto_promedio_sucursal, monto_total_factura_sucursal, monto_promedio_sucursales, monto_total_factura_sucursales):
    monto_promedio_sucursales=monto_promedio_sucursales+monto_promedio_sucursal
    monto_total_factura_sucursales= monto_total_factura_sucursales+monto_total_factura_sucursal

    return monto_promedio_sucursales, monto_total_factura_sucursales


def sucursales(monto_promedio_sucursales, monto_total_factura_sucursales):
    monto_promedio_sucursal=0
    monto_total_factura=0
    monto_menosDe1000_sucursal=0
    monto_total_factura_sucursal=0
    porc_monto_total_factura_sucursal=0

    print("#####################PROGRAMA_START#######################")
    #sucursales
    for n in range(1,5):
        print(f"||||===================sucursal {n}===================||||")
        nombre_sucursal, ciudad_sucursal, cantEmpleados_sucursal=entrada_sucursal()

        monto_total_factura=0
        monto_promedio=0
        iva=0
        monto_menosDe1000=0
        porc_monto_menosDe1000=0
        i=0

        print(f"SUCURSAL {nombre_sucursal}")
        print(f"CIUDAD {ciudad_sucursal}")
        print(f"NUMERO DE EMPLEADOS: {cantEmpleados_sucursal}")
        #factura
        while True:
            i=i+1
            print("================factura================")
            monto_total_factura, iva, monto_promedio=calc(monto_total_factura, iva, monto_promedio)
            monto_menosDe1000,porc_monto_menosDe1000=calc_menos1000(monto_total_factura, i, monto_menosDe1000, porc_monto_menosDe1000)

            print("factura: ", monto_total_factura)
            print("iva: ", iva)
            print("monto promedio: ", monto_promedio)
            if monto_total_factura<1000:
                print("esta factura tiene menos de 1000")
            print("=======================================")
            breaker=input("si quieres ya NO quieres hacer otra factura presiona espacio")
            if breaker==" ":
                break

        monto_total_factura_sucursal=monto_total_factura_sucursal+monto_total_factura
        monto_promedio_sucursal=monto_promedio_sucursal+monto_promedio
        
        monto_menosDe1000_sucursal=monto_menosDe1000_sucursal+monto_menosDe1000
        porc_monto_total_factura_sucursal=(monto_menosDe1000_sucursal/4)

        print(f"MONTO TOTAL FACTURADO EN LA SUCURSAL {monto_total_factura_sucursal}")
        print(f"porcentage de las facturas con un monto menor a 1000 EN LA SUCURSAL: {porc_monto_total_factura_sucursal}")
        
        print("||||==================================================||||")
    monto_promedio_sucursales, monto_total_factura_sucursales=promedio_sucursales(monto_promedio_sucursal, monto_total_factura_sucursal, monto_promedio_sucursales, monto_total_factura_sucursales)
    
    print(f"  LA FACTURACION OBTENIDA POR TODAS LAS SUCURSALES ES {monto_total_factura_sucursales}")
    print(f"  EL MONTO OBTENIDO POR TODAS LAS SUCURSALES ES {monto_promedio_sucursales} ")
    print("######################PROGRAMA_END########################")

sucursales(monto_promedio_sucursales, monto_total_factura_sucursales)