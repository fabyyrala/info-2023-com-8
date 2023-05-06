"""Escribe un programa que solicite al usuario un número decimal y luego
imprima la parte entera y decimal por separado."""

numero= (input('Ingrese un numero decimal: '))
lista=numero.split("."or ",")
print(f'Parte entera; {lista[0]}, Parte decimal: {lista[1]}')