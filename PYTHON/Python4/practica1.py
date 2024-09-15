edo_civil= input (f"cual es tu estado civil? (S)oltero (C)asado (V)iuda (P)areja").upper()
soltero=(edo_civil=="S")
casado=(edo_civil=="C")
viuda=(edo_civil=="V")
Pareja=(edo_civil=="P")

if soltero:
    print("jajajaja, full dentro del .gitignore")

if not soltero:
    print("F, ahora tienes q esperar la opinion de otro, pero...")
    if Pareja:
        print ("no se te habran olvidaron tus pastillas??")
    elif casado:
        print("na, 'tas soñando jajajajaja")
    elif viuda:
        print("F, pero en negrita")