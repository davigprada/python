def conversor(tipo_pesos, valor_dolar):
    pesos = float(input('¿Cuántos pesos ' + tipo_pesos + ' tienes? '))
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2) 
    valor_dolar = str(dolares)
    print(f'Tienes ${dolares} dólares')
    
menu = """
Bienvenido al conversor de monedas 💰

¿Qué moneda quieres convertir a dólar?

1- Pesos Colombianos 🇨🇴
2- Pesos Argentinos 🇦🇷
3- Pesos Mexicanos 🇲🇽

Elige una opción: """

opcion = input(menu)
if opcion == '1':
    conversor('colombianos',3760)
elif opcion == '2':
    conversor('argentinos',99.70)
elif opcion == '3':
    conversor('mexicanos',20.56)
else:
    print('Ingresa una opción correcta, por favor.')
