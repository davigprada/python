
'''
Escribir archivos en Python
https://ellibrodepython.com/escribir-archivos-python

-> Nombre para el fichero
-> Parámetro opcional según las necesidades del archivo.

Los parámetros más relevantes son:
w: Borra el fichero si ya existiese y crea uno nuevo con el nombre indicado.
a: Añadirá el contenido al final del fichero si ya existiese (append end Inglés)
x: Si ya existe el fichero se devuelve un error.

'''

#Crear un fichero desde python
fichero = open('fichero_de_prueba.txt', 'w') #Es importante cambiar el parámetro sí queremos (r,w...)
fichero.write('Hola, este es un archivo de texto creado\ndesde el archivo write.py!')
open(fichero,'r')
print(fichero.read())



""" 
with open('./texto.txt', 'w+') as texto: #Permisos de escritura pero borra y crea nuevo contenido (reescritura)
    for line in texto:
        print(line)
    texto.write('\ntexto nuevo en este archivo!\n')
    

with open('./texto.txt', 'r+') as texto: #Permisos de lectura y escritura al archivo de texto
    for line in texto:
        print(line)
    texto.write('\n') """