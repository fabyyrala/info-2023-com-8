"""Crea un programa que pida al usuario el radio de un círculo y muestre su
diámetro, su circunferencia y su área.
Supón que pi es aproximadamente 3.14159"""

import math

radio=float(input('Ingrese radio del circulo:'))
print(f'El diametro del circulo es: {radio*2} ')
print(f'La circunferencia del circulo es: {2*math.pi*radio}')
print(f'El area del circulo es: {math.pi*radio**2}')