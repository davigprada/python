
'''
Errores en Python

Hay dos tipos diferentes de errores: errores de sintaxis y excepciones.

👇 
Los errores de sintaxis, también conocidos como errores de interpretación,
son quizás el tipo de queja más común que tenés cuando todavía estás aprendiendo Python.

#saludar print('Hola mundo') -> SyntaxError: invalid syntax


👇
Las excepciones en python son una forma de controlar el
comportamiento de un programa cuando se produce un error.

Esto es muy importante ya que salvo que tratemos este error, el programa se parará,
y esto es algo que en determinadas aplicaciones no es una opción válida.

Existen muchos tipos de Excepciones integradas en Python, puedes consurtarlas aquí:
https://www.w3schools.com/python/python_ref_exceptions.asp


👇
Así como también existen excepciones integradas en Python,
podemos de igual forma crear nuestras propias excepciones
haciendo uso de 👉 raise Exception(" ")

'''

#Lanzar una excepción propia con raise
age = int(input('¿Cuál es tu edad? '))
if age < 18:
    raise Exception('No se permiten menores de edad')
else:
    print('¡Puedes ingresar!')


#Otra forma de crear excepciones
a = 5
b = 0
#raise ZeroDivisionError('No se puede dividir entre 0 pelotudo!')
c = a/b




'''

La buena noticia es que las excepciones pueden ser capturadas
y manejadas adecuadamente, sin que el programa se detenga.🔥

'''






""" while True:
    try:
        x = int(input("Please enter a number: "))
        print('Well done! The number is:',x)
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...") """

