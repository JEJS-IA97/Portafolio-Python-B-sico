class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def Saludo(self):
        print("Hola, mi nombre es", self.nombre, self.apellido)

class Admin(Usuario):
    def superSaludo(self):
        print("Hola, me llamo", self.nombre, "y soy administrador")

usuario = Usuario("Felipe", "Feliz")
usuario.Saludo()
usuario.nombre = "Chanchito"
usuario.Saludo()

admin = Admin("Super", "Feliz")
admin.Saludo()
admin.superSaludo()

