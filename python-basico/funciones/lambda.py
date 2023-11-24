
'''
Funciones lambda

Son funciones anónimas o sin nombre que se utilizan para
definir funciones pequeñas y simples en una línea de código. 

La sintaxis de una función lambda es

   < lambda argumentos: expresión >

👉 lambda: La palabra clave utilizada para definir una función lambda.
👉 argumentos: Los argumentos que la función lambda tomará.
👉 expresión: La expresión que se evaluará y devolverá como resultado.
'''

#
#lamb arg : expr
lambda x : x + 1

'''
Las funciones lambda son especialmente útiles cuando se utilizan
con funciones de orden superior como map, filter y reduce.

También se usan comúnmente en list comprehension
y en situaciones donde necesitas una función rápida y sencilla.
'''


#Imprimir usando una variable
#<funcion   lambda arg : expr>
my_funcion = lambda x : x ** 2
#print(my_funcion(4))

#Imprimir de forma directa sin variable
#print((lambda y : y ** 3)(3)) #Donde 3 es el valor de y


full_name = lambda name, last_name : f'mi nombre completo es {name.title()} {last_name.title()}'
text = full_name('david gonzalo','gelves prada')
#print(text)


#Imprimir el número mayor
mayorque = lambda n1,n2 : n1 if n1 > n2 else n2
resultado = mayorque(4,6)
#print(resultado)

#
filtrar_numeros = lambda lista : [x for x in lista if x % 2==0]
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = filtrar_numeros(numeros)
#print(numeros_pares)

#
mayus = lambda lista : [name.upper() for name in lista]
nombres = ['david', 'felipe', 'andrés']
nombres_v2 = ['juan', 'gonza', 'luis']
resultado = mayus(nombres) + mayus(nombres_v2)
print(resultado)
