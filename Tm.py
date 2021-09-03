# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 16:13:36 2021

@author: Usuario
"""
"""
1. Haga un algoritmo que calcule la masa de la siguiente fórmula:
Masa = (presión * volúmen) / (0.37 * (temperatura + 460))
"""
presion = float ( input ( 'Digite el valor de la presion : '))
volumen = float (input ('Digite el valor del volumen : '))
temperatura = float ( input ('Digite el valor de la temperatura : '))
masa = (presion * volumen) / (0.37 * (temperatura + 460))
print(f'El valor de la masa es : {masa} ')

"""
2. Calcular el número de pulsaciones que una persona debe tener por
cada 10 segundos de ejercicio, si la fórmula es:
Num. Pulsaciones = (200 – edad) /10.
"""

edad = int (input ('Digite la edad : '))
numeroPulsaciones = (200 - edad)/10
print(f'El numero de pulsacion son : {numeroPulsaciones}')

"""
3. Tres personas deciden invertir su dinero para fundar una empresa.
Cada una de ellas invierte una cantidad distinta. Obtener el porcentaje
que cada quien invierte con respecto a la cantidad total invertida.
"""

inversorUno = float (input('Digite la cantidad invertida : $ '))
inversorDos = float (input('Digite la cantidad invertida : $ '))
inversorTres = float (input('Digite la cantidad invertida : $ '))
total = inversorUno + inversorDos + inversorTres
porInversorUno = (inversorUno / total) * 100
porInversorDos = (inversorDos / total) * 100
porInversorTres = (inversorTres / total) * 100
print(f'El procentaje invertido por el inversor uno es {porInversorUno}% ')
print(f'El procentaje invertido por el inversor uno es {porInversorDos}% ')
print(f'El procentaje invertido por el inversor uno es {porInversorTres}% ')

"""
4. Un banco da a sus ahorradores un interes de 1.5% sobre el monto
ahorrado. Teniendo como dato de entrada el saldo inicial del
ahorrador determine el saldo final.
"""
saldoInicial = float (input('Digite el saldo inicial : $ '))
interes = saldoInicial * 0.015
saldoFinal = saldoInicial + interes
print(f'El saldo final es de : ${saldoFinal} ')

"""
5. Una empresa le hace los siguientes descuentos sobre el sueldo base
a sus trabajadores: 1% por ley de politica pública, 4% por seguro
social, 0.5% por seguro forzoso y 5% por caja de ahorro. Realice un
algoritmo que determine el monto de cada descuento y el monto total
a pagar al trabajador.
"""

sueldoBase = float (input('Digite el sueldo base $ '))
politicaPublica = sueldoBase * 0.01
seguroSocial = sueldoBase * 0.04
seguroForzoso = sueldoBase * 0.005
cajaAhorro = sueldoBase * 0.05
totalDescuento = politicaPublica + seguroSocial + seguroForzoso + cajaAhorro
montoPagar = sueldoBase - totalDescuento
print (f'Descuento por ley de politica publica  : ${politicaPublica} ')
print (f'Descuento por seguro social :  ${seguroSocial} ')
print (f'Descuento por seguro forzoso : ${seguroForzoso} ')
print (f'Descuento por caja de ahorro : ${cajaAhorro} ')
print (f'Monto total a pagar es de : ${montoPagar}')

"""
6. El periódico el Informador cobra por un aviso clasificado un monto
que depende del número de palabras, tamaño en cetímetros y
número de colores. Cada palabra tiene un costo de $20.000, cada
centímetro tiene un costo de $15.000 y cada color tiene un costo de
$25.000. Realice un algoritmo que determine el monto a pagar por un
aviso clasificado.
"""
numeroPalabra = int (input ('Digite el numero de palabras : '))
tamañoCentimetro = float (input ('Digite el tamaño en centimetro : '))
numeroColores = int (input ('Digite el numero de colores : '))
costoPalabra = numeroPalabra * 20000
costoCentimentro = tamañoCentimetro * 15000
costoColor = numeroColores * 25000
totalPagar = costoPalabra + costoCentimentro + costoColor
print (f'El costo total a pagar es de : ${totalPagar} ')

"""
7. Una empresa paga a sus empleados un bono por antigüedad que
consiste en $100.000 por el primer año laboral y $120.000 por cada
año siguiente. Realice un algoritmo que determine el monto del bono
a pagar a un trabajador que tiene varios años en la empresa.
"""
añoLaborando = int (input ('Digite el numero de años laborando en la empresa : '))
montoBono = añoLaborando * 120000 - 20000
print (f'El monto del bono es de : ${montoBono} ')

"""
8. Una Universidad le paga a sus profesores $20.000 la hora y le hace
un descuento del 5% por concepto de caja de ahorro. Determine el
monto del descuento y el monto total a pagar al profesor.
"""
cantidadHora = int (input ('Digite la cantidad de horas : '))
pago = 20000 * cantidadHora
interes = pago * 0.05
totalPago = pago - interes
print(f'El valor a pagar al profesor es de : ${totalPago: ,}')

"""
9. Un centro de comunicaciones alquilan tarjetas para realizar llamadas
y cobran el monto consumido de la tarjeta mas un recargo del 20%.
Teniendo como dato de entrada el monto inicial y el monto final de la
tarjeta, determine el costo de la llamada.
"""
montoInicial = float (input ('Digite el monto inicial : $ '))   
montoFinal = float (input ('Digite el monto final : $ ')) 
montoPagar = (montoInicial - montoFinal)/0.20
print (f'El monto a pagar es de : ${montoPagar}')              

"""
10. En una fototienda cobran por el revelado de un rollo $1.500 por cada
foto. Realice un algoritmo que determine el monto a pagar por un
revelado completo sabiendo que adiconalmente le cobran el IVA
(16%).
"""
numeroFoto= int(input('Digite el numero de fotos : '))
cadaFoto = 1500 * numeroFoto
adicionIvan = cadaFoto * 0.16
totalPago = cadaFoto + adicionIvan
print(f'El valor a pagar es de : ${totalPago} ')

"""
11. En un hospital existen tres áreas: Ginecología, Pediatría y
Traumatología. El presupuesto anual del hospital se reparte
conforme a la siguiente tabla:
"""
presupuestoAnual = float (input('Digite el presupuesto anual : $ '))
ginecologia = presupuestoAnual * 0.40
traumatologia = presupuestoAnual * 0.30
pediatria = presupuestoAnual * 0.30
print (f'La cantidad que recibira el area de ginecologia es de : ${ginecologia} ')
print (f'La cantidad de dinero que recibira el area de traumatologia es de : ${traumatologia} ')
print (f'La cantidad de dinero que recibira el area de pediatria es de : ${pediatria} ')

"""
12. Una video tienda alquila DVD a $1.500 el día. Tiene una promoción
que consiste en dejar gratis el alquiler de una película. Realice un
algoritmo que teniendo como dato de entrada el total de películas
alquiladas, y el número de días de alquiler, determine el monto a
pagar.
"""
peliculasAlquiladas = int(input('Digite el numero de peliculas : '))
numeroDias = int(input('Digite el numero de dias: '))
totalPago= peliculasAlquiladas * numeroDias * 1500
print (f'El valor a pagar es de : ${totalPago}')

"""
13. Una Agencia de viajes cobra por un Tour a Cartagena $25.000
diarios por persona. Realice un algoritmo que determine el monto a
pagar por una familia que desee realizar dicho Tour sabiendo que
también cobran el 12% de IVA.
"""
numeroPersonas = int (input ('Digite el numero de personas : '))
pago = 25000 * numeroPersonas
interes = pago * 0.12
totalPago = pago + interes
print (f'El total del pago es de ${totalPago} ')

"""
14. Un Hotel 5 Estrellas de Santa Marta tiene una promoción para sus
clientes. Cobra por una habitación $100.000 el primer día y por el
resto $200.000 por día. Realice un algoritmo que determine el valor
total a pagar por la habitación si la estadía fue de varios días.
"""
numeroDias = int(input('Digite el numero de dias: '))
totalPagar = numeroDias * 200000 - 100000
print(f'El valor a pagar es de : ${totalPagar}')

"""
15. El banco del Pueblo da microcréditos a empresarios para ser
cancelados en un lapso de 2 años (24 meses). Al monto del
préstamo se le cobra un interés del 24%. El empresario debe pagar
la mitad del préstamo en 4 cuotas especiales y la otra mitad en 20
cuotas ordinarias. Realice un algoritmo que teniendo como dato de
entrada el monto del préstamo, determine el monto total a pagar por
el préstamo, el monto de las cuotas especiales y el monto de las
cuotas ordinarias.
"""
montoPrestamo = float (input ('Digite el monto a prestar : $ '))
interes = montoPrestamo * 0.24
totalPrestamo=interes+montoPrestamo
cuotaEspecial = (totalPrestamo/2)/4
cuotaOrdinaria = (totalPrestamo/2)/20 
print (f'El monto total a pagar es de  : ${totalPrestamo} ')
print(f'El monto de cuota especial a pagar es de : ${cuotaEspecial} ')
print (f'El monto de la cuota ordinaria es de: ${cuotaOrdinaria}')