from libro import Libro
from biblioteca import Biblioteca

if __name__ == "__main__":
    biblio = Biblioteca()
    libro1 = Libro('Cervantes', 'El Quijote')
    libro2 = Libro('Shakespeare', 'Hamlet')
    biblio.agregar_libro(libro1)
    biblio.agregar_libro(libro2)
    print(biblio)