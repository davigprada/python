diccionario = {
    'Nombre': 'David',
    'Edad': 19,
    'Altura': 1.68,
    '¿Soltero?': True,
}

#Accediendo a los elementos de keys 
print(diccionario['Nombre']) #David
print(diccionario.get('Edad')) #19

# #Modificando el valor de una key
diccionario['Nombre'] = 'Gonzalo'
print(diccionario)


#Añadiendo nueva key
dic = {
    'First': 'Python',
    'Second': 'Java',
}
dic['Third'] = 'Ruby'
print(dic)

# --------------------------------------------------

#Iterando diccionarios con ciclos

#Imprimir las keys del diccionario con For:
for i in diccionario:
    print(i)
#Nombre, Edad, Altura, ¿Soltero?


#Imprimir solos los valores de las keys.
for i in diccionario.values():
    print(i)
#David, 19, 1.68, True


#Imprimir las keys y los varios a la vez.
for i in diccionario.items():
    print(i)


#-------------------------------------------------

#Diccionarios anidados

anidado1 = {'a': 1, 'b': 2,}
anidado2= {'c': 3, 'd': 4,}
d = {
    'anidado1': anidado1,
    'anidado2': anidado2,
}
print(d)



#Métodos de diccionarios

#Método clear()
d = {'hola': 'chao'}
print(d.clear()) #None

#Método get()
print(diccionario.get('Edad'))

#Método pop()
print(diccionario.pop('¿Soltero?'))
print(diccionario) #Elimina el value de Soltero

#Método popitem()
print(diccionario.popitem())
print(diccionario) #Elimina random

#Método update()
d1 = {'n1': 1, 'n2': 2, 'n3': 2}
d2 = {'n3': 3, 'n4': 4, 'n5': 5,}
d1.update(d2) 
print(d1) # 'n3': 2 -> 'n3'-> 3


#Método items()
#Imprime las keys y los values.
print(diccionario.items())

#Método values()
#Imprime los values.
print(diccionario.values())

#Método keys()
#Imprime las keys.
print(diccionario.keys())