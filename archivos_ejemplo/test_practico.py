#Dados dos números, escriba un código Python para encontrar el mínimo de estos dos números: 2 y 4; -1 y -4
def minimun(a, b):
    if a <= b:
        return a
    else:
        return b
a=2
b=4
print(minimun(a, b))


def minimun(a, b):
    if a <=b:
        return a
    else:
        return b
a=-1
b=-4
print(minimun(a, b))
    
#Invertir palabras de una cadena dada.
def rev_sentence(sentence):
    words=sentence.split(' ')
    reverse_sentence= ' '.join(reversed(words))
    return reverse_sentence
if __name__ == "__main__":
    input = 'geeks de prueba de práctica de código'
print (rev_sentence(input))

#Realizar una suma de los elementos de una tupla
test_tup = (7, 9, 12, 63, 74, 2)
print ("la tupla original es: " + str(test_tup))
res = sum(list(test_tup))
print("la suma de los elementos de la tupla es: " + str(res))

# Escriba un código que calcule una lista de números proporcionados.
def list_sum(num_List):
    if len(num_List) == 1:
        return num_List[0]
    else:
        return num_List[0] + list_sum(num_List[1:])
print(list_sum([4, 2, 9, 10, 3]))

#Escriba un código que desordene al azar una lista.
from random import shuffle
x = ['La', 'Lechita', 'Es', 'Muy', 'Deliciosa']
shuffle(x)
print(x)

#Escriba un código que pueda contar todas las palabras mayúsculas de un archivo.
with open('archivo.txt') as fh:
    count= 0
    text = fh.read()
    for character in text:
        if character.isupper():
            count += 1
print(count)

#Escriba un programa para producir la serie Fibonacci en Python.
n23 = input("introduzca el numero de valores de 'n': ")
first= 0
second= 1
sum= 0 
count= 1
print("Secuencia de Fibonacci: ")
while(count<=int(n23)):
    print(sum)
    count+=1
    sum=count
    first=second
    second=sum
    sum=first+second

# Escriba un programa en Python para comprobar si un número es primo.
def isPrimo(num):
    if num <2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True
        
def app():
    num = int(input('Escriba un numero: '))
    result = isPrimo(num)
    if result is True:
        print('El número es primo!!')
    else:
        print('El número NO es primo!!')

if __name__ == '__main__':
    app()


#Escribir un programa en Python para comprobar si un número es capicúa. 
#Es decir, si se lee igual de derecha a izquierda que de izquierda a derecha.

a=input('Introduzca un número: ')
b=a[::-1]
if a==b:
    print("Es capicúa!!")
else:
    print("No es capicúa")

#Escribir un algoritmo de ordenación para un conjunto de datos numéricos en Python.

list = ["1", "4", "0", "6", "9"]
list = [int(i) for i in list]
list.sort()
print (list)

#¿Cuál es el resultado de ejecutar el siguiente código?
try:
    if '1' != 1:
        raise "algún error"
    else:
        print("no se ha producido algún error")
except "algún error":
    print("Se ha producido algún error")