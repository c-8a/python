class Contacto:

    def __init__(self, nombre, telefono, email):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__email = email

    def __str__(self):
        return (f"{self.__nombre}\n"
                f"{self.__telefono}\n"
                f"{self.__email}\n")

    def get_nombre(self):
        return self.__nombre

    def get_telefono(self):
        return self.__telefono

    def get_email(self):
        return self.__email


