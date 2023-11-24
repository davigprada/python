import store #importamos el modulo store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1, 2, 3]

@app.get('/contact')
def get_list():
    return { 'name' : 'David'}


@app.get('/web', response_class=HTMLResponse)
def get_list():
    return '''
        <h1>Hola soy una página</h1>
        <p>Soy un parrafo</p>
    '''










def run():
    store.get_categories() #función principal que ejecuta el modulo store para obtener get_categories


if __name__ == '__main__':
    run() #Ejecuta la función principal