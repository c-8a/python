suma = 0
for i in range (1, 101):
    suma += i
print("la suma es:" , suma)


numero = int(input("ingresa un número"))
if numero < 0:
    print("Este numero es negativo")
elif numero > 0:
    print("Este numero es positivo")
else:
    print("El numero es cero")


numero = int(input("ingresa un número"))
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")


numero1 = float(input("introduzca un numero"))
numero2 = float(input("introduzca el segundo numero"))
if numero1 > numero2:
    print("El número 1 es mayor al numero 2")
elif numero2 > numero1:
    print("El número 2 es mayor al numero 1")
else:
    print("Los números son iguales")



letra = input("Ingresa una letra: ").lower()
if letra in ['a', 'e', 'i', 'o', 'u']:
    print("La letra es una vocal")
else:
    print("La letra es una consonante")
