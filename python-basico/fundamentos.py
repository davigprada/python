
#FUNDAMENTOS DE PYTHON

#Esto es un comentario
'''Esto es un comentario
con salto de línea'''



#Variables
nombre_variable = 'contenido de la variable'


#Tipos de datos
nombre = 'David'
apellido = 'Prada' #Datos string

edad = 20 #Dato integer
estatura = 1.68 #Dato float
soltero = True #Dato boolean

numero_grande = 1e6
#print(numero_grande)

#Concatenación de datos
#print(f'Mi nombre es {nombre} {apellido} y tengo {edad} años.')
#print('¿Estás soltero? ')
#print(soltero)

#números
vidas = 4
vidas = 3 #Se reemplaza el valor de 4 por 3. 
vidas = vidas - 1  #Se resta -1 a la variable vidas. Quedaría 2.
vidas -= 1 #Forma abreviada de restar -1 a la variable vidas. Quedaría 1.
vidas += 5 #Se suman (agregan) 5 vidas más a la variable vidas. Quedaría 6.
#print(vidas)

#💡
#number = print(0.00000000005)
#print(type(number)) #5e-11 <class 'NoneType'>


#Transformación de tipos
edad = 20
#print('Mi edad es '+str(edad)) #Usar Str para convertir el dato a string.
#print(f'Mi edad es {edad}') #La función format -> f({variable}) manipula todo como un string.

#nueva_edad = input('¿Cuál es tu edad? ')
#print(f'Tu edad en 10 años será {int()+10} años')


#Operadores de Pertenencia
a = [1,2,3,4,5]
#print(5 in a) #Está 5 en la lista a? #True
#print(12 not in a) #No Está 12 en la lista a? #True

#Comparación de números flotantes

a = 3.3
b = 1.1  + 2.2
#print(b) #3.300000000003
#print(round(b,1)) #3.3
#print(a == b) #False ¿Qué hacer para que sean 
b_string = format(b, '.2')
#print(b_string)
#print(str(a) == b_string)



#CONDICIONALES
""" n = int(input('Digita un número: '))
if n % 2 == 0:
    print('par')
else:
    print('impar') """


#PIEDRA, PAPEL O TIJERA
""" usuario = input('Elige piedra, papel o tijera: ').lower() #Se usan metodos para evitar errores
compu = 'papel'

if usuario == compu:
    print(f'Elegiste {usuario} y la computadora eligió {compu}')
    print('Empate')
elif usuario == 'tijera':
    print(f'Elegiste {usuario} y la computadora eligió {compu}')
    print('Ganaste')
else:
    print(f'Elegiste {usuario} y la computadora eligió {compu}')
    print('Perdiste') """



#Metodos de String
""" pizza = 'hawAiNa en caSa'

print(len(pizza)) #cantidad de carácteres - 15

print(pizza.lower()) #minúsculas
print(pizza.upper()) #mayúsculas

print(pizza.capitalize()) #primera en mayúscula
print(pizza.title()) #transforma el inicio de cada palabra en mayuscula

print(pizza.isdigit()) #Pregunta si es un numero -False 
print(pizza.swapcase()) #transforma los caracteres al contrario de minus o mayus

print(pizza.count('a')) #cuenta la cantidad del caracter específicado.
print(pizza.startswith('h')) #pregunta si un texta inicia con X caracter -True 

print(pizza.endswith('a')) #pregunta si un texta finaliza con X caracter -True 
print(pizza.replace('hawAiNa','peperoni')) #reemplaza un caracter por el que se asigne -peperoni """

''' Y existen muchos más métodos de strings. Es importante aclarar que algunos métodos
    hacen transformaciones de carácteres y otros retornan valores booleanos.'''


#INDEXING y SLICING

""" palabra = input('Escribe un palíndromo: ')
espalindromo = palabra[0:] and palabra[::-1]

if espalindromo == palabra:
    print('Es palindromo.')
else:
    print('No es palindromo.') """


#LISTAS
#VER NOTAS DE CODING-PYTHON/CODIGOFACILITO
'''METODOS DE LISTAS NO VISTOS
- pop(): Extrae un ítem de la lista y lo borra.
- reverse(): Le da la vuelta a la lista actual.
'''

#TUPLAS
""" tupla = 'David', 'Prada'
new_tupla = tupla[::-1]
#print(new_tupla)

#DICCIONARIOS
my_dict = { }
print(my_dict)

diccionario = {
#    {KEY} :   {VALUE}
    'Marca': 'Chevrolet',
    'Año': '2020',
    'Estado': ['En buen estado','Checar llantas'],
    'A la venta': True
}
print(diccionario)

#Modificar elementos.
nueva_marca = diccionario['Marca'] = 'Ford'
print(diccionario) #Se reemplaza/actualiza 'Chevrolet' por 'Ford'.

#Uso de in para saber sí una {KEY} está dentro del diccionario.
print('Estado' in diccionario) #True --->No aplica para los valores.

#METODOS DICCIONARIOS
#metodo append()
diccionario['Estado'].append('Fijar retrovisores')
print(diccionario) """


#CICLO WHILE
#FORMA BÁSICA #1
""" continuar = 'sí'
while continuar == 'sí':
    continuar = input('¿Desea continuar con el programa? ')
    print('¡Hasta la vista!')

#FORMA BÁSICA #2 CON CONTADOR.    
contador = 0
while contador < 10:
    contador +=1
    print(contador) """


#CICLOR

""" lista = [20, 15, 40, 24]
for i in lista:
    print(i) """



