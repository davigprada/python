def run(n1, n2):
    return n1 + n2


n1 = int(input('Digita un número: '))
n2 = int(input('Digita otro número: '))
suma = run(n1, n2)
print(f'El resultado de la suma es: {suma}')


if __name__ == '__main__':
    run(n1, n2)