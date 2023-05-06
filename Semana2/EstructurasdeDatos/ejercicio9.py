'''Crear una lista con los nombres de tres países y ordenar la lista en orden
alfabético. Mostrar la lista resultante.'''

paises=[]

for i in range(3):
    pais=input('Ingrese un pais:  ')
    paises.append(pais) #mete el pais ingresado en la lista paises

print('Lista Desordenada: ',end=' ')
for pais in paises:
    print(pais,end=' ')
    paises.sort()

print('\nLista ordenada:',end=' ')

for pais in paises:
    print(pais,end=' ')