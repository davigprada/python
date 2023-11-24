def potencia(numero):
    potencia = 1 #Siempre definir una variable para que el ciclo pueda funcionar correctamente.
    while potencia <= 10: #Condición del While 
        result = numero ** potencia #Operaciones matemáticas
        print(f'Potencia de {numero} elevado a la {potencia} es {result}') #Resultado de las operaciones
        potencia +=1 #Contador de potencia. Sí antes valía un número, ahora vale +1.


def run():
    numero = int(input('Escribe el número al cual quieres averigüarle la potencia: ')) #Pido datos al usuario.
    potencia(numero) #Con esta línea lo que hago es invocar/mandar a llamar la función para que el programa se puede ejecutar



#Programa 2: Potencia de 2 con While.
def main():
    LIMITE = 1024 #Se define la CONSTANTE límite asignándole el valor 1000.
    i = 0 #Se defina la variable con valor 0.
    potencia_2 = 2 ** i #Operación que calcula la potencia de 2.
    while potencia_2 <= LIMITE: #Condicición
        print(f'2 elevado a {i} es igual a {potencia_2}') #Resultado de las potencias.
        i+=1 #Contador asignándole un valor nuevo a i. Sí antes valía x ahora vale +x.
        potencia_2 = 2**i   #Operación matemática, sí no se coloca se crea un bucle infinito. Tener cuidado.


if __name__ == '__main__':
    run() #Mando a llamar la función run()
    main() #Mando a llamar la función main()
