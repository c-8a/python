#Definicion de la Clase Libro
class Libro:
    #Constructor de la clase, inicializa los atributos de la clase
    def __init__ (self, titulo, autor, isbn) :
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__disponible = True

    #Método para agregar un libro a la lista
    def agregar(self, libreria):
        libreria.append(self)
        print ("\nLibro añadido exitosamente")
    
    #Método para prestar un libro si el mismo está disponible
    def prestar(self):
        if self.__disponible == True:
            self.__disponible = False
            print("Libro prestado exitosamente")
        else:
            print("Libro no disponible")

    #Método para devolver un libro si el mismo fue prestado
    def devolver(self):
        if self.__disponible == False:
            self.__disponible = True
            print("Libro devuelto exitosamente")
        else:
            print("Libro ya disponible")

    #Método para mostrar toda la información del objeto
    def mostrar (self) :
        if self.__disponible == True:
            s_disponible = "Si"
        else:
            s_disponible = "No"
        print (f"- Título: {self.__titulo}", end=" ")
        print (f"- Autor: {self.__autor}", end=" ")
        print (f"- ISBN: {self.__isbn}", end=" ")
        print (f"- Disponible: {s_disponible}")

    #Getter para las busquedas de ISBN de los objetos
    def get_isbn(self):
        return self.__isbn
    


#Declaración inicial de una lista vacía
libreria = []

#Funcion para buscar el indice del libro según el ISBN en la lista
def buscar_indice(isbn):
    for indice, libros in enumerate(libreria):
        if libros.get_isbn() == isbn:
            return indice
    print("Libro no encontrado")
    return None
        
#Funcion para prestar un libro de la lista buscando por ISBN
def prestar_libro (isbn) :
    indice = buscar_indice(isbn)
    if indice != None:
        libreria[indice].prestar()

#Funcion para devolver un libro de la lista buscando por ISBN
def devolver_libro (isbn) :
    indice = buscar_indice(isbn)
    if indice != None:
        libreria[indice].devolver()
    
#Funcion para mostrar la información de cada objeto dentro de la lista
def mostrar_libros():
    for libros in libreria:
        libros.mostrar()

#Funcion para buscar un elemento dentro de la lista según su ISBN
def buscar_libro(isbn):
    indice = buscar_indice(isbn)
    if indice != None:
        libreria[indice].mostrar()

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
    opcion = input("\nOpción elegida: ")
    if opcion.isdigit():
        opcion = int(opcion)
    else:
        opcion = -1

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