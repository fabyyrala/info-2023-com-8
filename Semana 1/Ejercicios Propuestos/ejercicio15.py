"""Escribe un programa que solicite al usuario una temperatura en grados
Celsius y luego imprima la temperatura equivalente en grados Fahrenheit.
La fórmula para convertir de Celsius a Fahrenheit es: F = (C * 1.8) + 32."""

temperatura=round(float(input ('Ingrese temperatura en centigrados: ')),2)
print(f'La temperatura {temperatura} °C en farenheit es de : {temperatura*1.8+23}  ')