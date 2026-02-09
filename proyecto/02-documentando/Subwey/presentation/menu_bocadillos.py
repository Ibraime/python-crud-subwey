# presentation/menu_bocadillos.py
# Maneja la interacción con el usuario mediante un menú en consola.
# Se accede a él desde el menú de ingredientes
# presentation/menu_bocadillos.py

def mostrar_menu():
    print("\n=== SUBWEY (bocadillos) ===")
    print("1. Registrar bocadillo")
    print("2. Modificar ingredientes del bocadillo")
    print("3. Eliminar bocadillo")
    print("4. Listar bocadillos")
    print("5. Volver a ingredientes")

# Para modificar y crear bocadillos se eligen los ingredientes que tendrá, sin repetirlos
def elegir_ingredientes(servicio_ingrediente):

    ingredientes_disponibles = servicio_ingrediente.listar_ingredientes()

    if not isinstance(ingredientes_disponibles, list) or not ingredientes_disponibles:
        print("No hay ingredientes disponibles.")
        return []

    print("\nIngredientes disponibles:")
    for nombre, precio, stock in ingredientes_disponibles:
        print(f"{nombre:<10} - {precio:<5.2f}€ - {stock:<5.2f} unidades")

    seleccionados = []

    while True:
        nombre_ing = input("\nIngrediente (o 'fin'): ").strip()

        if nombre_ing.lower() == "fin":
            break

        ingrediente = servicio_ingrediente.buscar_por_nombre(nombre_ing)

        if not ingrediente:
            print("X Ingrediente no encontrado.")
            continue

        if ingrediente in seleccionados:
            print("X Ya añadido.")
            continue

        seleccionados.append(ingrediente)
        print(f"✔ {nombre_ing} añadido.")

    return seleccionados


def main_bocadillos(servicio_ingrediente, servicio_bocadillo):

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        try:

            # 1. Crear Bocadillo
            if opcion == "1":

                nombre = input("Nombre del bocadillo: ").strip()
                ingredientes = elegir_ingredientes(servicio_ingrediente)

                if not ingredientes:
                    print("X No puede crearse sin ingredientes.")
                    continue

                bocadillo = servicio_bocadillo.crear_bocadillo(nombre, ingredientes)

                print(f"✔ Bocadillo '{bocadillo.nombre}' creado.")
                print(f"Precio total: {bocadillo.precio:.2f}€")

            # 2. Modificar ingredientes del bocadillo
            elif opcion == "2":

                nombre = input("Nombre del bocadillo a modificar: ").strip()
                ingredientes = elegir_ingredientes(servicio_ingrediente)

                if not ingredientes:
                    print("X No puede quedar sin ingredientes.")
                    continue

                boc = servicio_bocadillo.modificar_bocadillo(nombre, ingredientes)

                print(f"✔ Bocadillo modificado.")
                print(f"Nuevo precio: {boc.precio:.2f}€")

            # 3. Eliminar bocadillo
            elif opcion == "3":

                nombre = input("Nombre del bocadillo a eliminar: ").strip()
                servicio_bocadillo.eliminar_bocadillo(nombre)

                print("✔ Bocadillo eliminado.")

            # 4. Listar bocadillos
            elif opcion == "4":

                bocadillos = servicio_bocadillo.listar_bocadillos()

                if isinstance(bocadillos, str):
                    print(bocadillos)
                    continue

                print("\nListado de bocadillos:")
                for b in bocadillos:
                    nombres = [i.nombre for i in b.ingredientes]
                    print(f"{b.nombre:<15} - {b.precio:<5.2f}€ - {', '.join(nombres)}")

            # 5. Volver al menú de ingredientes
            elif opcion == "5":
                print("Volviendo al menú anterior.")
                break

            else:
                print("Opción no válida.")

        except ValueError as e:
            print("X " + str(e))
