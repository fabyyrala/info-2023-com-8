"""Escribe un programa que solicite al usuario dos palabras y luego las imprima
en orden inverso.
Por ejemplo, si el usuario ingresa "hola" y "mundo", el programa debe imprimir
"mundo hola".
Importante!!! Utiliza un solo print() 😈.
'''"""

palabras=input('Ingrese dos palabras: ')
pa1, pa2=map(str, palabras.split(' '))
print(pa2 +' '+ pa1)
