
#Lista de listas. 
lista = [[56, 34, 1],
         [12, 4, 5],
         [9, 4, 3]]

""" #Sí iteramos usando solo un For
#estaremos realmente accediendo a la segunda lista
#pero no a los elementos individuales
print('Utilizando un solo For.')
for i in lista:
    print(i)
print('') """


#Si queremos acceder a cada elemento individualmente, podemos anidar dos for.
#Uno de ellos se encargará de iterar las columnas y el otro las filas.
#print('Anidando dos For.')
for i in lista:
    for j in i:
        print(j)