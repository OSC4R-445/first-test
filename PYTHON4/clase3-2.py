#Burbuja sorting
def ordenar(arreglo):
    for i in range(len(arreglo)):
        for j in range(len(arreglo)-1):
            if arreglo[j]>arreglo[j+1]:
                aux=arreglo[j]
                arreglo[j]=arreglo[j+1]
                arreglo[j+1]=aux
    #end

def Iprint(arreglo):
    for i in arreglo:
        print(i)

#Main Body
names=["Mariana", "Fabiana", "Paola", "Jenny", "Alismar"]
ages=[12,20,45,4,15,7,8,1]
Iprint(names)
ordenar(ages)
print("-"*15)
Iprint(ages)