print('-----ANALIZADOR DE TEXTO-----')
texto=input('Ingrese un texto: \n')
letras= set()

contPython=0
ind=-1
band1=1
band2=0


#Letras para analizar

print("Ingrese letras a buscar en el texto(No Ingrese letras repetidas)")
while len(letras) < 3:
        letra=input('Ingrese una letra: ')
        
        if len(letra)==1 and band1==1:
            letras.add(letra)
            band1=0
        #Marca si la letra es una palabra o si esta repetida y lo añade 
        
        if len(letra)==1 and (not letra in letras):
            letras.add(letra)
        #else:
             #print('LETRAS GUARDADAS, ingrese una letra para buscar en el texto o una letra que no este en el texto')#print que sirve para confirmar que se guardaron las 3 letras en el array


# ---Consigna 1: Cantidad de veces que aparece cada una de letras que eligió---#

contLetras=0
for letraConj in letras:       #letraConj se refiere a las letras elementos del conjunto de letras
    for letraText in texto:    #ñetraText se refiere a las letras  de cada caracter individual del texto
        if letraConj.lower()==letraText.lower():
            contLetras+=1
    else:
        print (f'La letra {letraConj} apareció {contLetras} veces.')
        contLetras=0


#----Consigna 2: Cuantas palabras hay en total en todo el texto.----#

contPalabra=texto.split()
print(f'La cantidad de palabras totales del texto son:  {len(contPalabra)}')


#---Consigna 3: Cual es la primera letra y cuál es la última. (Indexación)---#

print (f'La primera letra del texto es: {texto[0]}\nLa ultima letra del texto es: {texto[-1]}')


#---Consigna 4: Mostrar el texto en orden inverso.---#

for i in range(len(texto)):
    print(f'{texto[ind]}',end='')
    ind-=1
else:
     print('\n')



#---Consigna 5:Decir si la palabra "python" aparece en el texto. ---#

for palabra in contPalabra:
    if palabra.lower()=='python':
        print ('La palabra \"PYTHON\" aparece en el texto"')
        band2=1
        break
if band2!=1:
    print ('La palabra \"PYTHON\" NO aparece en el texto"')