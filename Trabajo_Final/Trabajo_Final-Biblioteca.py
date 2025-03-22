#Definicion de la Clase Libro
class Libro:
    #Constructor de la clase, inicializa los atributos de la clase
    def __init__ (self, titulo, autor, isbn) :
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    #Método para agregar un libro a la lista
    def agregar(self, libreria):
        libreria.append(self)
        print ("\nLibro añadido exitosamente")
    
    #Método para prestar un libro si el mismo está disponible
    def prestar(self):
        if self.disponible == True:
            self.disponible = False
            print("Libro prestado exitosamente")
        else:
            print("Libro no disponible")

    #Método para devolver un libro si el mismo fue prestado
    def devolver(self):
        if self.disponible == False:
            self.disponible = True
            print("Libro devuelto exitosamente")
        else:
            print("Libro ya disponible")

    #Método para mostrar toda la información del objeto
    def mostrar (self) :
        if self.disponible == True:
            s_disponible = "Si"
        else:
            s_disponible = "No"
        print (f" - Título: {self.titulo} - Autor: {self.autor} - ISBN: {self.isbn} - Disponible: {s_disponible}")

    #Getter para las busquedas de ISBN de los objetos
    def get_isbn(self):
        return self.isbn
    
#Declaración inicial de una lista vacía
libreria = []

#Funcion para prestar un libro de la lista buscando por ISBN
def prestar_libro (isbn) :
    for libros in libreria:
        if libros.get_isbn() == isbn:
            libros.prestar()
            return 
    print("Libro no encontrado")

#Funcion para devolver un libro de la lista buscando por ISBN
def devolver_libro (isbn) :
    for libros in libreria:
        if libros.get_isbn() == isbn:
            libros.devolver()
            return
    print("Libro no encontrado")
    
#Funcion para mostrar la información de cada objeto dentro de la lista
def mostrar_libros():
    for libros in libreria:
        libros.mostrar()

#Funcion para buscar un elemento dentro de la lista según su ISBN
#Si el elemento no existe, muestra una advertencia
def buscar_libro(isbn):
    for libros in libreria:
        if libros.get_isbn() == isbn:
            libros.mostrar()
            return   
    print("Libro no encontrado")

#Mensaje de bienvenida
print ("Bienvenido al sistema de gestión de biblioteca")

opcion = 1 #Creación de la variable de control del bucle while

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
        #Se piden los datos del nuevo libro
        titulo = input("\nIngrese titulo: ")
        autor = input("Ingrese autor: ")
        isbn = input("Ingrese ISBN: ")
        #Se crea un nuevo objeto libro con los datos introducidos
        libro = Libro(titulo, autor, isbn)
        #Se agrega el libro al listado
        libro.agregar(libreria)
    elif opcion == 2:
        isbn = input("Ingrese ISBN: ")
        prestar_libro(isbn)
    elif opcion == 3:
        isbn = input("Ingrese ISBN: ")
        devolver_libro(isbn)
    elif opcion == 4:
        mostrar_libros()
    elif opcion == 5:
        isbn = input("Ingrese ISBN: ")
        buscar_libro(isbn)
    elif opcion == 6:
        print("Gracias por usar el servicio")
    else: #Para cualquier otra opción, se muestra un mensaje y reintenta
        print("Opción incorrecta, intente de nuevo")