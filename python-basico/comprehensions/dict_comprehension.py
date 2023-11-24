

'''
La sintaxis de una comprensión de diccionario es
    {clave: valor for elemento in iterable}
'''

#Forma normal
diccionario = {}
for i in range(1,6):
    diccionario[i] = i * 2
#print(dict)

#Comprensión de diccionario
        #clave:valor - elemento - iterable
new_dict = {i : i * 2 for i in range(1,6)}
#print(new_dict)



asignaturas = ['matemáticas', 'fisica', 'quimica']
notas = [20, 41, 64]
dicc = {}
#Forma dict comprehension
notas_asignaturas = {asignatura : nota for (asignatura, nota) in zip(asignaturas, notas)}
#print(notas_asignaturas)
#Usamos la función incorporada zip() para combinar elementos de varias secuencias (listas,tuplas, etc.)

#Forma dict() con zip()
n_asig = dict(zip(asignaturas, notas))
#print(n_asig)


#Otra forma
new_notas = {asignaturas[i]:notas[i] for i in range(len(asignaturas))}
#print(new_notas)



#------------------#
#Dictionary comprehension: condition

                #Llave:Valor                     #condicion opcional para filtrar   
#Su sintaxis es-> {key:value for var in iterable if condition}

cuadrados = {n:n**2 for n in range(0,11) if n % 2 == 0}
#print(cuadrados)

frutas = ['manzana', 'pera', 'melocotón', 'piña']
longitudes = {fruta : len(fruta) for fruta in frutas if len(fruta) > 5}
#print(longitudes)

numeros = [3, 6, 9, 12, 15]
filtrados = {n : n for n in numeros if n > 5 }
#print(filtrados)

words = ['apple', 'banana', 'green', 'avocado', 'cherry']
start_with_a = {word : len(word) for word in words if word.startswith('a')}
#print(start_with_a)

#1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impares = {n:n**2 for n in numbers if n % 2 != 0}
#print(impares)

#2
impares_v2 = {n:n**2 for n in range(0,11) if n % 2 != 0}
#print(impares_v2)





