
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
            print("Función para ingresar un libro")
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