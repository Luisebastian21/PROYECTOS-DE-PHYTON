import os
import shutil

def listar_archivos(directorio):
    """Lista los archivos y carpetas en el directorio especificado."""
    try:
        contenido = os.listdir(directorio)
        print(f"\nContenido de: {directorio}")
        for item in contenido:
            ruta = os.path.join(directorio, item)
            if os.path.isdir(ruta):
                print(f"[Carpeta] {item}")
            else:
                print(f"[Archivo] {item}")
    except FileNotFoundError:
        print("El directorio no existe.")
    except PermissionError:
        print("No tienes permiso para acceder a este directorio.")

def mover_archivo(origen, destino):
    """Mueve un archivo de un directorio a otro."""
    try:
        shutil.move(origen, destino)
        print(f"Archivo movido de {origen} a {destino}")
    except FileNotFoundError:
        print("El archivo o directorio no existe.")
    except PermissionError:
        print("No tienes permiso para realizar esta acción.")

def renombrar_archivo(ruta, nuevo_nombre):
    """Renombra un archivo o carpeta."""
    try:
        nueva_ruta = os.path.join(os.path.dirname(ruta), nuevo_nombre)
        os.rename(ruta, nueva_ruta)
        print(f"Renombrado: {ruta} -> {nuevo_nombre}")
    except FileNotFoundError:
        print("El archivo no existe.")
    except PermissionError:
        print("No tienes permiso para realizar esta acción.")

def eliminar_archivo(ruta):
    """Elimina un archivo o carpeta."""
    try:
        if os.path.isdir(ruta):
            shutil.rmtree(ruta)
            print(f"Carpeta eliminada: {ruta}")
        else:
            os.remove(ruta)
            print(f"Archivo eliminado: {ruta}")
    except FileNotFoundError:
        print("El archivo o carpeta no existe.")
    except PermissionError:
        print("No tienes permiso para realizar esta acción.")

# Menú interactivo
if __name__ == '__main__':
    print("Explorador de Archivos")
    directorio = input("Introduce el directorio para explorar: ")
    listar_archivos(directorio)

    while True:
        print("\nOpciones:")
        print("1. Listar archivos")
        print("2. Mover archivo")
        print("3. Renombrar archivo")
        print("4. Eliminar archivo")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            listar_archivos(directorio)
        elif opcion == '2':
            origen = input("Introduce la ruta del archivo a mover: ")
            destino = input("Introduce el destino: ")
            mover_archivo(origen, destino)
        elif opcion == '3':
            ruta = input("Introduce la ruta del archivo a renombrar: ")
            nuevo_nombre = input("Introduce el nuevo nombre: ")
            renombrar_archivo(ruta, nuevo_nombre)
        elif opcion == '4':
            ruta = input("Introduce la ruta del archivo o carpeta a eliminar: ")
            eliminar_archivo(ruta)
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")
