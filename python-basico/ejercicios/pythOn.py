n1 = 3
n2 = 4
#print(n1+n2) #Suma
#print(n1-n2) #Resta
#print(n1%n2) #Se usa para obtener el residuo de una división.
#print(n1/n2) #División
#print(n1**n2) #Potencia
#print(n1//n2) #Se usa para obtener el cociente de una división.

#print(type(10))
#print(type(9.8))
#print(type(3.14))
#print(type(4-4j))
#print(type(['Asabeneh', 'Python', 'Finland']))
#print(type({'Asabeneh', 'Python', 'Finland'}))
#print(type(True))
#print(type('David'))

""" 
            Funciones Built-in
El intérprete de Python tiene una serie de funciones
y tipos incluidos en él que están siempre disponibles.
Están listados aquí en orden alfabético.
>> https://docs.python.org/es/3.9/library/functions.html
"""
#abs() -> Devuelve el valor absoluto.
#print(abs(-3)) #3

#All() #Devuelve True sí todos los valores de un iterable son True / De lo contrario False.
x = [True, True, False, -5]
#print(all(x)) #False

#Any(iterable) #Devuelve True sí un elemento cualquiera es True / De lo contrario False. (o está vacío).
x = {}
#print(any(x)) #False

#bin() Convierte un número entero a una cadena binaria con prefijo «0b»
bin(10)




#Variables

my_variable = 'My String Variable'
#print(my_variable) #snake_case

nombre, apellido, pais, edad, casado = 'David', 'Prada', 'Colombia', 20, False
#print(nombre, apellido, pais, edad, casado) #Declaración de varias variables en una línea. ¡No abusar de la sintaxis! 

'''
            Forzar el tipo de las variables.
Python es un lenguaje en ciertos casos debilmente típado,
pero que es realmente denominado un lenguaje de programación con tipado dinámico.
'''
direccion = str('Mi dirección')
direccion = 10
#print(direccion)
#print(type(direccion))


#Operadores Aritmeticos 
""" 
print(5 + 3)
print(5 - 3)
print(5 * 3)
print(5 / 3)
print(5 // 3)
print(5 % 3) 
print(5 ** 3)

Raiz cuadrada -> 3 formas.
1 forma
print(round(20**(0.5),2))
#2 forma
import math
print(round(math.sqrt(20),2))     #En las 3 formas uso la función round(n,2) para redondear el resultado a 2 decimales.
#3 forma
print(round(pow(20,0.5),2))

#Multiplicando strings
print('David ' * 5)
"""

#Operadores Relacionales

"""
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)
 """

#Compara la ordenación alfabética (teniendo en cuenta mayus-minus) por ASCII.
"""
print('Hola' > 'Python')
print('Hola' < 'Zola')
print('Hola' >= 'Ola')
print('Hola' <= 'zola')
print('Hola' == '')
print('Hola' != 'Python')
 """

#Operadores Lógicos

"""
print(True and True) # True
print(False and True) # False
print(True or True) #  True
print(False or True) # True
print(not True) # False
print(not False) # True
"""


#Strings
my_string = 'David es una persona increíble.'

x = len(my_string)
#print(f'La cantidad de caracteres dentro de "{my_string}" es: {x}')
#len() -> Devuelve la longitud de un objeto (lista, una cadena, una tupla o un diccionario).


#Salto de línea // Para hacer slash inverso es <<alt gr \>>.
#print('Este es un String con\nsalto de línea.')

#Salto de línea con tabulación.
#print('\tEste es un String con tabulación')


#Formas de concatenar // Formateo.

cargo = 'Estudiante'
edad = 25
estado = 'Soltero'

#print('El cargo de la persona es ' + str(cargo) + ', tiene ' + str(edad) + ' años y su estado civil es ' + str(estado) + '.')

#print('El cargo de la persona es {}, tiene {} años y su estado civil es {}'.format(cargo, edad, estado)) #(str.format)

#print('El cargo de la persona es %s, tiene %d años y su estado civil es %s.' %(cargo, edad, estado)) #(% Operator) Old Style.

#print(f'El cargo de la persona es {cargo}, tiene {edad} años y su estado civil es {estado}') """ #String Interpolation / f-Strings


#Desempaquetado de caracteres
           #012345
lenguaje = 'Python'
a, b, c, d, e, f= lenguaje
"""
print(a)
print(b)
print(c) 
print(d) 
print(e) 
print(f)
"""

#Slices

# [desde : hasta : saltos]
                # 12345678911234567892    1234567
nombre, estado = 'David G Gelves Prada', 'Soltero'
#print(nombre[::],estado[:0:])


          #01234
palabra = 'David'

n = palabra[0:2] + palabra[2:5]
#print(n)
#print(type(n))

#print(len(palabra))


#Listas

           #0    #1   #2   #3
lista = ['Hola', 20, 2.5, True]


listas = ['David',['Hola'],2]
#print(listas[::-1])


#Unir dos listas
new_lista = print(lista + listas)



#CASTING -> CONVERSIÓN DE DATOS.

""" n = 4500
nueva_n = str(n)
print(nueva_n) #'4500'
print(type(nueva_n)) #class 'str'


a = '50'
nueva_a = int(a)
print(nueva_a) #50
print(type(nueva_a)) #class 'int'


z = True
nueva_z = int(z) 
print(nueva_z) #1
print(type(nueva_z)) #class 'int' """





#Metodo split()
       #0    #1    #2
#print('Hola mundo mundo'.split()[1])
