def run():
    numero = int(input('Escribe un número: '))
    contador = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            contador+=1
    if contador == 2:
        print('Es primo')
    else:
        print('No es primo')

if __name__ == '__main__':
    run()