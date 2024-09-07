porc=0
sueldobase=2500
monto_vendido=float(input("Cual es el monto vendido?"))
print("eres de tercera edad?")
terceraedad=input().upper()

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

porc = porc*monto_vendido
comis = monto_vendido+porc

if terceraedad=="S":
    print("tienes un bono de tercera edad")
print(f"""
su pago es
{monto_vendido+sueldobase+comis}
""")