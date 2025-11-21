class Libro:
    def __init__(self, titulo, autor, disponible = True):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible
    def __str__(self):
        return f'{self.titulo}: {self.disponible}'

