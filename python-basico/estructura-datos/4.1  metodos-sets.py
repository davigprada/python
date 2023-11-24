
paises = {'Colombia', 'México', 'Bolivia'}

#len() longitud total del conjunto.
print(len(paises))

#in() saber si un elemento está presente en un conjunto.
print('Colombia' in paises) #True
print('España' in paises) #False


#Métodos de set()


#El metodo add() añade UN SOLO elemento al set.
paises.add('España') #True
print(paises)

#El metodo update() añade varios elemento al set.
paises.update({'Italia', 'Argentina', 'Colombia'}) 
print(paises) #Añade Italia y Argentina pero omite Colombia

#El metodo remove() elimina un elemento y si este no existe lanza el error “keyError”.
paises.remove('Italia') 
#paises.remove('Venezuela') KeyError: 'Venezuela'
print(paises)

#El metodo pop() remueve un elemento aleatorio del conjunto.
print(paises.pop())

#Para ordenarlos alfabéticamente, se puede usar la función sorted()
print(sorted(paises))

#El metodo clear() elimina todo el contenido del conjunto.
paises.clear()
print(paises) #Conjunto vacío.

