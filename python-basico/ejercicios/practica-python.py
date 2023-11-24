""" nombre = input('¿Cómo te llamas? ')
altura = input('¿Cuál es tu altura? ')
peso = input('¿Cuánto estás pesando actualmente? ')
ano = input('¿En qué año estamos? ')

print(f'Ni nombre es {nombre}, mido {altura}, actualmente estoy pesando {peso}kg y estamos en el año {ano}.')

 """

""" import random
gorras_nike = random.randint(1, 500)
gorras_adidas = random.randint(1, 500)
resultado = gorras_nike - gorras_adidas

if gorras_nike > gorras_adidas:
    print(f'Hay {gorras_nike} gorras de marca Nike, por lo tanto hay más stock.')
else:
    print(f'Hay {gorras_adidas} gorras de marca Adidas, por lo tanto hay más stock.')
print(f'Hay {resultado} gorras de diferencia')
 """


""" def suma():
    resultado=a+b
    return resultado

a = int(input('Digita un número: '))
b = int(input('Digita otro número: '))

print(suma()) """

""" 
lista = ['Victor', 'Felipe', 'Andrés']

for i in lista:
    print('-' +i) """


""" def name(fname, lname):
    print(f'{fname}{lname}')
name('David ', 'Prada') """

""" import math
problema = ((3+2)/(2*5))**2
print(problema) """

""" htrabajadas =int(input('Horas totales de trabajo: '))
cxh = int(input('¿Cuál es el coste por hora? '))
pago = cxh*htrabajadas
print(f'Te corresponde de pago ${pago} pesos.') """


""" n = int(input('Digita un número: '))
suma = n * (n+1) / 2
#operacion = round(operacion, 0)
print(suma) """


#Calculando el IMC
""" peso = (input('¿Cuál es tu peso en kg? '))
estatura = (input('¿Cuál es tu estatura en metros? '))
imc = peso / estatura
imc = round(imc, 2)
imc = round(float(peso)/float(estatura)**2, 2)
print(f'Tu índice de masa corporal es {imc}' )
 """


""" #División calculando el cociente y el residuo.
n = int(input('Digita un número entero: '))
m = int(input('Digita otro número entero: '))
c = n//m ; r = n%m
print(f'{n} entre {m} da un cociente {c} y un resto {r}')
 """


""" #9
inversion = input('¿Cuánto dinero vas a invertir? ')
interes = input('¿Cuál es el interés anual? ')
t = input('Cantidad de años de la inversión: ')

capital = round(int(inversion)*(1+float(interes))**int(t),3)

print(f'El capital obtenido de la inversión después de {t} años es de {capital}') """



#10
""" num_payasos = int(input('Número de payasos vendidos: '))
num_munecas = int(input('Número de muñecas vendidas: '))
peso_payaso = 112
peso_muneca = 75
peso_total = (peso_payaso * num_payasos) + peso_muneca * num_munecas

print(f'El peso total del paquete enviado es {peso_total}')
 """


#11
""" 
inversion = float(input('Cantidad de dinero depositada: '))
i = 0.04
balance1 = inversion * (1 + i)
print(f'El balance tras el primer año es: {round(balance1, 2)}')
balance2 = balance1 * (1 + i)
print(f'El balance tras el primer año es: {round(balance2, 2)}')
balance3 = balance2 * (1 + i)
print(f'El balance tras el primer año es: {round(balance3, 2)}')
 """

#12

""" panVendido_noDia = int(input('Número de barras vendidas que no son del día: '))
#panVendido_dia = int(input('Número de barras vendidas del día: '))
descuento = 0.6
barra_pan = 3.49
descuento_aplicado = panVendido_noDia * (descuento * barra_pan)
print(f'El precio de la barra de pan son {barra_pan}€ \
y el descuento aplicado es del 60%. El coste total son {round(descuento_aplicado,2)}€')
 """


#----------------------------------------------------------------------------------------#

#Ejercicios de Cadenas

#Ejercicio 1
""" nombre = input('Escribe tu nombre: ')
n = int(input('Digita un número: '))
#print((nombre + '\n') * int(n)) FORMA #1

for n in nombre:
    print(nombre) #FORMA #2 """


#Ejercicio 2
""" nombre = input('Escribe tu nomnbre: ')
print(nombre.lower())
print(nombre.upper())
print(nombre.title()) """

#Ejercicio 3

""" nombre = input('¿Cuál es tu nombre: ')
n = len(nombre)
print(f'{nombre.capitalize()} tiene {n} letras')

#EJEMPLO DEL MÉTODO LEN()
mylist = ['david', 939, True]
print(len(mylist)) """

""" #Ejercicio #4
numero = input('Digita tu número de telefono +xx-xxxxxxxxx-xx: ')
print(f'El numero de telefono es {numero[4:-3:]}') 
 """
#01234567891123456
#+34-913724710-56


""" #Ejercicio #5
nombre = input('Cómo te llamas: ')
print(nombre[::-1])
"""

#Ejercicio #6
""" frase = input('Escribe una frase: ')
vocal = input('Escribe una vocal: ')
print(frase.replace(vocal, vocal.upper())) """

#Ejercicio #7
""" correo = input('¿Cuál es tu correo electrónico? ')
newCorreo = correo[:correo.find('@')] + '@ceu.es'
print(newCorreo) """

#Ejercicio #8
""" precio = (input('¿Cuál es el precio del producto en €? '))
#euros = precio[:precio.find('.')]
#print((f'{euros} euros.'))
#centimos = precio[precio.find('.')+1:]
#print((f'{centimos} céntavos.'))
print(precio[:precio.find('.')] + ' euros y',precio[precio.find('.')+1:]+ ' céntimos.') """

#Ejercicio #9
""" 
fecha = input('Escribe tu fecha de nacimiento en formato [dd/mm/aaaa]: ')
print('Naciste el día: ' + fecha[:2])
print('Del mes: ' + fecha[3:5])
print('Del año: ' + fecha[6:11])

#Un solo carácter
enero = 1
febrero = 2

dia = print('Naciste el día: '+fecha[:fecha.find('/')])
mes = int(fecha[fecha.find('/')+1:5]) #Se puede (+1,-2) cuando queramos obtener un caracter de los lados.
if mes == febrero:
    print('Del mes: '+'Febrero')
    #elif mes == marzo:
        #print('Del mes: '+'Marzo')
año = print('Del año: '+fecha[fecha.find('/')+4:]) """

#Ejercicio #10

""" cesta = input('Introduce los productos de la cesta de la compra separados por comas: ')
print('\n'.join(cesta.split('+'))) """
#\n permite hacer salto de linea 
#.join() Une todos los caracteres de una cadena utilizando un caracter de unión -> \n.
#.split(', ') Separa la cadena en subcadenas, quita las comas y espacios.



#Ejercicios de Condicionales

#Ejercicio 1
""" edad = int(input('Cuál es tu edad: '))
if edad >= 18:
    print('Mayor')
else:
    print('Menor') """

#Ejercicio 2
""" pw = 'contraseña'
password = input('Digita "contraseña": ')
if pw == password.lower():
    print('COINCIDE')
else:
    print('NO COINCIDE') """

#Ejercicio #3
""" n1 = int(input('Escribe un número: '))
n2 = int(input('Escribe un número: '))
if n2 == 0:
    print('ERROR')
else:
    print(n1/n2) """


#Ejercicio #4
""" n = int(input('Digita un número: '))
if n % 2 == 0:
    print(f'El número {n} es par')
else: 
    print(f'El número {n} es impar') """



#Ejercicio #5
""" edad = int(input('¿Cuántos años tienes? '))
ingresos_mensuales = int(input('¿Cuál es tu ingreso mensual? '))
if edad >= 16 and ingresos_mensuales >= 1000:
    print('Debes tributar')
else:
    print('No debes tributar') #Intenté con un if anidado, funciona en parte, pero no del todo bien. """


#Ejercicio 6
#PREGUNTA DE MIERDA

#Ejercicio 7

nombre = 'david'

segunda_letra = nombre[0:] + nombre[1].capitalize() + nombre[:]
print(segunda_letra)


#dAvid
#01



