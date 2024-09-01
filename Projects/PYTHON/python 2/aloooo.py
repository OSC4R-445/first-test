alumnos = int(input("cuantos alumnos hay:\n"))
if alumnos>=8: 
    print("son suficientes alumnos para empezar la clase")
else:
    print("no son suficientes alumnos para empezar la clase")
#2
cantp = int(input("cuanto vas a pagar? necesitas almenos 10000 para obtener un descuento:\n"))
if cantp>=10000:
    print (f"obtuviste un descuento del 20%! ahora pagaras: {cantp*.8}")
else:
    print ("no obtuviste el descuento :(,  triste... paga el total xd:", cantp)
