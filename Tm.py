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

