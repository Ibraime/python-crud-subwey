# presentation/menu_ingredientes.py
from Subwey.servicios.servicios_ingrediente import ServicioIngrediente
from Subwey.backend.repositorio_ingrediente import RepositorioIngrediente

def mostrar_menu():
    print("\n=== SUBWEY ===")
    print("1. Registrar ingrediente")
    print("2. Consumir ingrediente")
    print("3. Reponer ingrediente")
    print("4. Eliminar ingrediente")
    print("5. Listar ingredientes")
    print("6. Salir")

def main():
    repo = RepositorioIngrediente()
    servicio = ServicioIngrediente(repo)
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()
        try:
            if opcion == "1":
                nombre = input("Nombre del ingrediente: ").strip()
                precio = float(input("Precio: ").strip())
                stock = input("Stock: ").strip()
                if not stock:
                    stock = 0
                servicio.registrar_ingrediente(nombre,precio,float(stock))
                print("✔ Ingrediente registrado correctamente.")
            elif opcion == "2":
                nombre = input("Nombre del ingrediente: ").strip()
                cantidad = float(input("Cantidad a consumir: ").strip())
                servicio.consumir_ingrediente(nombre, cantidad)
            elif opcion == "3":
                nombre = input("Nombre del ingrediente: ").strip()
                cantidad = int(input("Cantidad a reponer: ").strip())
                servicio.reponer_ingrediente(nombre, cantidad)
            elif opcion == "4":
                nombre = input("Nombre del ingrediente: ").strip()
                servicio.eliminar_ingrediente(nombre)
            elif opcion == "5":
                ingredientes = servicio.listar_ingredientes()
                if not ingredientes:
                    print("(No hay ingredientes registrados)")
                else:
                    print("\nListado de ingredientes:")
                    print("")
                    for nombre, precio, stock in ingredientes:
                        print(f"{nombre:<10} - {precio:<5.2f}€ - {stock:<5.2f} unidades")
            elif opcion == "6":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida.")
        except ValueError as e:
            print("X " + str(e))

if __name__ == "__main__":
    main()