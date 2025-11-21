class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def agregar_libro(self, Libro):
        self.catalago.append(Libro)
    def prestar_libro(self, titulo_libro):
        for libro in self.catalago:
            if libro.titulo == titulo_libro:
                print(libro.titulo)
            else:
                print('No se ha encontrado el libro')
    