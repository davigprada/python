
#Realizar una suma con sum()
data = [10, 10, 5, 7, 10]
print(sum(data))


#Forma #1 para calcular el promedio.
def promedio(listado):    #longitud del listado
    return sum(listado) / len(listado) #5 

resultado = promedio([10, 10, 5, 7, 10])
print(resultado)



#Forma #2 para calcular el promedio.
import statistics

lista = [10, 10, 5, 7, 10]
mean = statistics.mean(lista)
print(mean)