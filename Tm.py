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
