# presentation/menu_ingredientes.py
"""
Módulo de presentación que maneja la interacción con el usuario
mediante un menú en consola para gestionar ingredientes.

Permite:
- Registrar, consumir, reponer, eliminar y listar ingredientes.
- Acceder al menú de bocadillos.
"""

from Subwey.application.servicios_ingrediente import ServicioIngrediente
from Subwey.infrastructure.repositorio_ingrediente import RepositorioIngrediente
from Subwey.infrastructure.repositorio_bocadillo import RepositorioBocadillo
from Subwey.application.servicios_bocadillo import ServicioBocadillo
from Subwey.presentation.menu_bocadillos import main_bocadillos 


def mostrar_menu():
    """
    Muestra el menú principal de la aplicación para ingredientes.
    """
    print("\n=== SUBWEY (ingredientes) ===")
    print("1. Registrar ingrediente")
    print("2. Consumir ingrediente")
    print("3. Reponer ingrediente")
    print("4. Eliminar ingrediente")
    print("5. Listar ingredientes")
    print("6. Menú de bocadillos")
    print("7. Salir")


def main():
    """
    Función principal que ejecuta el menú interactivo en consola.

    Inicializa los repositorios y servicios necesarios y mantiene
    un bucle hasta que el usuario decide salir.
    """
    # Inicializa repositorio y servicio de ingredientes
    repo = RepositorioIngrediente()
    servicio = ServicioIngrediente(repo)

    # Inicializa repositorio y servicio de bocadillos
    # para mantener consistencia de datos al cambiar de menú
    repo_bocadillo = RepositorioBocadillo(repo)
    servicio_bocadillo = ServicioBocadillo(repo_bocadillo)

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        try:
            # 1. Registrar ingrediente
            if opcion == "1":
                nombre = input("Nombre del ingrediente: ").strip()
                precio = float(input("Precio: ").strip())
                stock = input("Stock: ").strip()
                if not stock:
                    stock = 0
                servicio.registrar_ingrediente(nombre, precio, float(stock))
                print("✔ Ingrediente registrado correctamente.")

            # 2. Consumir ingrediente
            elif opcion == "2":
                nombre = input("Nombre del ingrediente: ").strip()
                cantidad = float(input("Cantidad a consumir: ").strip())
                servicio.consumir_ingrediente(nombre, cantidad)
                print(f"✔ Se consumió el {nombre}")

            # 3. Reponer ingrediente
            elif opcion == "3":
                nombre = input("Nombre del ingrediente: ").strip()
                cantidad = int(input("Cantidad a reponer: ").strip())
                servicio.reponer_ingrediente(nombre, cantidad)
                print(f"✔ Se añadió stock de {nombre}")

            # 4. Eliminar ingrediente
            elif opcion == "4":
                nombre = input("Nombre del ingrediente: ").strip()
                servicio.eliminar_ingrediente(nombre)
                print(f"✔ Se eliminó el {nombre}")

            # 5. Listar ingredientes
            elif opcion == "5":
                ingredientes = servicio.listar_ingredientes()
                if isinstance(ingredientes, list):
                    print("\nListado de ingredientes:\n")
                    for nombre, precio, stock in ingredientes:
                        print(f"{nombre:<10} - {precio:<5.2f}€ - {stock:<5.2f} unidades")
                else:
                    # Mensaje en caso de lista vacía
                    print(ingredientes)

            # 6. Cambiar al menú de bocadillos
            elif opcion == "6":
                print("Cambiando al menú de bocadillos...")
                main_bocadillos(servicio, servicio_bocadillo)

            # 7. Salir del programa
            elif opcion == "7":
                print("Saliendo del programa.")
                break

            # Opción no válida
            else:
                print("Opción no válida.")

        except ValueError as e:
            # Mostrar error al usuario con prefijo X
            print("X " + str(e))


if __name__ == "__main__":
    main()