#4
alumnos = int(input("cuantos alumnos hay"))
print (f"hay: {alumnos} , son suficientes? {alumnos>=8}")
#5
cant = int(input("cuanto vas a pagar"))
print (f"tu pago es de: {cant} si pagaste mas tienes un descuento: {cant>10000}")
#6
beisbol = int(input("tenemos suficientes entradas para el juego de beisbol?"))
print (f" hay {beisbol} entradas, son suficientes para todos? {beisbol>3}")
#7
carrito = int(input("cuantos productos tienes en tu carrito?"))
print (f" tienes {carrito} productos, si son mas de 12 no te los puedes llevar {12>=carrito}")

#TEMPERATURA
temp = int(input("indica la temperatura"))
if temp<20:
    (print("hace frio"))#; 
if temp>=20:
    (print("hace calor"))
#else: 
#    print("me estoy asando aaaaaa")

#AGE
edad = int(input("dime tu edad tienes"))
if edad>17:
    print("tas viejo")#;
if edad<=17:
    print("tas joven")
#else:
#    print("tas joven")

#PREGUNTA
answ = input ("responde si o no \n")
if answ.lower()=="si":
    print("si...")
if answ.lower()=="no":
    print("no...")