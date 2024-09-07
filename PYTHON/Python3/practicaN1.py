print("Tipo     precio")
print("A    80")
print("B    180")
print("C    250")
print("\n   Cual tipo de pantalon va a llevar? A/B/C")
tipo=input().upper()
print("\n  Cuantos va a llevar")
cant=int(input())
precio=0
if tipo=="A":
    precio=80
elif tipo=="B":
    precio=180
elif tipo=="C":
    precio=250
else: 
    print ("ese no es u un tipo valido,")

precio_total=precio*cant
if precio !=0: 
    print(f"""
 el coste del pantalon de tipo {tipo} es: {precio}
 y se va a llevar: {cant}
 por lo que el coste final va a ser: {precio_total}
    """)
else:
    print("hubo un error con la transaccion")