# presentation/menu_ingredientes.py
# Maneja la interacción con el usuario mediante un menú en consola.
# Es el archivo que hay que ejecutar por ahora para que funcione el programa
# Altera la lista de ingredientes con el servicio_ingredientes que a su vez llama a repositorio_ingrediente cuando es necesario
from Subwey.application.servicios_ingrediente import ServicioIngrediente
from Subwey.infrastructure.repositorio_ingrediente import RepositorioIngrediente

from Subwey.infrastructure.repositorio_bocadillo import RepositorioBocadillo
from Subwey.application.servicios_bocadillo import ServicioBocadillo

from Subwey.presentation.menu_bocadillos import main_bocadillos 

def mostrar_menu():
    print("\n=== SUBWEY (ingredientes) ===")
    print("1. Registrar ingrediente")
    print("2. Consumir ingrediente")
    print("3. Reponer ingrediente")
    print("4. Eliminar ingrediente")
    print("5. Listar ingredientes")
    print("6. Menú de bocadillos")
    print("7. Salir")

def main():
    # Inicializa el repositorio y servicio
    repo = RepositorioIngrediente()
    servicio = ServicioIngrediente(repo)

    # También los de bocadillo para que al salir y entrar a ese segundo menú se mantengan los datos
    repo_bocadillo = RepositorioBocadillo(repo)
    servicio_bocadillo = ServicioBocadillo(repo_bocadillo)
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()
        try:
            # 1. Pide los datos mínimos y crea un ingrediente
            if opcion == "1":
                nombre = input("Nombre del ingrediente: ").strip()
                precio = float(input("Precio: ").strip())
                stock = input("Stock: ").strip()
                if not stock:
                    stock = 0
                servicio.registrar_ingrediente(nombre,precio,float(stock))
                print("✔ Ingrediente registrado correctamente.")
            # 2. Especifica que nombre de ingrediente y cantidad para decrementar el stock
            elif opcion == "2":
                nombre = input("Nombre del ingrediente: ").strip()
                cantidad = float(input("Cantidad a consumir: ").strip())
                servicio.consumir_ingrediente(nombre, cantidad)
                print(f"✔ Se consumió el {nombre}")
            # 3. Especifica que nombre de ingrediente y cantidad para aumentar el stock
            elif opcion == "3":
                nombre = input("Nombre del ingrediente: ").strip()
                cantidad = int(input("Cantidad a reponer: ").strip())
                servicio.reponer_ingrediente(nombre, cantidad)
                print(f"✔ Se añadió stock de {nombre}")
            # 4. Especifica que nombre de ingrediente para eliminarlo 
            elif opcion == "4":
                nombre = input("Nombre del ingrediente: ").strip()
                servicio.eliminar_ingrediente(nombre)
                print(f"✔ Se eliminó el {nombre}")
            # 5. Muestra la lista de ingredientes, en caso de que no haya ninguno da un aviso
            elif opcion == "5":
                ingredientes = servicio.listar_ingredientes()
                if isinstance(ingredientes, list):
                    print("\nListado de ingredientes:")
                    print("")
                    for nombre, precio, stock in ingredientes:
                        print(f"{nombre:<10} - {precio:<5.2f}€ - {stock:<5.2f} unidades")
                else:
                    print(ingredientes)
            # 6. Cambia al menú de bocadillos
            elif opcion == "6":
                print("Cambiando al menú de bocadillos...")
                main_bocadillos(servicio, servicio_bocadillo) 
            # 12. Sale del menú finalizando el programa
            elif opcion == "7":
                print("Saliendo del programa.")
                break
            # Si escribe una opción no válida, avisa al usuario y vuelve al bucle
            else:
                print("Opción no válida.")
        # Si ocurre algún error se muestra al usuario con una X a la izquierda
        except ValueError as e:
            print("X " + str(e))

if __name__ == "__main__":
    main()