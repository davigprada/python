'''

Un módulo en Python es un fichero.py que alberga un conjunto de
funciones, variables o clases y que puede ser usado por otros módulos.

¿Cómo utilizar un modulo?

import nombre_modulo 👉 Usando import podemos importar todo el contenido.

from nombre_modulo import suma, resta 👉 Podemos importar únicamente los componentes que nos interesen.

from nombre_modulo import * 👉 Podemos importar todo el módulo haciendo uso de *

'''


from math_operations import sumar, restar

a = 5
b = 3

print(sumar(a, b)) 
# Imprime 8

print(restar(a, b))
# Imprime 2

#👉 ¡Cualquier archivo en python puede ser un módulo! 👈


#Algunos modulos integrados de python


# 1- Modulo para el manejo del sistema
import sys
print(sys.path) #Ubicacion donde se ejecuta el archivo actual


# 2- Modulo de expresiones regulares
import re
text = 'mi núm es 321 123 531, el código del país es 57 y mi num de la suerte es 10'
#expresión regular que imprime SOLO los números de un texto
result = re.findall('[0-9]+', text)
print(result)


# 3- Modulo para el manejo de horas y fechas
import time

#Hora y fecha actual en el formato de la computadora
timestamp = time.time()
print(timestamp)

#Hora y fecha actual con formato de hora
local = time.localtime()
hora_actual = time.asctime(local)
print(hora_actual)


# 4- Modulo para el manejo de listas
import collections

#Frecuencia de los numeros de una lista en un diccionario
numbers = [1,2,4,5,5,5,7,1,3,8,5,5]
counter = collections.Counter(numbers)
print(counter)
