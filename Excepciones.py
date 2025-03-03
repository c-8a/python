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
