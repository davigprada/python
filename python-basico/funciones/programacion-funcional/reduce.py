'''

La función reduce() se usa para reducir todos los elementos
de la entrada a un único valor aplicando un determinado criterio.

👇 Para utilizar reduce() debemos importar
from functools import reduce

Sintaxis
reduce(función, iterable)

Sintaxis con lambda function
reduce(lambda acc, val: acc (criterio) valor, funcion)

Es importante notar que la función recibe dos argumentos:

-> El acumulador es el valor devuelto en la iteración anterior,
que va acumulando un resultado hasta que llegamos al final.

-> El valor es cada uno de los elementos de nuestra lista,
que en nuestro caso vamos añadiendo al acumulador.


'''
from functools import reduce


#
lista_numeros = [1, 2, 3, 4, 5]            
suma_total = reduce(lambda acc, val : acc + val, lista_numeros)
print(suma_total)

#print(sum(lista_numeros))

#
n = [5, 7, 3, 2]
minimo = reduce(lambda acc, min : acc if acc < min else min, n)
print(minimo)

#print(min(n))

#
suma_cuadrado = reduce(lambda acc, n : acc + n**2, lista_numeros)
print(suma_cuadrado)

#
palabras = ["Hola", " ", "mundo", "!"]

concatenar = reduce(lambda acc, palabra : acc + palabra, palabras)
print(concatenar)