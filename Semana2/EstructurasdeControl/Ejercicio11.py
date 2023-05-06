'''Escribir un programa que pida al usuario dos números y muestre por pantalla
la suma de ellos solo si ambos son pares.'''

num1=int(input('Ingrese el primer numero: '))
num2=int(input('Ingrese el segundo numero: '))

if num1%2==0 and num2%2==0:
    print(f'La suma de {num1} y {num2} es de : {num1+num2}')
else: 
    print(f'La suma no se puede realizar debido a que {num1} o {num2} no es PAR ')