
""" def run():
    nombre = input('Escribe tu nombre: ')
    for recorriendo_nombre in nombre:
        print(recorriendo_nombre)

    frase = input('Escribe una frase: ')
    for i in frase:
        print(i.upper(), end=' ')

if __name__ == '__main__':
    run()
 """

#

#Recorriendo Strings con range.
nombre = 'SANTIAGO'
for i in nombre:
    print(f'Dame una {i}'.upper())
#print('¿Qué dice?...')
#print(nombre)

#Pidiendo datos al usuario.
#Uso de la built-in function -> end=''.
""" veces = int(input('¿Cuántas veces quieres que se repita el programa?: '))
for i in range(veces):
    print('¡HOLA! ', end='') """