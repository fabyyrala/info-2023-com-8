"""'''Trabajas en una empresa X donde sus vendedores cobran comisiones del 6% de
sus ventas totales y el departamento comercial te solicita que ayudes a los
vendedores a calcular sus comisiones creando un programa que les pregunte su
nombre y cuánto han vendido en éste mes.
Tu programa le va a responder con una frase que incluya su nombre y el monto
que le corresponde por las comisiones
'''"""

nombre=input('Ingrese Nombre: ')
monto=float(input('Ingrese monto total de ventas mensuales: '))
print(f' Nombre: {nombre}\n Monto Total de Ventas Mensuales: ${monto}\n Comisión: ${round(monto*0.06,2)} ')