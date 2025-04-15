import os.path


class Pelicula:

    def __init__(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre



class ServicioPeliculas:

    NOMBRE_CATALOGO = "Peliculas.txt"

    def agregar_pelicula(self, pelicula):
        with open(self.NOMBRE_CATALOGO, "a", encoding="utf8") as archivo:
            archivo.write(f"{pelicula.get_nombre()}\n")
            print("Pelicula añadida correctamente")

    def listar_peliculas(self):
        with open(self.NOMBRE_CATALOGO, "r", encoding="utf8") as archivo:
            print("--- Catalogo de peliculas ---")
            for line in archivo.readlines():
                print(f"- {line}", end="")

    def eliminar_peliculas(self):
        os.remove(self.NOMBRE_CATALOGO)
        print("Catalogo eliminado")


class AppCatalogoPeliculas:

    def __init__(self):
        self.servicio_peliculas = ServicioPeliculas()

    def app_catalogo(self):
        print("\n*** Menu de catalogo de peliculas ***")
        while True:
            print("""\tOpciones:
            1. Agregar Pelicula
            2. Listar Peliculas
            3. Eliminar Catalogo
            4. Salir\n""")
            try:
                opcion = int(input("Seleccione una opcion: "))
                if opcion == 1:
                    nombre = input("Ingrese el nombre: ")
                    pelicula = Pelicula(nombre)
                    self.servicio_peliculas.agregar_pelicula(pelicula)
                elif opcion == 2:
                    self.servicio_peliculas.listar_peliculas()
                elif opcion == 3:
                    self.servicio_peliculas.eliminar_peliculas()
                elif opcion == 4:
                    print("Gracias, vuelva prontos")
                    break
                else:
                    print("Opcion incorrecta, intente nuevamente")
            except ValueError:
                print("Error: introduce un numero válido")
            except Exception as e:
                print(f"Ha ocurrido un error: {e}")

#Programa principal
if __name__ == "__main__":
    catalogo_Peliculas = AppCatalogoPeliculas()
    catalogo_Peliculas.app_catalogo()