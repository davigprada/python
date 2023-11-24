
import utils


data = [
    {
        'country': 'Colombia',
        'data': 300
    },
    {
        'country': 'Bolivia',
        'data': 500
    }
]

def run():
    country = input('digite el país: ')
    resultado = utils.population_by_country(data, country)
    print('main=>',resultado)

if __name__ == '__main__':
    run()

