# Programa que dice sí una palabra es un Palíndromo o no.

# Forma #1 (Más explicita)
def palindromo(palabra): #Definimos una función que recibirá como parametro la palabra. 
    palabra = palabra.replace(' ', '').lower() #A la palabra le eliminamos los espacios y convertimos a minúsculas.
    palabra_invertida = palabra[::-1] #Generamos la palabra invertida a partir de la palabra original.
    if palabra == palabra_invertida: #Preguntamos sí la palabra es igual a la palabra invertida.
        return True #Devuelve True sí es igual.
    else:
        return False #Devuelve False sí no es igual.


def run(): #Definimos la función principal.
    palabra = input('Escribe una palabra: ') #Pedimos al usuario que de una palabra y la guardamos en una variable.
    #Ejecutamos la función palíndromo y le pasamos como parametro la variable con la palabra solicitada.
    #Guardamos lo que returne esta función en una variable.
    es_palindromo = palindromo(palabra) 
    if es_palindromo == True: #Preguntamos sí lo que retorna la función es Verdadero.
        print('Es palíndromo.')
    else:
        print('No es palíndromo') #No es palíndromo.
    
    
if __name__ == '__main__': #Entry Point.
    run() #Mandamos a llamar la función principal.

