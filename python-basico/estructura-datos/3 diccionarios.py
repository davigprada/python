#Sintaxis de los diccionarios en Python
mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
print(mi_diccionario['llave1'],mi_diccionario['llave2'],mi_diccionario['llave3'])
print(mi_diccionario['llave2'])
print(mi_diccionario['llave3'])

#Otra forma de crear diccionarios en Python
#Usando el constructor dict()
mi_segundo_dict = dict( Nombre='Sara',
                        Edad=27,
                        Documento=1004922661)
print(mi_segundo_dict)


#Obteniendo el contenido {} en general de los diccionarios:
poblacion_pais = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424, #Es una buena práctica poner , al final del diccionario.
    }
#Cómo llamar llaves {} del diccionario.
print(poblacion_pais['Argentina'])
#print(poblacion_pais['Bolivia']) #Esto es un error de llaves. La llave bolivia no existe.
print(poblacion_pais['Brasil'])
print(poblacion_pais['Colombia'])


diccionario = {
    'Nombre': 'David',
    'Edad': 19,
    'Documento': 1004922661
}

print(diccionario.keys())
#dict_keys(['Nombre', 'Edad', 'Documento'])

print(diccionario.values())
#dict_values(['David', 19, 1004922661])

print(diccionario.items())
#dict_items([('Nombre', 'David'), ('Edad', 19), ('Documento', 1004922661)])



#Recorriendo diccionarios a partir de las llaves con un ciclo For.

for pais in poblacion_pais.keys(): #Utilizamos el método keys() para acceder a las llaves.
    print(pais)
    #Argentina, Brasil, Colombia.

print('')

for pais in poblacion_pais.values():#Utilizamos el método values() para acceder a los valores de las llaves.
    print(pais)
    # 44938712, 210147125, 50372424

print('')

for pais, poblacion in poblacion_pais.items():#Utilizamos el métodos items() para imprimir las llaves y los valores del diccionario.
        #Agregamos dos iteradores:
        #pais(para los paises)
        #población(para la cantidad de habitantes)
    print(pais + f' tiene {int(poblacion)} habitantes.')
    #En el print, añadimos los dos parametros país y población.
    # Con población debemos convertirlo a int(numero) porque está como un srt(string). 
