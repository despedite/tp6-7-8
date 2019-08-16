import os
import time
import csv

# Repetir codigo si el input no es valido.
invalid_input = True

# Sueldo Básico: lo introduce la persona
sueldobasico = 45000

# Días del mes: Cuantos días trabaja la persona
diasdelmes = 20

# Turnos: Se le paga un porcentaje añadido a el sueldo
turnomanana = 10
turnotarde = 20
turnonoche = 30

# Jubilacion: Se le descuenta este porcentaje del total
jubilacion = 11
obrasocial = 3
sindicato = 3

# Descontación por faltas: Se te saca esta plata bruta cada día que faltas
faltas = 500

# Premio: La gente que no faltó en todo el mes recibe un X% mas, la gente que falto un dia recibe Y% mas.
sinfaltas = 25
faltoundia = 15

# Feriados: (Sueldo / días al mes) * Turnomañana * Presentismo (si aplicable)

# Licencia: feriado * diaslicencia
try:

	# PARTE 1: SABER EN QUE TURNO TRABAJA
	
	while invalid_input == True:
		invalid_input = False
		os.system("cls")
		print("Trabajo Práctico 8")
		print("Programado en Python por Erik Bianco Vera")

		print("\n¿En que turno trabaja?\n(M)añana / (T)arde / (N)oche")
		turnotrabajado = input()
		trueturno = turnotrabajado
		
		if (turnotrabajado.upper() == "M"):
			turnotrabajado = turnomanana
		elif (turnotrabajado.upper() == "T"):
			turnotrabajado = turnotarde
		elif (turnotrabajado.upper() == "N"):
			turnotrabajado = turnonoche
		else:
			print("El valor introducido no es correcto.")
			print("Introduzca un valor que corresponda con las opciones: M/T/N")
			time.sleep(3)
			invalid_input = True

	# PARTE 2: SABER CUANTAS AUSENCIAS TIENE

	print("\n¿Cuantas ausencias tiene?\n* Si tiene asistencia perfecta, introduzca 0.")
	ausentismo = int(input())
	invalid_input = True
	trueausentismo = ausentismo
	
	# PARTE 3: SABER CUANTOS DIAS DE FERIADO SE TOMO
	
	while invalid_input == True:
		invalid_input = False

		print("\n¿Cuantos días de feriado trabajó?\n* Si no trabajó en ningun día feriado, introduzca 0.")
		diasferiados = int(input())

		if (diasferiados > 0):
			if ausentismo == 0:
				cantferiados = diasferiados
				diasferiados = (sueldobasico / diasdelmes) + (((sueldobasico / diasdelmes) * turnotrabajado) / 100) + (((sueldobasico / diasdelmes) * sinfaltas) / 100)
				pagonetoferiados = cantferiados * diasferiados
			elif ausentismo == 1:
				cantferiados = diasferiados
				diasferiados = (sueldobasico / diasdelmes) + (((sueldobasico / diasdelmes) * turnotrabajado) / 100) + (((sueldobasico / diasdelmes) * faltoundia) / 100)
				pagonetoferiados = cantferiados * diasferiados
			else:
				cantferiados = diasferiados
				diasferiados = (sueldobasico / diasdelmes) + (((sueldobasico / diasdelmes) * turnotrabajado) / 100)
				pagonetoferiados = cantferiados * diasferiados
		elif (diasferiados == 0):
			cantferiados = diasferiados
			pagonetoferiados = cantferiados * diasferiados
		else:
			# Solo ocurre si el usuario se hace el vivo y pone "-1" o similares.
			print("El valor introducido no es correcto.")
			print("Introduzca un valor que corresponda con las opciones: 0, >0")
			time.sleep(3)
			invalid_input = True

	# PARTE 4: SABER CUANTOS DIAS DE LICENCIA SE TOMO
	
	invalid_input = True
	while invalid_input == True:
		invalid_input = False

		print("\n¿Cuantos días de licencia se tomo?\n* Si no tomo ningun dia de licencia, introduzca 0.")
		diasdelicencia = int(input())

		if (diasdelicencia > 0):
			diaslicenciados = diasdelicencia
			valorlicencia = diasdelicencia * diasferiados
		elif (diasdelicencia == 0):
			diaslicenciados = diasdelicencia
			valorlicencia = 0
		else:
			# Solo ocurre si el usuario se hace el vivo y pone "-1" o similares.
			print("El valor introducido no es correcto.")
			print("Introduzca un valor que corresponda con las opciones: 0, >0")
			time.sleep(3)
			invalid_input = True
except KeyboardInterrupt:
    print('\n\nSe canceló la operación. Saliendo...')
	
horarioporciento = ((sueldobasico * turnotrabajado) / 100)
bonusporhorario = sueldobasico + horarioporciento

print("\n---------")
print("BONUS")
if (turnotrabajado == 10):
	print("Por horario: 10% extra de "+ str(sueldobasico) + " = " + str(bonusporhorario))
elif (turnotrabajado == 20):
	print("Por horario: 20% extra de "+ str(sueldobasico) + " = " + str(bonusporhorario))
elif (turnotrabajado == 30):
	print("Por horario: 30% extra de "+ str(sueldobasico) + " = " + str(bonusporhorario))
print("Pago por todos los feriados: " + str(cantferiados) + " x " + str(diasferiados) + " = " + str(pagonetoferiados))
print("Pago por todos los dias de licencia: " + str(diaslicenciados) + " x " + str(diasferiados) + " = " + str(valorlicencia))
valorbruto = bonusporhorario + pagonetoferiados + valorlicencia

print("\n---------")
print("DESCUENTOS")
descuentoporfaltas = (ausentismo * faltas)
print("Descuento por faltas: " + str(ausentismo) + " x -" + str(faltas) + " = -" + str(descuentoporfaltas)) 
descuentoporjubilacion = ((sueldobasico * jubilacion) / 100)
print("Descuento por jubilacion: -" + str(jubilacion) + "% de " + str(sueldobasico) + " = -" + str(descuentoporjubilacion)) 
descuentoporobrasocial = ((sueldobasico * obrasocial) / 100)
print("Descuento por obra social: -" + str(obrasocial) + "% de " + str(sueldobasico) + " = -" + str(descuentoporobrasocial)) 
descuentoporsindicato = ((sueldobasico * sindicato) / 100)
print("Descuento por sindicato: -" + str(sindicato) + "% de " + str(sueldobasico) + " = -" + str(descuentoporsindicato))
valordescuentos = descuentoporfaltas + descuentoporjubilacion + descuentoporobrasocial + descuentoporsindicato 

print("\n---------")
print("SUELDO TOTAL")
print("Sueldo bruto: " + str(valorbruto))
print("Descuentos: -" + str(valordescuentos))
valorneto = valorbruto - valordescuentos
print("Sueldo neto: " + str(valorneto))

try:
	print("\nIntroduce el nombre del trabajador para guardarlo.")
	print("* Esto es opcional - si terminaste, solo usa Ctrl-C para salir.")

	nombre = input()

except KeyboardInterrupt:
    print('\n\nSaliendo...')
# CSV

with open('tp8.csv', mode='a', newline='\n') as csv_file:
    fieldnames = ['nombre', 'turno', 'ausentismo', 'diasferiados', 'diasdelicencia', 'bruto', 'descuento', 'neto']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')
    writer.writerow({'nombre': nombre, 'turno': trueturno.upper(), 'ausentismo': trueausentismo, 'diasferiados': cantferiados, 'diasdelicencia': diaslicenciados, 'bruto': valorbruto, 'descuento': valordescuentos, 'neto': valorneto})