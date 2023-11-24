'''
Un iterable es el contenedor que podemos iterar,
este puede ser una estructura de datos (tuplas, listas, diccionarios, sets e incluso strings).

Un iterador es el objeto con el que se puede iterar, es decir, recorrer todos los elementos.
Consta de los metodos iter() y next()
'''

n = [1, 2, 3, 4, 5] #iterable

'''
En bambalinas, la sentencia for llama a iter() en el objeto contenedor -> n. 
La función retorna un objeto iterador que define el método __next__() que accede
elementos en el contenedor de a uno por vez.

Cuando no hay más elementos, __next__() lanza una excepción
StopIteration que le avisa al bucle del for que hay que terminar. 
'''
for i in n:
    print(i) 


'''
Lo mismo sucede sí lo hacemos paso por paso usando el metodo iter(n)
y a su vez, el metodo next para que recorra uno a uno el contenedor n.
'''
new_iter = iter(n) #iterador
print(new_iter) #<list_iterator object at 0x7f1e29593730>

print(next(new_iter)) #1
print(next(new_iter)) #2 
print(next(new_iter)) #3 y así sucesivamente hasta llegar a 5 que después lanza un StopIteration.
print(next(new_iter)) #4
print(next(new_iter)) #5
print(next(new_iter)) #StopIteration



#Lo mismo sucede aquí
libro = ['pagina1', 'pagina2', 'pagina3', 'pagina4'] #iterable

for i in libro:
    print(i)

marcapaginas = iter(libro) #iterador
print(marcapaginas)

print(next(marcapaginas)) #pagina1
print(next(marcapaginas)) #pagina2
print(next(marcapaginas)) #pagina3
print(next(marcapaginas)) #pagina4

#print(next(marcapaginas)) #StopIteration -> Excepción integrada de Python


