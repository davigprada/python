#practica for

""" pares = []
for n in range(0,21):
    if n%2==0:
        pares.append(n)
print(pares)

for i in range(2, 21, 2):
    print(i)


num_par = [n for n in range(0,21,2)]
print(num_par)
 """

lista = [10, 23, 56, 78, 90]
suma = 0
for numero in lista:
    suma += numero
#print(suma)



""" cadena = "ejemplo de cadena"
conteo = 0
for letra in cadena:
    if letra == "a":
        conteo += 1
print(conteo)

contando = sum( 1 for letra in cadena if letra =='a')
print(contando)
 """


#asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']


#1
""" for i in asignaturas:
    print(f'Yo estudio ' + i)
 """

#2 LO HICE BIEN✅
""" print('Digita la nota que has sacado en cada asignatura ')
notas_asignaturas = {
    'Matemáticas' : input('Matemáticas, nota: '),
    'Física' : input('Física, nota: '),
    'Química' : input('Química, nota: '),
    'Historia' : input('Historia, nota: '),
    'Lengua' : input('Lengua, nota: ')
}
for asignatura, nota in notas_asignaturas.items():
    print(f'En {asignatura} has sacado {nota}') """


numbers = [35, 16, 10, 34, 37, 25]
even_numbers = []
for number in numbers:
  if number % 2 == 0:
    even_numbers.append(number)
#print('v1 =>', even_numbers)


even_numbers = [n for n in numbers if n%2==0]
#print(even_numbers)

def saludar():
    print('hola')

#saludar()



def area_rectangulo(base, altura):
   return base * altura

resultado = area_rectangulo(25, 10)
#print(resultado) #250
   

def cuadrado(x):
   return x**2
r = cuadrado(4)
#print(r) #16


def tipo_de_numero(n):
   if n > 0:
      return 'positivo'
   elif n < 0:
      return 'negativo'
   else:
      return 'cero'

tipo = tipo_de_numero(3)
#print(tipo) #positivo

def promedio(lista):
   return sum(lista) / len(lista) 

n = promedio([3,5,6,8])
#print(n)

def celsius_a_fahrenheit(celsius):
   return (celsius * 9/5) + 32
resul = celsius_a_fahrenheit(5)
#print(resul)#41.0



""" 
def message_creator(text):
   if text.lower() == 'computadora':
      return 'Con mi computadora puedo programar usando Python'
   elif text.lower() == 'celular':
      return 'En mi celular puedo aprender usando la app de Platzi'
   elif text.lower() == 'cable':
      return '¡Hay un cable en mi bota!'
   return 'Artículo no encontrado'
   
text = input('¿Computadra, celular o cable? ')
response = message_creator(text)
print(response) """



