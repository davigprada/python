import requests #importamos la librería requests

api_url_categories = 'https://api.escuelajs.co/api/v1/categories' #url

def get_categories(): # Creamos la función [obtener_categorias]
    r = requests.get(api_url_categories) #Creamos la variable r de requests para hacer la solicitud al enlace https
    #El método requests.get() de la librería requests envía una solicitud GET a la URL para obtener "toda la información".
    print(r.status_code) #Podemos obtener el estado [status_code]
    #Los status code de respuesta HTTP indican sí se ha completado satisfactoriamente una solicitud HTTP específicada.
    print(r.text) #Podemos obtener la respuesta: Qué información nos da esta API
    print(type(r.text)) #Conocemos el tipo de dato que es r.text
    categories = r.json() 
    #EL formato json lo transforma en una lista (con diccionarios dentros) que Python va a reconocer.
    for category in categories:
        print(category['name'])