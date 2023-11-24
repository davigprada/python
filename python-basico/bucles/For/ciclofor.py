
#Función range()
for i in range(6):
    print(i)
"""


"""
#función range con parametros
for i in range(0, 20):
    print(i)
"""


"""
#función range(parametros y saltos)
#output en una lista.
for i in range(5, 22, 2):
    print(list(range(i)))
"""


"""
#función range output inverso.
for i in range (5, 0, -1):
    print(i) #5,4,3,2,1
"""



"""
#Función anidada + tablas de multiplicar.
for i in range(10):
    print(f'Esta es la tabla del {i}')
    for j in range(10):
        print(f'{i} * {j} = {i*j}')


 