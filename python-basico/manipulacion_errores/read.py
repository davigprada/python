

'''
En Python es posible abrir ficheros y leer su contenido.
Los ficheros o archivos pueden ser de lo más variado,
desde un simple texto, un .csv o contenido binario.


'''
#Podemos abrir el fichero con open('.nombre_del_fichero.txt')
texto = open('./texto.txt', 'r')

'''

#Argumentos de open()

Open() cuenta con un segundo argumento que debemos específicar: 
-> r: Por defecto, para leer el fichero.
-> w: Para escribir en el fichero.
-> x: Para la creación, fallando si ya existe.
-> a: Para añadir contenido a un fichero existente.
-> b: Para abrir en modo binario.

'''


# 👇Metodo read()

#print(texto.read()) #-> De esta forma puedes leer todo el archivo .txt (Ocupa más memoria)

#print(texto.readline()) #-> De esta forma lees el archivo línea a línea.
#print(texto.readline()) y va imprimiendo linea a linea.

#print(texto.readlines()) -> Devuelve una lista donde cada elemento es una línea del fichero.

for i in texto:
    print(i) #Esta es otra forma de leer el archivo usando un ciclo for (Ocupa menos memoría)

texto.close()



'''
Existe otra forma de abrir y cerrar el .txt haciendo que Python
lo haga por nosotros una vez termine de ejecutar el código.
👇
'''
print('👇Forma con with:')
with open('./texto.txt') as file:
    for line in file:
        print(line)
