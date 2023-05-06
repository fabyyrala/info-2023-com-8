'''-Crear una lista con los nombres de tres animales y agregar una cuarta animal
al principio de la lista. Mostrar la lista resultante'''

animales=[]
for i in range(3):
    animal=input('Ingrese un animal:')
    animales.append(animal)
else:
    print('Lista de animales:')
    for animal in animales:
        print(animal)
    animal=input('Agregar un animal mas:')
    animales.insert(0,animal)
    print('Lista de animales agregando un animal en primera posicion:')
    for animal in animales:
        print(animal)