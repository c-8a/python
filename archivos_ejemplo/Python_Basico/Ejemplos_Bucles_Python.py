a = 0
while a<3:
    print (a, end='-') # Acabamos con espacios en lugar de salto de línea
    a += 1 # Equivalente a: a = a + 1
print (a) # Estamos fuera del while
print('Hemos salido fuera del while')


a = 5
while a: # Utilizamos la propia variable como condición
    print (a, end=' ')
    if a == 2:
        break
    a -= 1
print ('\nFuera del Bucle.')
print('Valor de "a": {} porque la leche es rica'.format(a))
print('Valor de "a":', str(a))


a = 7
while bool(a):
    a -= 1
    if a % 2 == 0:
        continue # Saltamos a la siguiente iteracción si es a es par.
    print (a, end=' ')
print ('\nFuera del Bucle.')


a = 1054273
b = a // 2 # División entera. P. ej. 13 // 2 = 6
while b > 1:
    if a % b == 0: # % es el operador resto. P. ej. 10 % 5 == 0
        print('{} es factor de {}'.format(b,a))
        break
    b -= 1
else:
    print('{} es primo'.format(a))
print ('\nFuera del Bucle.')

for s in ['Me', 'gusta', 'Python!']:
    print(s, end=' ')

a = 0
for x in [1, 20, 3, 45]:
    a += x
print(a)

for c in 'Me gusta Python!':
    print(c, end=' ')

keys = ['nombre', 'apellidos', 'edad']
values = ['Guido', 'van Rossum', '60']
d = dict(zip(keys, values)) # Creamos el diccionario
for k in d:
    info = '{}: {}'.format(k, d[k]) # Texto formateado con claves y valores
    print(info)
else:
    print("memita rica, terminó correctamente el for")

a1 = [10, 20, 300, 40]
b1 = [5, 25, 50, 10]
for a, b in zip(a1, b1): #equivalente => c1 = [(10,5),(20,25),(300,50),(40,10)]
    m = max(a, b) # max(a, b) devuelve el máximo entre a y b
    print(m , end=' ')

keys = ['nombre', 'apellidos', 'edad', 'sexo']
values = ['Guido', 'van Rossum', 60, 'enorme']
d = dict(zip(keys, values))
for k, v in d.items(): # d.items devuelve tupla con clave, valor
    print('{}: {}'.format(k, v))


letras = list('abcdefghijklmnopqrstuvwxyz')

import random

l1 = letras[:8]
l2 = letras [8:16]
l3 = letras [16:]

random.shuffle(l1)
random.shuffle(l2)
random.shuffle(l3)

print(l1)
print(l2)
print(l3)
for a,b,c in zip(l1,l2,l3):
    print(a+b+c, end=' ')


#ficheross

zen = '''\
Bello es mejor que feo.
Explícito es mejor que implícito.
Simple es mejor que complejo.
Complejo es mejor que complicado.
'''

f = open('short.zen.txt', 'w')
f.writelines(zen) # Escribe el fichero
f.close() # Cierra el fichero

f = open('short.zen.txt', 'r')
linea = f.readline()
print(linea)
linea = f.__next__()
print(linea)
linea = f.readline()
print(linea)
linea = f.readline()
print(linea)
linea = f.readline()
print(linea)

lista = [1,2,3, 4]
#li = lista.__iter__()
li = iter(lista)

li_print = next(li)
print(li_print)
li_print = next(li)
print(li_print)
li_print = next(li)
print(li_print)
li_print = next(li)
print(li_print)

