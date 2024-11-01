#1 Capricornio: del 22 de diciembre al 19 de enero.
#2 Acuario: del 20 de enero al 18 de febrero.
#3 Piscis: del 19 de febrero al 20 de marzo.
#4 Aries: del 21 de marzo al 19 de abril.
#5 Tauro: del 20 de abril al 20 de mayo.
#6 Géminis: del 21 de mayo al 20 de junio.
#7 Cáncer: del 21 de junio al 22 de julio.
#8 Leo: del 23 de julio al 22 de agosto.
#9 Virgo: del 23 de agosto al 22 de septiembre.
#10 Libra: del 23 de septiembre al 22 de octubre.
#11 Escorpio: del 23 de octubre al 21 de noviembre.
#12 Sagitario: del 22 de noviembre al 21 de diciembre.
signos_zodiacales=["Capricornio","Acuario","Piscis","Aries","Tauro","Geminis","Cacer","Leo","Virgo","Libra","Escorpio","Sagitario"]

def entradas():
    mesNacimiento=int(input("mes de nacimiento(num): "))
    diaNacimiento=int(input("dia de nacimiento(num): "))
    return mesNacimiento, diaNacimiento

def signoUser(mesNacimiento ,diaNacimiento,):
    sign=-1

    #capricornio
    if (mesNacimiento == 12 and diaNacimiento >= 22) or (mesNacimiento == 1 and diaNacimiento <= 19):
        sign=0
    
    #acuario
    elif (mesNacimiento == 1 and diaNacimiento >= 20) or (mesNacimiento == 2 and diaNacimiento <= 18):
        sign=1
    
    #piscis
    elif (mesNacimiento == 2 and diaNacimiento >= 19) or (mesNacimiento == 3 and diaNacimiento <= 20):
        sign=2

    # Aries: del 21 de marzo al 19 de abril.
    elif (mesNacimiento == 3 and diaNacimiento >= 21) or (mesNacimiento == 4 and diaNacimiento <= 19):
        sign=3

    # Tauro: del 20 de abril al 20 de mayo.
    elif (mesNacimiento == 4 and diaNacimiento >= 20) or (mesNacimiento == 5 and diaNacimiento <= 20):
        sign=4
    
    # Géminis: del 21 de mayo al 20 de junio.
    elif (mesNacimiento == 5 and diaNacimiento >= 21) or (mesNacimiento == 6 and diaNacimiento <= 20):
        sign=5

    # Cáncer: del 21 de junio al 22 de julio.
    elif (mesNacimiento == 6 and diaNacimiento >= 21) or (mesNacimiento == 7 and diaNacimiento <= 22):
        sign=6

    # Leo: del 23 de julio al 22 de agosto.
    elif (mesNacimiento == 7 and diaNacimiento >= 23) or (mesNacimiento == 8 and diaNacimiento <= 22):
        sign=7

    # Virgo: del 23 de agosto al 22 de septiembre.
    elif (mesNacimiento == 8 and diaNacimiento >= 23) or (mesNacimiento == 9 and diaNacimiento <= 22):
        sign=8

    # Libra: del 23 de septiembre al 22 de octubre.
    elif (mesNacimiento == 9 and diaNacimiento >= 23) or (mesNacimiento == 10 and diaNacimiento <= 22):
        sign=9

    # Escorpio: del 23 de octubre al 21 de noviembre.
    elif (mesNacimiento == 10 and diaNacimiento >= 23) or (mesNacimiento == 11 and diaNacimiento <= 21):
        sign=10

    # Sagitario: del 22 de noviembre al 21 de diciembre.
    elif (mesNacimiento == 11 and diaNacimiento >= 22) or (mesNacimiento == 12 and diaNacimiento <= 21):
        sign=11
    return sign

def TemporadaUser(mesNacimiento):
    season="a"
    if mesNacimiento == 11 or mesNacimiento == 12 or mesNacimiento ==1:
        season = "Invierno"

    if mesNacimiento >= 2 and mesNacimiento <= 4 :
        season = "Primavera"

    if mesNacimiento >=5 and mesNacimiento <= 7:
        season = "Verano"

    if mesNacimiento >= 8 and mesNacimiento <= 10:
        season = "Otonio"

    return season
    
#main body

while True:
    m,d = entradas()
    sgn = signoUser(m,d)
    ss = TemporadaUser(m)
    if m < 1 or m > 12 or d < 0 or d > 31 or sgn == -1:
        end = input("no escribiste una fecha real, vuelve a intentar o termina el programa: s/n\n").lower()
        if end != "s":
            break
    else:    
        end = input(f"""
        
    Tu signo es: {signos_zodiacales[sgn]}
    Tu temporada es: {ss}

        Quieres volver a probar el programa?
            s/n
    """).lower()
        if end != "s":
            break
print("bye :)")