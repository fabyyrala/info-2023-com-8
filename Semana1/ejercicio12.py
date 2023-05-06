"""Escribe un programa que solicite al usuario su fecha de nacimiento en formato
dd/mm/aaaa y luego imprima su edad en años.
Utiliza la función .split()"""

actual=input('Ingrese la fecha Actual con el siguiente formato dd/mm/aa : ')
fecha=input('Ingrese su fecha de nacimiento con el siguiente formato dd/mm/aaaa: ')

lista1=actual.split("/")
lista2=fecha.split("/")

print(f'Tu edad es de: {int(lista1[2])-int(lista2[2])} años')