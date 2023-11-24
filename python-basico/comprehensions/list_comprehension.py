
#Las list comprehension nos permiten crear listas de elementos en una sola línea de código

        #[expresion for elemento in iterable]
n = [element for element in range(5)]
#print(n)
#El valor de retorno es una lista nueva, que deja la lista anterior sin cambios.



nums = [2, 21, 44, 32, 70, 98, 146]
pares = [n for n in nums if n % 2 == 0]
#print(pares)


numeros = [98, 483, 34, 25,40, 21, 59, 85]
doble_par = [n * 2 for n in numeros if n % 2 == 0]
#print(doble_par)


oracion = 'Maria Angelica tiene una situación grave con sus pies, le duelen!'
vocales = [v for v in oracion if v.lower() in 'aeiou']
#print(vocales)



pares = [i for i in range(0,21) if i % 2 == 0]
#print(pares)

palabras = ['david', 'santiago', 'jean']
cantidad = [len(palabra) for palabra in palabras]
#print(cantidad)


mayus = [palabra.upper() for palabra in palabras]


days = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
solo_a = [vocal for vocal in days if 'a' in vocal]
#print(solo_a)

#invertir 
t = ['david', 'es', 'inteligente']
t_invertido = [texto for texto in t[::-1]]
#print(t_invertido)

#invertir palabra 
palabras = ["Python", "es", "divertido"]
invertidas = [palabra[::-1] for palabra in palabras]
#print(invertidas)


lista_uno = ['cacaroto', 25, True, 5.3, 'DAVID']
lista_dos = [25, 9.5, 'cacaroto', False, 'DAVID']
interseccion = [x for x in lista_uno if x in lista_dos]
#print(interseccion)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)


newlist = ['hello' for x in fruits]
print(newlist)

list_dos = [letra[::-1] for letra in fruits if 'a' in letra]
#print(list_dos)
