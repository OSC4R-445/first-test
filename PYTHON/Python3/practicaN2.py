print("cual es tu edad")
edad=int(input())
porcetaje=0
precio=100
if edad>0:
    if edad<2:
        porcetaje=1
    elif edad<=5:
        porcetaje=.5
    elif edad<=10:
        porcetaje=.2
    elif edad>=55:
        porcetaje=.3

estudiante=input().upper()
print("eres estudiante S/N?")
if estudiante=="S":
    print("Eres estudiante")
    if porcetaje<.25:
         porcetaje=.25
descuento=precio*porcetaje
total=precio-descuento
print (f"""
el porcentaje de descuento es: {porcetaje}
el descuento es de: {descuento}.bs
total a pagar: {total}.bs
""")