'''-Crear un set/conjunto con los números impares del 1 al 10 y mostrar el número
de elementos en el conjunto'''

conjunto1,conjunto2=set(),set()
conjunto1={1,2,3,4,5,6,7,8,9,10}

for numero in conjunto1:
    if numero%2==1:
        conjunto2.add(numero)
print(f'Numero de impares detectados: {len(conjunto2)}')
print(conjunto2)