def entradas(nombreE,cantA,MontoV):
    nombreE= input("Cual es el nombre del empleado")
    cantA= int(input("Cuantos autos fueron vendidos"))
    MontoV= float(input ("cuanto vendio?"))
def calcular(cantA, comA, comV, montoV, salTotal):
    comA=300*cantA
    comV=montoV
    salTotal=120+comA+comV
def printdata(nombreE, comA, comV, salTotal):
    print ("Empleado: ",nombreE)
    print ("Comision autos: ",comA)
    print ("Comision ventas: ",comV)
    print ("Salario final: ",salTotal)

#cuerpo principal
entradas()
calcular()
printdata()