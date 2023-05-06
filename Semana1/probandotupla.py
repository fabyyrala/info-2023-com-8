b=0
tupla=([1,2],90,b)
print(tupla)
tupla[0].append(32)#busco la posicion 0 que es la lista y agrego el valor 32
print(tupla)
tupla[0].pop(1)# se ubica en la lista y dentro de la lista busca posicion 1 y saca el elemento de la posicion 1
print(tupla)

tupla=([1,2], 90 ,['2','43'])
tupla[2][1]=44 #se posiciona en la posicion 2 de la tupla donde esta la lista y dentro de la lista va a la posicion 1
               # tupla[2] -> ['2', '43'][1]-> '43'
print(tupla)

suma= tupla[0][0] + tupla[2][1]
print(suma)

suma = tupla[0][0]+ int(tupla[2][1])
print('suma de verdad',suma)