#entradas
def input1():
    nombre = input("digame su nombre\n")
    modalidad = input("cual es tu modalidad?\n online/presencial\n").lower()
    nota = float(input("cual es su nota\n"))
    monto_pagado = float(input("cual es el monto pagado\n"))
    
    return nombre,  modalidad, nota, monto_pagado

#contador
def superado(modalidad, nota, onlines, aprobados, reprobados):

    # onlines=0     # 
    # aprobados=0   # 
    # reprobados=0  #

    if modalidad == ("o") or modalidad == ("online"):
        onlines = onlines+1
    if nota>=80:
        aprobados = aprobados+1
    else:
        reprobados = reprobados+1

    return aprobados, reprobados, onlines

#acumulador
def process(modalidad, monto_pagado, recibo_pre, recibo_onl, recibo_pre_T, recibo_onl_T):

    # recibo_pre=0
    # recibo_onl=0
    # recibo_pre_T=0
    # recibo_onl_T=0

    if modalidad == ("p") or modalidad == ("presencial"):
        recibo_pre = monto_pagado
        recibo_pre_T = recibo_pre_T+monto_pagado
    if modalidad == ("o") or modalidad == ("online"):
        recibo_onl = monto_pagado
        recibo_onl_T = recibo_onl_T+monto_pagado
    recibo_T = recibo_pre_T+recibo_onl_T 

    return recibo_onl, recibo_onl_T, recibo_pre, recibo_pre_T, recibo_T

#
def age_check(nombre, oldest, younguest, o_nombre, y_nombre):

    # oldest=0
    # younguest=200
    # o_nombre=""
    # y_nombre=""

    edad = int(input("cuantos anios tienes"))
    if edad>oldest:
        oldest = edad
        o_nombre = nombre
    if edad<younguest:
        younguest = edad
        y_nombre = nombre

    return oldest, o_nombre, younguest, y_nombre, edad

def FINALPRINTER(nombre,  modalidad, nota, monto_pagado, aprobados, reprobados, onlines, recibo_onl, recibo_onl_T, recibo_pre, recibo_pre_T, recibo_T, oldest, o_nombre, younguest, y_nombre, edad):

    print(f"""
        CADI F1 - seccion (XXXXXX-2024)
    ======================================================================
        ********************************************************
        Ultimo nombre del aprendiz: {nombre}
        edad del ultimo aprendiz: {edad}
        modalidad del ultimo aprendiz: {modalidad}
        nota del ultimo aprendiz: {nota}
        monto pagado del ultimo aprendiz: {monto_pagado}
        pago por clase online : {recibo_onl}
        pago por clase presencial : {recibo_pre}
        ********************************************************

        ********************************************************
        numero de aprendices aprobados: {aprobados}/{aprobados+reprobados}
        numero de aprendices reprobados: {reprobados}/{aprobados+reprobados}
        aprendices online: {onlines}
        monto total pagado de los aprendices online: {recibo_onl_T}
        monto total pagado de los aprendices presenciales: {recibo_pre_T}
        monto toal pagado de todos los aprendices: {recibo_T}
        aprendiz mas joven: {y_nombre}, edad del aprendiz: {younguest} anios
        aprendiz mas viejo: {o_nombre}, edad del aprendiz {oldest} anios
        ********************************************************
    ======================================================================
""")

#variables globales

#superado
onlines=0
aprobados=0
reprobados=0

#process
recibo_pre=0
recibo_onl=0
recibo_pre_T=0
recibo_onl_T=0

#age_check
oldest=0
younguest=200
o_nombre=""
y_nombre=""


#cuerpo principal

while True:

    nombre,  modalidad, nota, monto_pagado = input1()

    aprobados, reprobados, onlines = superado(modalidad, nota, onlines, aprobados, reprobados)

    recibo_onl, recibo_onl_T, recibo_pre, recibo_pre_T, recibo_T =process(modalidad, monto_pagado, recibo_pre, recibo_onl, recibo_pre_T, recibo_onl_T)

    oldest, o_nombre, younguest, y_nombre, edad = age_check(nombre, oldest, younguest, o_nombre, y_nombre)
    
    FINALPRINTER(nombre,  modalidad, nota, monto_pagado, aprobados, reprobados, onlines, recibo_onl, recibo_onl_T, recibo_pre, recibo_pre_T, recibo_T, oldest, o_nombre, younguest, y_nombre, edad)

    resp=input("mas datos? NO/SI").lower()
    if resp==("n") or resp==("no"):
        print("para tener variables globales a travez de modulos prescione: ####### [FATAL_ERROR_SHUTTING_DOWN_ALL_SERVERS], (para el prox desaf de seguro me seran de utilidad, jajaja)")
        break
