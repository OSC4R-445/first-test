# las weas que hacen las funciones funcionar jsjsjs
from random import randint

# entradas
date = int (input ("que fecha es hoy (dd/mm/aaaa)"))
car = input ("que modelo quieres alquilar?")
time = int (input ("cuantos dias"))
# magic
dayCost = randint (25,50)

# procesos
totalCost = int (dayCost*time) 
downPayment = totalCost*0.35 
lastday = int (time+1)



# salida DESAF2
if time >=30 :
       print (f"""
              no puede alquilar tantos días
              """)
else :
# salida ORIGINAL
       if time>=10 :
              print (f"""
              **************************
              Fecha {date}
              el coste por dia es de: {dayCost}$
              el costo total es: {totalCost}$
              el pago inicial es 35% del total: {downPayment}$
              recuerde devolver el modelo: 
              "{car}" con el tanque lleno y como el tiempo de {time} dias supera los 10
              debe pagar un monto adicional de deposito de 100$ además
              con un max de {lastday} dia(s) para evitar costos extra
              **************************
              Gracias por alquilar el vehiculo en [REDACTADO]
              conserva la factura hasta terminar el alquiler!
              **************************
              """)
       else :
              print (f"""
              **************************
              Fecha {date}
              el coste por dia es de: {dayCost}$
              el costo total es: {totalCost}$
              el pago inicial es 35% del total: {downPayment}$
              recuerde devolver el modelo: 
              "{car}" con el tanque lleno y 
              con un max de {lastday} dia(s) para evitar costos extra
              **************************
              Gracias por alquilar el vehiculo en [REDACTADO]
              conserva la factura hasta terminar el alquiler!
              **************************
              """)