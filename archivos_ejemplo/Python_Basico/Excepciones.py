def indexador(objeto, indice):
    return objeto[indice]
indexador('Python', 10) #Produce un error


def indexador(objeto, indice):
    return objeto[indice]
try:
    indexador('Python', 10)
except IndexError: # Captura Indexerror
    print('Has puesto un índice muy grande.')
print('Hemos salido del try-catch')


def indexador(objeto, indice):
    return objeto[indice]
try:
    indexador('Python', 'h')
except (IndexError, TypeError): #Captura varios errores
    print('Error.')
print('Hemos salido del try-catch')

try:
    indexador('Python', 'h')
except: # Captura todos los errores. No recomendado.
    print('Error.')
print('Hemos salido del try-catch')


def indexador(objeto, indice):
    return objeto[indice]
try:
    indexador('Python', 'h')
except IndexError: # Captura IndexError
    print('Error de índice.')
except TypeError: # Captura TypeError
    print('El índice tiene que ser un número.')
print('Hemos salido del try-catch')

a = 10
b = 1000
assert(a > b), 'A tiene que ser mayor que B!' # Si se cumple no salta el error
print('Si se muestra esto es que no ha saltado el assert')

a = 10
b = 0
c = 5
assert(a == c), 'A y C tienen que ser iguales!'

class miPropiaExcepcion(Exception): #Las excepciones heredan de Exception
    pass
try:
    raise miPropiaExcepcion
except miPropiaExcepcion:
    print('He capturado mi propia excepción')


class miError(Exception):
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return str(self.valor)
    
raise(miError('Mensaje de error'))


def indexador(objeto, indice):
    return objeto[indice]

try:
    indexador('Python', 10)
finally:
    print('Esto se ejecuta includo cuando salta la excepción')


def indexador(objeto, indice):
    return objeto[indice]
try:
    indexador('Python', 10)
    print('Este print no se ejecuta')
finally:
    print('Esto se ejecuta includo cuando salta la excepción')

def indexador(objeto, indice):
    return objeto[indice]
try:
    indexador('Python', 10)
finally:
    print('Esto se ejecuta includo cuando salta la excepción')
print('Este print tampoco se ejecuta') 

def indexador(objeto, indice):
    return objeto[indice]
try:
    indexador('Python', 10)
except IndexError:
    print('Capturamos la excepción')
finally:
    print('Esto se ejecuta incluso cuando salta la excepción')
print('Se ejecutará este print?') 

def divide(x, y):
    try:
        resultado = x/y
    except ZeroDivisionError:
        print('No se puede dividir por cero')
    else:
        print('El resultado es: ', resultado)
    finally:
        print('Ejecutamos el finally')
divide(4, 12)
divide(4, 0)

