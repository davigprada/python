#convirtiendo de pesos mexicanos a dólares
nombre = input('¿Cuál es tu nombre? ')
pesos_mexicanos = input('¿Cuántos pesos mexicanos tienes? ')
pesos_mexicanos = float(pesos_mexicanos)
valor_dolar = 20.56
dolares = pesos_mexicanos / valor_dolar
dolares = round(dolares, 2)
valor_dolar = str(dolares)
print(f'Tienes ${dolares} pesos mexicanos, {nombre}.')


#convirtiendo de dólares a pesos colombianos
nombre = input('¿Cuál es tu nombre? ')
pesos = input(f'¿Cuántos pesos colombianos tienes {nombre}? ')
pesos = float(pesos)
valor_dolar = 3776
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print(f'{nombre} tienes ${dolares} dólares.')

















