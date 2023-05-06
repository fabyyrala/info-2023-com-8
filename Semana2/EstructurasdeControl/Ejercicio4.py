"""Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por
pantalla si está aprobado (5 o más) o no"""

nota=float(input('Ingrese nota del examen de (0 a 10):'))
print('El alumno APROBO') if nota>=5.0 else print('El alumno DESAPROBO')