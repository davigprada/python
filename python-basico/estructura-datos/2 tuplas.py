#Para crear tuplas usamos () y separamos con ,
# () es opcional pero es una buena práctica usarlo.
tupla = (1, 2, 3) 
print(type(tupla)) #<class 'tuple'>

tupla2 = 'hola', 'carebola'
print(type(tupla2)) #<class 'tuple'>

print(tupla, tupla2)

#Operaciones con tuplas

#Convertir una lista en tupla
lista = [1, 2, 3]
tupla = tuple(lista)
print(type(tupla)) #< class 'tuple'>
print(tupla) # (1, 2, 3)


#Iterar una tupla con For
tupla = ('David', 'es un', 'crack.')
for i in tupla:
    print(i)


#Asignar el valor de una tupla
#   con n elementos a n variables.
tupla = (1, 2, 3)
v1, v2, v3 = tupla
print(f'{tupla} : Tupla')
print(f'{v1}, {v2}, {v3} : Nuevos valores')

print('')

navegadores = ('google', 'bing', 'safari')
navegador1, navegador2, navegador3 = navegadores
print(f'{navegadores} : Tupla')
print(f'{navegador1}, {navegador2}, {navegador3} : Nuevos valores')


#-----------------------------------------------------------------------------------------------#

#Métodos de tuplas

valores = (0, -1, 2.5, 'Hola', True, 'Te amo bro', True)

# count(obj) -> Cuenta las veces que el objeto está en la tupla
valor1 = valores.count(True)
print(valor1) #Se pueden guardar el print en una variable.

# index(obj) 
print(valores.index('Hola'))


#For con tuplas break y continue

tupla = ('Hola', 'cómo estás', 'haha', '¡chao!')
for i in tupla:
    if i == 'haha':
        continue #break
    print(i)
print('Programa Finalizado')