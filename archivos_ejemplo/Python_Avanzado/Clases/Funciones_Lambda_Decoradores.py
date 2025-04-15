#Funciones Lambda:
# Son funciones muy cortas y directas
# escritas en una sola linea

# Funcion Cuadrado sin Lambda

def cuadrado (x):
    return x**2

print(f"El cuadrado de 5 es: {cuadrado(5)}")


# Funcion Cuadrado con Lambda (anonima)

cuadrado_lambda = lambda x: x**2

print(f"El cuadrado de 5 es: {cuadrado_lambda(5)}")



# Decoradores:
# Añaden lineas de ejecucion antes o despues de otra funcion

def decorador(funcion):
    def wrapper(*args, **kwargs):
    # Inicio del bloque de wrapper (indentado)
       print("Antes de llamar a la función")
       result = funcion(*args, **kwargs)
       print("Despues de llamar a la función")
       return result
    # Fin del bloque de wrapper
    # Esta línea está al nivel de 'def decorador', no dentro de 'wrapper'
    return wrapper

@decorador
def saludar(nombre):
    print(f"Hola {nombre}")

saludar("Carlos")