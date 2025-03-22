# Definimos una variable x con una cadena
x = "El valor de (a+b)*c es"
# Podemos realizar múltiples asignaciones
a, b, c = 4, 3, 5
# Realizamos unas operaciones con a,b,c
d = (a + b) * c
# Definimos una variable booleana
imprimir = True
# Si imprimir, print()
if imprimir:
 print(x, d)
# Salida: El valor de (a+b)*c es 35


import math
math.pi * 4
math.pi ** 2
math.sqrt(4)     # Raíz cuadrada
math. sqrt(12)


import random
random.random ()
lista = [1, 2, 3, 4]
random.choice(lista)
random.shuffle(lista)
lista

#funciones


def en_pantalla(frase1, frase2):
    print(frase1, frase2) # "return" no es obligatorio
#en_pantalla('Me gusta', 'Python')
# Resultado: Me gusta Python

def suma(a, b): # Definimos la función "suma". Tiene 2 parámetros.
    return a+b # "return" devuelve el resultado de la función.
suma (2, 3) # Función con ints
# Resultado = 5
suma(2.7, 4.0) # Función con floats
# Resultado = 6.7
suma('Me gusta', 'Python') # Función con strings

def f1(a): # Función que "encierra" a f2 (enclosing)
    print(a)
    b = 100
    def f2(x): # Función anidada
        print(x) # Llamamos a f2 desde f1
    f2(b)
f1('Python') # Llamamos a f1


def factorial(x):
    if x>1:
        return x*factorial(x-1)
    else:
        return 1
factorial(5)


def funcion_externa():
    x = 10  # Variable en el ámbito de la función externa

    def funcion_interna():
        nonlocal x  # Indica que 'x' no es local, sino no local
        x = 20      # Modifica la variable 'x' de la función externa
        print("Dentro de funcion_interna:", x)

    funcion_interna()
    print("Dentro de funcion_externa:", x)

funcion_externa()


G = 'Esta variable es de ámbito Global'
def f1():
    E='Esta variable es local a f1. Enclosing a f2'
    def f2():
        L = 'L es local a f2'
        E = 'E también es local a f2'
        G = 'G también es local a f2'
        print(L, E, G, sep = '\n')
    def f3():
        print(E, G, sep = '\n')
    f2()
    f3()
f1()


def minimo(l):
    l[0] = 1000 # Modificamos la lista en el interior
    return min(l)
l = [1, 2, 3]
print(minimo(l[:])) # minimo modifica la lista aquí
print(l)


print("hola","como", "estas", "mi", "leches", sep='--', end="\n")


