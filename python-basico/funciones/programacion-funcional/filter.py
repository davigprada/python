

"""

La función de filter() se utiliza para filtrar elementos de una secuencia
(como una lista, tupla o iterable) según una función de filtrado dada. 

Sintaxis
filter(función_de_filtrado, iterable)

-> función_de_filtrado: Una función que toma un elemento de la secuencia
y devuelve True o False según la condición de filtrado.

-> iterable: El iterable de entrada que se va a filtrar.

filter() devuelve un objeto de tipo filter,
que es un iterador que puedes convertir en una lista,
tupla u otro tipo de secuencia para obtener los resultados filtrados.

"""

my_list = [1, 2, 3, 4, 5]
new_list = list(filter(lambda x: x == 2, my_list))
print(new_list)

#
palabras = ['manzana', 'banana', 'pera', 'kiwi', 'uva']
filtrado_de_palabras = list(filter(lambda palabra : len(palabra)>5, palabras))
print(filtrado_de_palabras)

#
numeros = (-2, -1, 0, 1, 2, 3, 4, 5)
filtar_negativos = tuple(filter(lambda x : x < 0, numeros))
print(filtar_negativos)


#
personas = [
    {'nombre': 'Alice', 'edad': 25},
    {'nombre': 'Bob', 'edad': 30},
    {'nombre': 'Charlie', 'edad': 22},
    {'nombre': 'David', 'edad': 35}
]

filtrar_por_edad = list(filter(lambda edad : edad['edad']<30, personas))
print(filtrar_por_edad)


#filtrar los num primos
lista_numeros = [2, 3, 5, 6, 9, 25]

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

filtrar_primos = filter(es_primo, lista_numeros)
print(list(filtrar_primos))

#
words = ['canción', 'moraleja', 'casa', 'avión', 'cesped']

empiezan_por_c = list(filter(lambda letra : letra.startswith('c'), words))
print(empiezan_por_c)





def filter_by_length(words):
   return list(filter(lambda word : len(word)>=4, words))

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)

