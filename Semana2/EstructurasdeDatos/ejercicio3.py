"""Crear una lista con los nombres de tres países y mostrar el segundo país de la
lista''"""

print('----PAISES---')
paises=['Oslo','Argentina','Rusia']
for i in range(len(paises)):
    print(f'{paises[i]}',end=' ')

print(f'\nEl Pais en segunda posicion de lista es es: {paises[1]}')