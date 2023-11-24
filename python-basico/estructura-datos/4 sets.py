#Forma #1 de crear un set(conjunto)
countries = {'Colombia', 'Chile', 'España'}
print(type(countries))
print(countries)


#Forma #2 de crear un set(conjunto) 
lista_paises = ['Argentina', 'Bolivia', 'Guatemala']
conjunto_paises = set(lista_paises) #Creo una variable nueva (alt) y uso la función set().
print(type(conjunto_paises))
print(conjunto_paises) 


    #Crear un conjunto a partir de un String
set_from_string = set('Guuateemalaa')
print(set_from_string) #No acepta valores repetidos e imprime alfabéticamente

    #Crear un conjunto a partir de una tupla
set_from_tuple = set(('carro', 'aavión', 'paz', 'aavion'))
print(type(set_from_tuple))
print(set_from_tuple)

    #Crear un conjunto a partir de una lista
lista = [4, 6, 4, 'hola', True, 'hola']
set_from_list = set(lista)
print(type(set_from_list))
print(set_from_list) 

#-------------------------------------------------------------------------#

#Operaciones con sets()

set_a = {'Colombia', 'México', 'Bolivia'}
set_b = {'Perú', 'Bolivia'}

#Unir dos conjuntos

    #Forma 1
set_c = set_a.union(set_b)
print(set_c)

    #Forma 2
set_c = set_a | set_b
print(set_c)

#Intersección entre dos o más conjuntos

    #Forma 1
set_c = set_a.intersection(set_b)
print(set_c)

    #Forma 2
set_c = set_a & (set_b)
print(set_c)

#Diferencia (resta) entre dos conjuntos

    #Forma 1
set_c = set_a.difference(set_b)
print(set_c)

#Forma 2
set_c = set_a - set_b
print(set_c)
