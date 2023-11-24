
'''

Uso de try y except

Podemos capturar errores haciendo uso de try y except and finally(opcional)

Lo que hay dentro del try es la sección del código que podría lanzar
la excepción que se está capturando en el except. Por lo tanto cuando
ocurra una excepción, se entra en el except pero el programa no se detiene.



'''

""" #De esta forma se captura el error y no se detiene el programa
age = int(input('¿Cuál es tu edad? '))
try:
    if age < 18:
        raise Exception('No se admiten menores de edad')
    else:
        print(f'Tienes {age}. ¡Puedes ingresar!')
except Exception as error:
    print(error)
finally:
    print('Fin del programa') #opcional👇
'''
El bloque finally se ejecuta haya o no excepciones en el bloque try,
su ejecución es opcional dependiendo de los requerimientos del programa.
'''



#Al capturar el error las siguientes lineas de código se imprimen normal
print('Hola Mundo')



#Este programa admite solo números y captura el error sí se digita otro dato
#Por ser while, hasta que no se cumpla la función, no se detiene el programa.
while True:
    try:
        x = int(input("Please enter a number: "))
        print('Well done! The number is:',x)
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")



'''
👇
Otra forma si no sabes que excepción puede saltar,
puedes usar la clase genérica Exception.
En este caso se controla cualquier tipo de excepción.
De hecho todas las excepciones heredan de Exception.

'''
try:
    c = 5/0       # Si comentas esto entra en TypeError
    #d = 2 + "Hola" # Si comentas esto entra en ZeroDivisionError
except Exception:
    print("Ha habido una excepción")



#Haciendo uso de type(), sabemos qué excepción ha sido la que ha ocurrido
try:
    d = 2 + "Hola" # Si comentas esto entra en ZeroDivisionError
except Exception as ex:
    print("Ha habido una excepción", type(ex))


 """
def my_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = 'No se puede dividir por 0'
    return result
    
response = my_divide(10, 2)
print(response) 

response = my_divide(10, 0)
print(response) 