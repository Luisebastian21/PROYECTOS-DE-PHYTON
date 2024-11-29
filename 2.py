#GESTOR DE BIBLOTECAS (APLICACION)

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True
        
class Autor:
    def __init__(self, nombre):
        self.nombre = nombre


class Usuario:
    def __init__(self, nombre, usuario_id):
        self.nombre = nombre
        self.usuario_id = usuario_id
        self.libros_prestados = []

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, isbn):
        self.libros = [libro for libro in self.libros if libro.isbn != isbn]

    def buscar_libro(self, titulo):
        return [libro for libro in self.libros if titulo.lower() in libro.titulo.lower()]

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def prestar_libro(self, usuario_id, isbn):
        usuario = next((u for u in self.usuarios if u.usuario_id == usuario_id), None)
        libro = next((l for l in self.libros if l.isbn == isbn and l.disponible), None)
        if usuario and libro:
            usuario.libros_prestados.append(libro)
            libro.disponible = False
            return True
        return False

    def devolver_libro(self, usuario_id, isbn):
        usuario = next((u for u in self.usuarios if u.usuario_id == usuario_id), None)
        if usuario:
            libro = next((l for l in usuario.libros_prestados if l.isbn == isbn), None)
            if libro:
                usuario.libros_prestados.remove(libro)
                libro.disponible = True
                return True
        return False
    
# Crear la biblioteca
biblioteca = Biblioteca()

# Crear autores
autor1 = Autor("Gabriel García Márquez")
autor2 = Autor("J.K. Rowling")

# Agregar libros a la biblioteca
libro1 = Libro("Cien años de soledad", autor1, "978-3-16-148410-0")
libro2 = Libro("Harry Potter y la piedra filosofal", autor2, "978-0-7432-7350-2")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Registrar usuarios
usuario1 = Usuario("Luis Patersini", 1)
usuario2 = Usuario("Ana González", 2)
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Buscar libros
libros_encontrados = biblioteca.buscar_libro("Harry Potter")
for libro in libros_encontrados:
    print(f"Libro encontrado: {libro.titulo} por {libro.autor.nombre}")

# Prestar un libro
if biblioteca.prestar_libro(1, "978-0-7432-7350-2"):
    print("Libro prestado exitosamente.")
else:
    print("No se pudo prestar el libro.")

# Devolver un libro
if biblioteca.devolver_libro(1, "978-0-7432-7350-2"):
    print("Libro devuelto exitosamente.")
else:
    print("No se pudo devolver el libro.")


