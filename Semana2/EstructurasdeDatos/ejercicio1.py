"""Crear un diccionario con los nombres de tres frutas y sus respectivos precios y
mostrar el diccionario completo"""

verduras={'Cebollas' : 350, 'Morrones':800, 'Papa': 250 }

print('Precios de las Verduras por Kg: ')

#Mosntrando diccionario con for

for verdura,precio in verduras.items():
    print(f'Verdura:{verdura}, Precio(kg):{precio}')