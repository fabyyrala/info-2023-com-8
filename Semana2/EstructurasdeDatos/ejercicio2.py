"""Crear una lista con los nombres de tres ciudades y agregar una cuarta ciudad al
final de la lista."""

print('-----CIUDADES-----')
ciudades=['Presidencia Roque Saenz Peña','Corrientes','Obera']
for i in range(len(ciudades)):
    print(f'{ciudades[i]}',end=' ')

ciudadagregada=input('\nIngrese el nombre de la ciudad a agregar : ')
ciudades.append(ciudadagregada) 
for i in range(len(ciudades)):
    print(f'{ciudades[i]}',end=' ')  