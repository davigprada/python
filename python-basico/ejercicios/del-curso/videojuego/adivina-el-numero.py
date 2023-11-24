import random

def run():
    numero_random =  random.randint(1, 100)
    numero_elegido = int(input('Escribe un número del 1 al 100: '))
    vidas = 6
    while numero_random != numero_elegido:
        vidas-= 1
        if vidas <= 1:
            print(f'Te quedan {vidas} vidas, ¡Apresúrate!')
        elif numero_random < numero_elegido:
            print('\nElige un número más pequeño.\n')
        elif numero_random > numero_elegido:
            print('\nElige un número más grande.\n')
        if vidas == 0:
            print('Game Over.')
            print(f'El número era {numero_random} haha')
            break
        numero_elegido = int(input("Elige otro número: "))
    if numero_random == numero_elegido:
        print('¡GANASTE!')


if __name__ == '__main__':
    run() 