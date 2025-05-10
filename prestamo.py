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


# Mostrar los libros disponibles
def mostrar_libros():
    if not libros:
        print("\n📚 No hay libros en el sistema.")
        return
    
    print("\n📖 Lista de libros ingresados:")
    for i, libro in enumerate(libros, start=1):
        print(i, ".")
        print("Nombre:", libro["nombre"])
        print("Año:", libro["año"])
        print("Género:", libro["género"])
        print("")

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
            mostrar_libros()
        elif opcion == "3":
            print("Función para prestar un libro")
        elif opcion == "4":
            print("Función para devolver un libro")
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Llamamos a menu() solo después de definir todas las funciones
menu()