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


