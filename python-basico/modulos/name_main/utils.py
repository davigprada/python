

def population_by_country(data, country):
    result = list(filter(lambda item : item['country'] == country.capitalize(), data))
    return result
