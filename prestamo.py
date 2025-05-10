# Lista vacia
libros = []

def ingresar_libro():
    print("\n--- Ingresar un nuevo libro ---")
    nombre = input("Nombre del libro: ")
    editorial = input("Editorial: ")
    año = input("Año de publicación: ")
    genero = input("Género: ")

    libro = {
        "nombre": nombre,
        "editorial": editorial,
        "año": año,
        "género": genero,
        "prestado": False
    }

    libros.append(libro)
    print()
    print(f"📚 Libro '{nombre}' agregado exitosamente.")


# Menu de libros
def menu():
    while True:
        print("\n📖 Sistema de Préstamos de Libros")
        print("1. Ingresar un libro")
        print("2. Mostrar libros")
        print("3. Prestar un libro")
        print("4. Devolver un libro")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            ingresar_libro()
        elif opcion == "2":
            print("Función para mostrar un libro")
        elif opcion == "3":
            print("Función para prestar un libro")
        elif opcion == "4":
            print("Función para devolver un libro")
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")