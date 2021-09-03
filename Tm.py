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
