while True:
    #edad
    age = int(input("  la edad (solo numeros)\n  "))

    #dia
    print (f"""
        cual dia de la semana (escribe cualquiera de estos)
        lun - mar - mie - jue - vie
        sab - dom
        """)
    
    dia = input().lower()
    match dia:
        case "lun":
            desclun = .5
        case "mar":
            desclun = 1
        case "mie":
            desclun = 1
        case "jue":
            desclun = 1
        case "vie":
            desclun = 1
        case "sab":
            desclun = 1
        case "dom":
            desclun = 1
        case _:
            desclun = 1
            print ("debes escribir un dia, ej:-lun-")

    #hora
    print (f"""
        cual hora del dia (escribe tal y como se muestran a la izquierda)
        1pm = 1$ 
        2pm = 2$
        3pm = 3$
        otras horas = 4$
        """)
    hora = input().lower()
    match hora:
        case "1pm":
            price = 1
        case "2pm":
            price = 2
        case "3pm":
            price = 3
        case "5pm":
            price = 4
        case "7pm":
            price = 4
        case "9pm":
            price = 4
        case _:
            price = 0
            print("debes escribir 1, 2, 3, 5, 7 o 9, pegado a pm")

    #process
    if age<2 or age>70:
        desclun = 0
    elif age<10:
        if desclun>0:
            desclun = .5
    
    finalprice=price*desclun
    
    
    resp= input("deseas comprar otro boleto?\n s/n\n ").lower()

    #output
    print(f"""
        ===========Boleto==========
        dia de la funcion: {dia}        
        hora de la funcion: {hora}
        monto de la entrada: {price}$
        descuento : {desclun}
        monto final: {finalprice}$
        ===========================
    """)
    if resp !="s":
        break

