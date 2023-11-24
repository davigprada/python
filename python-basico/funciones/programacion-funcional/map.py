'''
La función de map() es hacer transformaciones a una
lista dada de elementos haciendo uso de otra función.

La función map toma dos entradas:

-> Una lista o iterable que será modificado en una nueva.
-> Una función, que será aplicada a cada uno de los elementos de la lista o iterable anterior.

Nos devuelve una nueva lista donde todos y cada uno de los elementos
de la lista original han sido pasados por la función.

Sintaxis
map(funcion_a_aplicar, entrada_iterable)

'''

lista = [1, 2, 3, 4, 5] #lista o iterable
def por_dos(x): #función
    return x * 2

               #list(map(función, iterable))
lista_pordos = list(map(por_dos, lista)) 
print(lista_pordos) #[2, 4, 6, 8, 10]

#También podemos hacer uso de funciones lambda aplicando la función map()
numeros = [6, 7, 8, 9, 10]
numbers = list(map(lambda i : i * 2, numeros))
print(numbers) #[12, 14, 16, 18, 20]


#map() es una herramienta que te permite aplicar una función a todos los elementos de una lista/iterable.

#---------------------------------------------#

nombres = ['david', 'felipe', 'andrea', 'sofia'] #lista/iterable
def convertir_a_mayúsculas(nombre): #función
    return nombre.upper()

                      #list(map(función,                iterable))
nombres_enmayuscula = list(map(convertir_a_mayúsculas, nombres))
print(nombres_enmayuscula)


nombres_v222 = list(map(lambda n : n.upper(), nombres)) #lambda function
print(nombres_v222)

#Haciendo uso de map() y lambda functions

sin_elevar = [12, 31, 45, 10, 90]
elevado = list(map(lambda x : x**2, sin_elevar))
print(elevado)


palabras = ['hola', 'me', 'llamo', 'david']
contar = list(map(lambda oracion : len(oracion), palabras))
print(contar)


decimales = [2.66, 4.11, 21.6, 1.9329]
redondeado = list(map(lambda x : round(x), decimales))
print(redondeado)


#📝 map() funciona como un bucle for, sin embargo, no reemplaza su uso.


#map() & diccionarios


items = [
    {
        'producto': 'camisa',
        'precio': 100
    },
    {
        'producto': 'pantalon',
        'precio': 200
    },
    {
        'producto': 'zapatos',
        'precio': 350
    }
]

precio = list(map(lambda item : item['precio'], items))
print(precio) #[100, 200, 350]

#agregar un nuevo atributo a la lista de diccionarios
def add_taxes(item):
    copia_items = item.copy() #para evitar overwriting, creamos una copia del array original
    copia_items['taxes'] = item['precio'] * .19
    return copia_items

new_items = list(map(add_taxes, items))
print(new_items)
