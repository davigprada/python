
'''
Las funciones de orden superior (Higher order function)
se refiere a funciones que pueden tomar otras funciones
como argumentos y/o devolver funciones como resultados. 
'''
    
def increment(x):
    return x + 1
    
def hof(x, func):
    return x + func(x) #func(3) toma el valor de la suma de incremen()

result = hof(2, increment)
print(result) #5

increment_v2 = lambda x : x + 1
hof_v2 = lambda x, func : x + func(x)
print(hof_v2(3, increment_v2))




def saludar():
    return 'hola'

def saludar_con_nombre(funcion, nombre):
    return funcion() + ' ' + nombre

nombre = 'david'
saludo = saludar_con_nombre(saludar, nombre)
print(saludo)


