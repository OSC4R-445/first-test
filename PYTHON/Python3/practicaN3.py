porc=0
sueldobase=2500
monto_vendido=float(input("Cual es el monto vendido?"))
print("cual es tu sexo?")
sexo=input().upper()
print("cual es tu edad?")
edad = int(input())
bono=0

if monto_vendido>0 and monto_vendido<75000:
    porc=.05
elif monto_vendido>=90000 and monto_vendido<20000:
    porc=.07
elif monto_vendido>=300000 and monto_vendido<1000000:
    porc=.08
elif monto_vendido>=1500000:
    porc=.1
else:
    porc=.06

if (sexo=="F" and edad==55) or (sexo=="M" and edad==60):
    bono = 40000
porc = porc*monto_vendido
comis = monto_vendido+porc
salariof = monto_vendido+sueldobase+comis+bono


print(f"""
    tiene un sueldo base de : {sueldobase}
    su porcentaje de venta es : {porc}
    su comision es : {comis}
    bono de tercera edad : {bono}
    su pago final es: {salariof}
""")
