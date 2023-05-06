"""Escribir un programa que pida al usuario tres números y muestre por pantalla
el mayor de ellos.
'''"""

num1=int(input('Ingrese el primer numero: '))
num2=int(input('Ingrese el segundo numero: '))
num3=int(input('Ingrese el tercer numero: '))

if num1>num2 and num1>num3:
    print(f'{num1} es mayor que {num2} y {num3}')

elif num2>num1 and num2>num3:
    print(f'{num2} es mayor que {num1} y {num3}')

elif num3>num1 and num3>num2:
    print(f'{num3} es mayor que {num1} y {num2}')

else:
    print('No hay numero mayor')