'''

Paquetes:
Un paquete en Python es una carpeta que contiene módulos relacionados.
Los paquetes se utilizan para organizar y estructurar proyectos más grandes.
Un paquete debe contener un archivo especial llamado __init__.py que le indica a Python que es un paquete.
Los paquetes pueden tener subpaquetes y módulos dentro de ellos


En resumen, un módulo es un archivo que contiene código reutilizable
y un paquete es una carpeta que contiene módulos relacionados.
Los módulos y paquetes se utilizan para organizar y reutilizar código
en proyectos más grandes y complejos.


Un paquete en Python es una carpeta que contiene varios módulos
y un archivo especial llamado __init__.py. 

El __init__.py es opcional en Python 3.3 o versiones posteriores,
pero se usa comúnmente para indicar que un directorio debe ser tratado como un paquete.

Los paquetes permiten una jerarquía en la organización del código.

mi_paquete/
    __init__.py
    modulo1.py
    modulo2.py
    subpaquete/
        __init__.py
        modulo3.py

        
- El directorio mi_paquete es el paquete principal.

- El archivo __init__.py en mi_paquete indica que es un paquete.

- Los archivos modulo1.py y modulo2.py son módulos en el paquete principal.

- El directorio subpaquete también es un paquete, ya que contiene su propio archivo __init__.py.

- El archivo modulo3.py es un módulo en el subpaquete.

'''