#Saber si número es par con mod -> % en Python.
"""
number = int(input("Ingresa un número: "))
if number % 2 == 0:
    print('Este número es par')
else:
    print('Este número es impar')"""


"""
#Saber sí un número es par sin mod -> % en Python. (FORMA AVANZADA CON EL OPERADOR LÓGICO AND)
number = int(input('Ingresa un número: '))
if number & 1 == 0:
    print('Este número es par')
else:
    print('Este número es impar')
"""



name = input('Hola, ¿cómo te llamas? ')
number = int(input(f'{name}, escribe un número: '))
number % 2 == 0
if number in range(2,5):
    print('Este número par es Not Weird😎')
elif number in range(6,20):
    print('Este número par es Weird😛')
elif number > 21:
    print('Este número par es Not Weird😎')
else:
    print('Este número impar es Weird😛')
    