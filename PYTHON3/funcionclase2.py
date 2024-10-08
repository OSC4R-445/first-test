def calcx2 (number):
    x2=number*2
    return x2
def calcxx2 (base , exp):
    potencia= base**exp
    return potencia
#principal bod
print ("ingresa un numero +")
number=int(input())
doble=calcx2(number)
number2=(int(input("ingresa un numero + (otra vez)")))
print (calcxx2(number,number2))

