#Definicion de la Clase Libro
class Libro:
    #Constructor de la clase, inicializa los atributos de la clase
    def __init__ (self, titulo, autor, isbn) :
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True
    
    def prestar(self):
        if self.disponible == True:
            self.disponible = False
            print("Libro prestado exitosamente")
        else:
            print("Libro no disponible")

    def devolver(self):
        if self.disponible == False:
            self.disponible = True
            print("Libro devuelto exitosamente")
        else:
            print("Libro ya disponible")

    #Método para mostrar toda la información de la clase
    def mostrar (self) :
        if self.disponible == True:
            s_disponible = "Si"
        else:
            s_disponible = "No"

        print (f" - Título: {self.titulo} - Autor: {self.autor} - ISBN: {self.isbn} - Disponible: {s_disponible}")


libreria = []
    
#Funcion para agregar un elemento a la lista
def agregar(libro):
    libreria.append(libro)
    print ("\nLibro añadido exitosamente")

#Funcion para marcar un libro como "No disponible" al prestarlo
#ó mostrar una advertencia si ya estaba prestado
def prestar (isbn) :
    for libros in libreria:
        if libros.isbn == isbn:
            libros.prestar()
            return
            
    print("Libro no encontrado")

#Funcion para marcar un libro como "Disponible" al ser devuelto
#ó mostrar una advertencia si ya se encontraba disponible
def devolver (isbn) :
    for libros in libreria:
        if libros.isbn == isbn:
            libros.devolver()
            return

    print("Libro no encontrado")
    
#Funcion para mostrar la información de cada objeto dentro de la lista
def mostrar_todos():
    for libros in libreria:
        libros.mostrar()

#Funcion para buscar un elemento dentro de la lista según su ISBN
#Si el elemento no existe, muestra una advertencia
def buscar(isbn):
    for libros in libreria:
        if libros.isbn == isbn:
            libros.mostrar()
            return
        
    print("Libro no encontrado")

#Mensaje de bienvenida
print ("Bienvenido al sistema de gestión de biblioteca")

opcion = 1 #creacion de la variable de control del bucle while

#Bucle interactivo de opciones
while opcion != 6:
    print ("\nElige una opción")
    print ("1. Agregar libro\n" +
        "2. Prestar libro\n" +
        "3. Devolver libro\n" +
        "4. Mostrar libros\n" +
        "5. Buscar\n" +
        "6. Salir")
    opcion = int(input("\nOpción elegida: ")) 
    if opcion == 1: 
        titulo = input("\nIngrese titulo: ")
        autor = input("Ingrese autor: ")
        isbn = input("Ingrese ISBN: ")
        libro = Libro(titulo, autor, isbn)
        agregar(libro)
    elif opcion == 2:
        isbn = input("Ingrese ISBN: ")
        prestar(isbn)
    elif opcion == 3:
        isbn = input("Ingrese ISBN: ")
        devolver(isbn)
    elif opcion == 4:
        mostrar_todos()
    elif opcion == 5:
        isbn = input("Ingrese ISBN: ")
        buscar(isbn)
    elif opcion == 6:
        print("Gracias por usar el servicio")
    else:
        print("Opción incorrecta, intente de nuevo")


