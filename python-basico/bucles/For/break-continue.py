""" def run():
    palabra = input('Escribe una palabra: ')
    for i in palabra:
        if i == 'k':
            print(f'Esta frase tiene la letra {i}, lo siento.')
            break
    for j in palabra:
        if j == 'o':
            print(f'Esta frase tiene la letra {j}')
            break
    print('Chao.')


if __name__ == '__main__':
    run()


#Imprime todos los números del 1 al 20 a excepción de aquellos que sean múltiplos de 5.
def run():
    for i in range(21):
        if i % 5 == 0:
            continue
        print(i)
 """

#Sentencia break con For.
""" 
for i in range(10):
    if i == 5:
        break
    print(f'El número es {i}')
print('Fin del programa.') """


""" #Sentencia break con While.
x = 5
while True:
    x -= 1
    print(x)
    if x == 0:
        break
print("Fin del bucle") """


""" 
for i in range(10):
    if i == 5:
        continue  #continua el ciclo.
    print(f'El número es {i}')
print('Fin del programa.')
 """


""" for letra in 'Python':
    if letra == 't':
        continue
    print(letra) """


x = 5
while x > 0:
    x -= 1
    if x == 3:
        continue
    print(x)