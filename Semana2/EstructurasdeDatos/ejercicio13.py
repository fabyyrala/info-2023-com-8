'''Crear una lista con los nombres de tres colores y agregar dos colores más al
final de la lista. Mostrar la lista resultante'''

colores=[]

for i in range(3):
    color=input('Ingrese un color:')
    colores.append(color)

else:
    print('Lista de colores ingresados:')
    for color in colores:
        print(color)
    
    for i in range(2):
        color=input('Agregar un color:')
        colores.append(color)

    print('Lista de colores agreando 2 colores extras:')
    for color in colores:
        print(color)