"""Escribe un programa que solicite al usuario su peso y su altura, y luego calcule
e imprima su índice de masa corporal (IMC).
La fórmula para calcular el IMC es: IMC = peso / (altura ** 2)."""

print('Calculando ICM(Indice de Masa Corporal)')
nombre=(input('Ingrese su nombre: '))
altura=float(input( 'Ingrese su altura en mts: '))
peso=float(input('Ingrese su peso en kg:  '))

print(f'{nombre} , {altura} mts , {peso} kg , su ICM es de : {round(peso/(altura**2),2)} ')