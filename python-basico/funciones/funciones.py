
#Sintaxis de una función

""" def nombre_de_la_funcion(argumentos):
    # Código de la función
    # Puede incluir operaciones, lógica, etc.
    return valor_de_salida (opcional)
 """


#Mi primera función
def saludar():
    print('Hola, David')
#saludar()


#Función con return
'''
Es util para guardar el resultado de la función en una variable para reutilizar en el código
Esto permite que el resultado de una funcion se puede utilizar, manipular, modificar o incluso añadir a otro resultado.

Ejercicios con return 👇
'''

def suma(a,b):
    return a + b
sumatoria = suma(1,4)
#print(sumatoria) #5


def area_rectangulo(base, altura):
   return base * altura

resultado = area_rectangulo(25, 10)
#print(resultado) #250
   

def tipo_de_numero(n):
   if n > 0:
      return 'positivo'
   elif n < 0:
      return 'negativo'
   else:
      return 'cero'

tipo = tipo_de_numero(3)
#print(tipo) #positivo

def promedio(lista):
   return sum(lista) / len(lista) 

n = promedio([3,5,6,8])
#print(n)


#En py podemos retornar más de una función
def volumen(l=1, w=1, d=1):
   return l * w * d, 'hola', 5+3 #retornamos 3 valores diferentes
result = volumen()
#print(result) #(1, 'hola', 8) -> Se devuelve una tupla // print(result[1]) <-> podemos indexar la tupla
result, text, sumita= volumen()
#print(result)
#print(text)
#print(sumita) #Se asigna una variable para cada valor de la función





   