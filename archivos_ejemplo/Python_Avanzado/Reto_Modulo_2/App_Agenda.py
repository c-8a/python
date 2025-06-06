import re

from Python_Memos.archivos_ejemplo.Python_Avanzado.Reto_Modulo_2.Clase_Contactos import Contacto
from Python_Memos.archivos_ejemplo.Python_Avanzado.Reto_Modulo_2.Clase_Gestion_contactos import GestionContactos


class MenuAgenda:

    def __init__(self):
        self.gestion_contactos = GestionContactos()

    def validar_nombre(self, nombre):
        # patron = r"^(?:[A-Za-z][a-z]*\s?)+$"
        patron = r"^([A-Za-z][a-z]*\s{1})+(\b[A-Za-z][a-z]+\b)"
        return bool(re.fullmatch(patron, nombre))

    def validar_telefono(self, telefono):
        # Expresión regular que permite un "+" opcional al inicio, seguido de dígitos.
        # Puedes ajustar la expresión regular para permitir otros caracteres (espacios, guiones, etc.)
        # si tus requisitos son más amplios.
        patron = r"^\+?\d{1,3}\s?\d{8,9}$"
        return bool(re.fullmatch(patron, telefono))

    def validar_email(self, email):
        # Patrón de expresión regular para validar correos electrónicos (versión común y práctica)
        # ^                    -> Inicio de la cadena
        # [a-zA-Z0-9._%+-]+    -> Parte local: letras, números y caracteres ._%+- (al menos uno)
        # @                    -> El símbolo @ literal
        # [a-zA-Z0-9.-]+       -> Nombre de dominio: letras, números y caracteres .- (al menos uno)
        # \.                   -> El punto literal que separa el dominio del TLD
        # [a-zA-Z]{2,}         -> TLD (Top-Level Domain): al menos dos letras
        # $                    -> Fin de la cadena
        patron = r"^[\w+-]+\.?[\w+-]+@[a-zA-Z0-9-]+(\.[a-zA-Z]{2,}){1,2}$"
        if re.match(patron, email):
            return True
        else:
            return False

    def appAgenda(self):
        print("Agenda de contactos")
        while True:
            print("""\t\tOpciones:
            1. Agregar Contacto.
            2. Mostrar agenda de Contactos.
            3. Buscar un Contacto.
            4. Eliminar un contacto.
            5. Salir de la aplicación.""")
            try:
                opcion = int(input("Ingrese una opción: "))
                if opcion == 1:
                    nombre = input("Ingrese nombre :")
                    while not self.validar_nombre(nombre):
                        print(f"El nombre: {nombre} es incorrecto.")
                        nombre = input("Ingrese nombre: ")

                    telefono = input("Ingrese teléfono (con código de país): ")
                    while not self.validar_telefono(telefono):
                        print(f"El numero: {telefono} es incorrecto.")
                        telefono = input("Ingrese teléfono (con código de país): ")

                    email = input("Ingrese email: ")
                    while not self.validar_email(email):
                        print(f"El email: {email} es incorrecto.")
                        email = input("Ingrese email: ")

                    contacto = Contacto(nombre, telefono, email)
                    self.gestion_contactos.agregar_contacto(contacto)
                elif opcion == 2:
                    self.gestion_contactos.mostrar_contactos()
                elif opcion == 3:
                    nombre = input("Ingrese nombre :")
                    self.gestion_contactos.buscar_contacto(nombre)
                elif opcion == 4:
                    nombre = input("Ingrese nombre :")
                    self.gestion_contactos.eliminar_contacto(nombre)
                elif opcion == 5:
                    print("Gracias por utilizar la agenda")
                    break
                else:
                    print("Opción incorrecta, intente de nuevo")
            except KeyboardInterrupt:
                print("Proceso interrumpido por el usuario")
                break
            except Exception as e:
                print(f"Ha ocurrido un error: {e}")

if __name__ == "__main__":
    agenda = MenuAgenda()
    agenda.appAgenda()
