edad=-1
while edad<=0:
    print("ingresa la edad")
    edad=int(input())
print ("tu edad es",edad,"años")

while True:
    print("ingresa un numero")
    num=int(input())
    if num<=0:
        print("ingreas un numero positivo")
    else:
        break