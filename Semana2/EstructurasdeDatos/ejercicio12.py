'''rear una lista con los nombres de tres países y reemplazar el segundo país de
la lista por otro país. Mostrar la lista resultante.'''

paises=[]
for i in range(3):
    pais=input('Ingrese un pais:')
    paises.append(pais)
else:
    print('Lista de Paises:')
    for pais in paises:
        print(pais)
    paises[1]=input('Remplazar el segundo pais con:')
    print('Lista de Paises remplazando el segundo pais:')
    for pais in paises:
        print(pais)