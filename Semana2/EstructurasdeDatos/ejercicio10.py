'''Crear una lista con los nombres de tres frutas y eliminar la segunda fruta de la
lista. Mostrar la lista resultante.'''

print('Ingrese 3 frutas')
frutas=[]
for i in range(3):
    fruta=input('Ingrese una fruta:')
    frutas.append(fruta)
else:
    print('Lista de Frutas:')
    for fruta in frutas:
        print(fruta)
    print('Lista de fruta eliminando la segunda fruta:')
    frutas.remove(frutas[1])
    for fruta in frutas:
        print(fruta)
