def entradas():
    nombreE= input("Cual es el nombre del empleado")
    cantA= int(input("Cuantos autos fueron vendidos"))
    montoV= float(input ("cuanto vendio?"))
    return nombreE, cantA, montoV
def calcular(cantA, montoV):
    comA=300*cantA
    comV=montoV*0.18
    salTotal=120+comA+comV
    return salTotal, comV, comA
def printdata(nombreE, comA, comV, salTotal):
    print ("Empleado: ",nombreE)
    print ("Comision autos: ",comA)
    print ("Comision ventas: ",comV)
    print ("Salario final: ",salTotal)

#cuerpo principal
nombreE, cantA, montoV = entradas()
salTotal, comV, comA = calcular(cantA, montoV)
printdata(nombreE, comA, comV, salTotal)