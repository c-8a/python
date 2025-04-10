# Funcion sum:
# Funcion nativa de python que suma todos los elementos de un iterable (lista, tupla, conjunto, etc)
# tambien se le puede especificar un valor inicial

lista = [1, 2, 3, 4, 5]

resultado = sum(lista)
print(f"Resultado de la suma es: {resultado}")


resultado = sum(lista, 20)
print(f"Resultado de la suma con valor inicial de 20 es: {resultado}")


# Funcion next:
# Funcion nativa de python que obtiene el siguiente elemento de un objeto iterable
# se puede indicar un valor predeterminado si el iterador está agotado
# si no se indica el valor predeterminado se genera una excepcion de StopIteration

iterador = iter(lista)

print(f"Siguiente elemento de la lista es: {next(iterador)}")
print(f"Siguiente elemento de la lista es: {next(iterador)}")
print(f"Siguiente elemento de la lista es: {next(iterador)}")
print(f"Siguiente elemento de la lista es: {next(iterador)}")
print(f"Siguiente elemento de la lista es: {next(iterador)}")
print(f"Siguiente elemento de la lista es: {next(iterador)}")


#Excepciones:
# Al ocurrir algun error durante la ejecucion del programa
# se generan objetos del tipo excepcion que pueden ser capturados
# y tratados con "try", "except", "else" y "finally", los ultimos 2 son opcionales
# se pueden programar todos los tipos de exceptions con except + Exceptiontype
# o se puede programar una sola que trate a todas las exceptions = except + Exception
# con el bloque finally se agregan instrucciones al finalizar la rutina del "try"
# independientemente de si existe o no exception, se ejecuta el finally
# el bloque else se ejecuta unicamente si el bloque try no lanza ninguna exception



def dividir(numerador, denominador):
    try:
        if denominador == 0:
            raise Exception("El denominador es igual a cero")
        resultado = numerador / denominador
        print(f"Resultado de la division: {resultado}")
    except Exception as e:
        print(f"Ocurrio un error: {e}")
    #except ZeroDivisionError:
    #    print("No se puede dividir por cero papi")
    #except TypeError:
    #    print("Los operadores deben ser numeros")
    else:
        print(f"No ocurrió ningun error")
    finally:
        print("Terminamos de procesar la exception\n")

dividir(10,2)
dividir(10,'0')



