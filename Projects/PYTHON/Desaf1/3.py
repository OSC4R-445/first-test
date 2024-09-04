nombre = (input ("ingresa tu nombre: "))
cedula = (input ("ingresa tu numero de cedula: "))
curso = (input ("ingresa el curso en el que estas: "))
mes_del_curso = int (input ("ingresa el mes: "))
asistencia = int (input ("cuantos dias de asistencia tienes en el curso: "))
if asistencia==4 :
    print (f"EL aprendiz {nombre} de cédula {cedula} participó en el curso {curso}, realizado durante el mes {mes_del_curso} con una duración de 20 horas académicas")
if asistencia <=4 : 
    print ("No ha cumplido con el mínimo de asistencias para obtener la constancia")