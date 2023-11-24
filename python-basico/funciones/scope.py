
x = 10 #global scope
print(f'variable global {x}') #10

def n():
   x = 20 #local scope
   return x
print(f'variable local {n()}') #20


#print(f'yo tengo {x} años') #10
#print(f'yo tengo {n()} años') #20



#Cambiar una variable global desde una función

name = 'David'
def my_name():
   global name # usando global se vuelve una variable global y se modifica su anterior valor
   name = 'Gonzalo'

my_name()
print(name)


