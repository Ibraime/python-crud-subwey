# presentation/menu_bocadillos.py
# Maneja la interacción con el usuario mediante un menú en consola.
# Se accede a él desde el menú de ingredientes
# presentation/menu_bocadillos.py

from Subwey.domain.usuario import Usuario
from Subwey.domain.bocadillo import BocadilloPromocion

USUARIOS_PREDETERMINADOS = [
    Usuario("Anónimo"),
    Usuario("Oficial"),
    Usuario("usuario_test")
]


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

    seleccionados = []

    while True:
        print("\nIngredientes disponibles:")
        for indice, (nombre, precio, stock) in enumerate(ingredientes_disponibles, start=1):
            marcado = "(✔)" if any(i.nombre == nombre for i in seleccionados) else ""
            print(f"{indice}. {nombre:<10} - {precio:<5.2f}€ - {stock:<5.2f} unidades {marcado}")

        eleccion = input("\nElige el número del ingrediente que quieres añadir al bocadillo ('fin' para terminar): ").strip()

        if eleccion.lower() == "fin":
            break

        if not eleccion.isdigit():
            print("X Debes escribir un número válido.")
            continue

        indice = int(eleccion) - 1
        if not (0 <= indice < len(ingredientes_disponibles)):
            print("X Número fuera de rango.")
            continue

        nombre_sel = ingredientes_disponibles[indice][0]
        ingrediente = servicio_ingrediente.buscar_por_nombre(nombre_sel)

        if ingrediente in seleccionados:
            seleccionados.remove(ingrediente)
            print(f"X {ingrediente.nombre} eliminado de la selección.")
        else:
            seleccionados.append(ingrediente)
            print(f"✔ {ingrediente.nombre} añadido.")

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

                autor_nombre = input("Elige el autor (Oficial - usuario_test - Anónimo): ").strip() or "Anónimo"

                autor = next(
                    (usuario for usuario in USUARIOS_PREDETERMINADOS if usuario.nombre.lower() == autor_nombre.lower()),
                    USUARIOS_PREDETERMINADOS[0]  # por defecto se establece a anónimo
                )

                 # Promo
                promo = input("¿Es promocional? (s/n): ").strip().lower() == "s"
                descuento = None
                if promo:
                    descuento = float(input("Introduce el porcentaje descuento (0-90)%: ").strip())

                # Crear bocadillo usando el servicio
                boc = servicio_bocadillo.crear_bocadillo(nombre, ingredientes, descuento)
                boc.autor = autor

                print(f"✔ Bocadillo '{boc.nombre}' creado por {autor.nombre}.")
                print(f"Precio total: {boc.precio:.2f}€")

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

                # Definir ancho fijo para el campo de nombre + promo
                ancho_nombre = 30

                for bocadillo in bocadillos:
                    ingredientes = [i.nombre for i in bocadillo.ingredientes]
                    autor = getattr(bocadillo, "autor", "Anónimo")

                    if isinstance(bocadillo, BocadilloPromocion):
                        promo_mark = f"[PROMO {bocadillo.descuento}%] "
                    else:
                        # Espacio en blanco para mantener alineación con los que no tienen promo
                        promo_mark = " " * 14  

                    nombre_formateado = f"{promo_mark}{bocadillo.nombre}"
                    print(f"{nombre_formateado:<{ancho_nombre}} - {bocadillo.precio:<5.2f}€ - {', '.join(ingredientes)} - Autor: {autor}")

            # 5. Volver al menú de ingredientes
            elif opcion == "5":
                print("Volviendo al menú anterior.")
                break

            else:
                print("Opción no válida.")

        except ValueError as e:
            print("X " + str(e))
