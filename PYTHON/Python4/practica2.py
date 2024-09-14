print(f"""
      Tallas disponibles
      Talla Precio
      S     50
      M     55
      L     60
      XL    65

    Cual talla desea
""")
talla=input().upper()
precio=0
descuento=0
match talla:
    case "S":
        preicio=50
    case "M":
        precio=55
    case "L":
        precio=60
    case "XL":
        precio=65
    case _:
        print("TALLA INVÁLIDA")
if precio>0:
    print (f"\nel precio de un pantalon de esa talla es {precio}")
    print ("\n      Cuantos vas a llevar?")

unidades=int(input())
if unidades>=6 and unidades<11:
    descuento=.05
elif unidades>=11 and unidades<24:
    descuento=.1
elif unidades>24:
    descuento=.15

porcdescuento=descuento*precio
finalcost=precio-porcdescuento
if unidades>0 and precio>0:
    print(f"""
          el tienes un descuento de {porcdescuento} 
          por la cantidad de pantalones que compraste, que son {unidades}
          entonces el coste total es de {finalcost}
""")
else:
    print("\n   No puedes llevar 0 pantalones :)\n")