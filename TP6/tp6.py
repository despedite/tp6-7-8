import os
os.system("cls")
banner = ("Trabajo Practico 6")
print(banner)
print("Programado en Python por Erik Bianco Vera")


amount = 3
existencia = [None] * amount
precio = [None] * amount
nepeps = [None] * amount
neueps = [None] * amount

for x in range(0, amount):
	print("\n("+str((x*2)+1)+"/"+str((amount*2)+1)+") Introduci la existencia de el dia "+str(x+1)+": ")
	existencia[x] = int(input())
	print("\n("+str((x*2)+2)+"/"+str((amount*2)+1)+") Introduci cuanto te salio el producto el dia "+str(x+1)+": ")
	precio[x] = float(input())
print("\n("+str((amount*2)+1)+"/"+str((amount*2)+1)+") Introduci cuantos productos salieron hoy: ")
salida = int(input())

print("\n----\n")

## PEPS

nepeps[0] = existencia[0]
nepeps[1] = existencia[1]
nepeps[2] = existencia[2]

if (existencia[0] >= salida): # OK
	print("PEPS: "+ str(salida) +"u X "+ str(precio[0]) +"$")
	nepeps[0] = existencia[0] - salida
	
elif (existencia[0] == 0 and existencia[1] >= salida): # OK
	print("PEPS: "+ str(salida) +"u X "+ str(precio[1]) +"$")
	nepeps[1] = existencia[1] - salida
	
elif (existencia[0] == 0 and existencia[1] == 0 and existencia[2] >= salida): # OK
	print("PEPS: "+ str(salida) +"u X "+ str(precio[2]) +"$")
	nepeps[2] = existencia[2] - salida
	
elif((existencia[0] + existencia[1]) >= salida): # NO
	i = (salida - (existencia[0]))
	print("PEPS: "+str(existencia[0])+"u X "+str(precio[0])+"$ / "+str(i)+"u X "+str(precio[1])+"$")
	nepeps[0] = 0
	nepeps[1] = existencia[1] - i
	
elif((existencia[0] + existencia[1] + existencia[2]) >= salida): # OK
	i = (salida - (existencia[1] + existencia[0]))
	print("PEPS: "+str(existencia[0])+"u X "+str(precio[0])+"$ / "+str(existencia[1])+"u X "+str(precio[1])+"$ / "+str(i)+"u X "+str(precio[2]))
	nepeps[0] = 0
	nepeps[1] = 0
	nepeps[2] = existencia[2] - i

else: # ?
	print("PEPS: La demanda es mayor a la oferta!")

## UEPS

neueps[0] = existencia[0]
neueps[1] = existencia[1]
neueps[2] = existencia[2]

if (existencia[2] >= salida):
	print("UEPS: "+ str(salida) +"u X "+ str(precio[2]) +"$")
	neueps[2] = existencia[2] - salida

elif (existencia[2] == 0 and existencia[1] >= salida): # OK
	print("UEPS: "+ str(salida) +"u X "+ str(precio[1]) +"$")
	neueps[1] = existencia[1] - salida
	
elif (existencia[2] == 0 and existencia[1] == 0 and existencia[0] >= salida): # OK
	print("UEPS: "+ str(salida) +"u X "+ str(precio[0]) +"$")
	neueps[0] = existencia[0] - salida

elif((existencia[2] + existencia[1]) >= salida): # OK
	i = (existencia[2] - existencia[1])
	print("UEPS: "+str(existencia[2])+"u X "+str(precio[2])+"$ / "+str(i)+"u X "+str(precio[1])+"$")
	neueps[1] = existencia[1] - i
	neueps[2] = 0
	
elif((existencia[2] + existencia[1] + existencia[0]) >= salida): # OK
	i = (salida - (existencia[2] + existencia[1]))
	print("UEPS: "+str(existencia[2])+"u X "+str(precio[2])+"$ / "+str(existencia[1])+"u X "+str(precio[1])+"$ / "+str(i)+"u X "+str(precio[0]))
	neueps[0] = existencia[1] - i
	neueps[1] = 0
	neueps[2] = 0
	
else: # OKS
	print("UEPS: La demanda es mayor a la oferta!")
	
## VP

total = ((existencia[0] * precio[0])+(existencia[1] * precio[1])+(existencia[2] * precio[2]))/(existencia[0] + existencia[1]+ existencia[2]) # creo que no
print("VP: "+str(salida)+"u X "+str(total)+"$")

## EXIST.

print("\nTu nueva existencia es:\n")
print("PEPS: Dia 1 - "+str(nepeps[0])+"u Dia 2 - "+str(nepeps[1])+"u Dia 3 - "+str(nepeps[2])+"u")
print("UEPS: Dia 1 - "+str(neueps[0])+"u Dia 2 - "+str(neueps[1])+"u Dia 3 - "+str(neueps[2])+"u")
print("VP: "+str((existencia[0] + existencia[1] + existencia[2]) - salida)+"u")