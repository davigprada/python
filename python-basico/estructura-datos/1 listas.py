#Listas
lista_datos = ['Hola', 21, True, 1.68]
#print(lista_datos)

    #Las listas son mutables.
    # Sus elementos se pueden modificar.
lista_datos[0] = 'David'
#print(lista_datos) #'Hola' -> 'David'

    #Crear una sublista a partir de una lista
    #En este caso, accedí solo a los números de la lista principal
lista_num = lista_datos[1::2]
#print(lista_num) #21, 1.68


#Recorrer una lista con For
#1
lista = [1, 2, 3, 4]
for i in lista:
    if i == 3: #Una vez llega al 3 cierra el ciclo
        break
    print(i)

print('')
#2
lista = [1, 2, 3, 4]
for i in lista:
    if i == 3: #Omite el 3 y continua el ciclo
        continue
    print(i)

print('')
#3
profesiones = ['Doctor', 'Astronauta', 'Ingeniero', 'Abogado']
for i in profesiones[::-1]: #Imprime el inverso de las profesiones
    print(i)

print('')
#-------------------------------------------------------------------------------------------------#

#METODOS DE LISTAS
lista_datos = ['Hola', 21, True, 1.68]

#append() -> añade un elemento al final de la lista
lista_datos.append(True)

#extend() -> añade una lista a la lista principal (no como lista anidada)
lista_datos.extend(['Soltero', 'Estudiante'])

#insert() -> Inserta un elemento en el indice determinado. 
lista_datos.insert(3, False)

#remove() -> Elimina el argumento indicado
lista_datos.remove('Soltero')

#pop() -> Elimina por defecto el último elemento de la lista
lista_datos.pop()

#reverse() -> Invierte el orden de la lista
lista_datos.reverse()

#sort() -> Ordena los elementos de un MISMO TIPO de menor a mayor.
#lista_datos.sort()


print(type(lista_datos))
print(lista_datos)