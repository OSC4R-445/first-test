#entradas
def input1 ():
    nombre = input("digame su nombre")
    modalidad = input("cual es la modalidad").lower
    nota = float(input("cual es su nota"))
    monto_pagado = float(input("cual es el monto pagado"))
    
    return nombre,  modalidad, nota, monto_pagado

def age_check (nombre):
    oldest=0
    younguest=200
    edad = int(input("cuantos anios tienes"))
    if edad>oldest:
        oldest = edad
        o_nombre = nombre
    elif edad<younguest:
        younguest = edad
        y_nombre = nombre
    return oldest, o_nombre, younguest, y_nombre
    



def process (modalidad, monto_pagado, nota):
    if modalidad == "online" or "o":
        recibo_pre = monto_pagado
        recibo_pre_T = recibo_pre_T+monto_pagado
    elif modalidad == "precencial" or "p":
        recibo_onl = monto_pagado
        recibo_onl_T = recibo_onl_T+monto_pagado
    if nota<80:
        U_Failed_ap = True
        Failed_ap = Failed_ap+1



def trueinput ():


#cuerpo principal
