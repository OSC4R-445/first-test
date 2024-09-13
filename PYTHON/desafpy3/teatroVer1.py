#3 boletos distintos

print("Tipo de boleto     precio")
print("  V                  50$")
print("  P                  30$")
print("  G                  15$")
print("\n   Cual tipo de boleto vas a llevar? V/P/G")

tipo=input().upper()
print("\n  Cuantos vas a llevar")
cant=int(input())
precio=0

##########      el selector de precio segun el boleto vpg
if tipo=="V":
    precio=50
elif tipo=="P":
    precio=30
elif tipo=="G":
    precio=15
else: 
    print ("ese no es u un boleto valido,")

###########     proceso del subtotal
subtotal=precio*cant

###########     los descuentos
if subtotal<=200:
    descuento=0
elif subtotal>200 and subtotal<=400:
    descuento=.05
elif subtotal>400 and subtotal<=1000:
    descuento=.07
elif subtotal>1000:
    descuento=.1
else:
    print("error de calculo descuento line28-36")#ignora esto

###########     proceso del descuento :)
descuento2=descuento*subtotal
montoAPagar=subtotal-descuento2

print(f"""
el tipo de boleto que va a llevar es: {tipo}
el precio de cada entrada individual es: {precio}
la cantidad de entradas es de: {cant}
el subtotal es: {subtotal}
su porcentage de descuento es: {descuento}
su monto de descuento es de {descuento2}
su monto total a pagar es: {montoAPagar}
""")