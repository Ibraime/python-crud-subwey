# infrastructure/repositorio_ingrediente.py
"""
Módulo que define el repositorio de ingredientes.

Se encarga de la persistencia en memoria, gestión y verificación
de los datos relacionados con los ingredientes.
"""

from Subwey.domain.ingrediente import Ingrediente


def crear_ingredientes_iniciales():
    """
    Crea un conjunto inicial de ingredientes por defecto
    para facilitar las pruebas del sistema.

    :return: Diccionario de ingredientes indexados por nombre.
    """
    return {
        "tomate": Ingrediente("tomate", 3, 20),
        "aguacate": Ingrediente("aguacate", 7, 8),
        "queso": Ingrediente("queso", 2, 42),
    }


class RepositorioIngrediente:
    """
    Repositorio en memoria para la gestión de ingredientes.

    Permite crear, consultar, actualizar stock y eliminar ingredientes.
    """

    def __init__(self):
        """Inicializa el repositorio con ingredientes por defecto."""
        self._ingredientes = crear_ingredientes_iniciales()

    def guardar(self, nombre, precio_float, stock_int):
        """
        Guarda un nuevo ingrediente en el repositorio.

        :param nombre: Nombre del ingrediente.
        :param precio_float: Precio unitario.
        :param stock_int: Cantidad inicial disponible.
        :raises ValueError: Si el ingrediente ya existe, o el precio o stock son inválidos.
        """
        nombre = nombre.strip().lower()

        if self.obtener_por_nombre(nombre) is not None:
            raise ValueError("Ya existe un ingrediente con ese nombre.")

        if precio_float is None or precio_float <= 0:
            raise ValueError("El precio es inválido.")

        if stock_int < 0:
            raise ValueError("El stock no puede ser negativo.")

        ingrediente = Ingrediente(nombre, precio_float, stock_int)
        self._ingredientes[nombre] = ingrediente

    def obtener_por_nombre(self, nombre):
        """
        Obtiene un ingrediente por su nombre.

        :param nombre: Nombre del ingrediente.
        :return: Objeto Ingrediente o None si no existe.
        """
        nombre = nombre.strip().lower()
        return self._ingredientes.get(nombre)

    def reponer(self, nombre, cantidad):
        """
        Aumenta el stock de un ingrediente.

        :param nombre: Nombre del ingrediente.
        :param cantidad: Cantidad a añadir.
        :raises ValueError: Si el ingrediente no existe o la cantidad es 0 o negativa.
        """
        ingrediente = self.obtener_por_nombre(nombre)

        if ingrediente is None:
            raise ValueError("No existe un ingrediente con ese nombre.")

        if cantidad <= 0:
            raise ValueError("La cantidad a reponer debe ser mayor que cero.")

        ingrediente.stock += cantidad

    def consumir(self, nombre, cantidad):
        """
        Reduce el stock de un ingrediente.

        :param nombre: Nombre del ingrediente.
        :param cantidad: Cantidad a consumir.
        :raises ValueError: Si no existe, cantidad menor o igual que 0, o no hay stock suficiente.
        """
        ingrediente = self.obtener_por_nombre(nombre)

        if ingrediente is None:
            raise ValueError("No existe un ingrediente con ese nombre.")

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        if cantidad > ingrediente.stock:
            raise ValueError("No se puede consumir: no hay suficiente stock.")

        ingrediente.stock -= cantidad

    def eliminar(self, nombre):
        """
        Elimina un ingrediente del repositorio.

        :param nombre: Nombre del ingrediente.
        :raises ValueError: Si el ingrediente no existe.
        """
        nombre = nombre.strip().lower()

        if self.obtener_por_nombre(nombre) is None:
            raise ValueError("El ingrediente no existe.")

        self._ingredientes.pop(nombre)

    def listar(self):
        """
        Devuelve una lista ordenada de ingredientes disponibles.

        :return: Lista de tuplas (nombre, precio, stock).
        """
        if not self._ingredientes:
            return "(No hay ingredientes registrados)"

        return sorted([(ingrediente.nombre, ingrediente.precio, ingrediente.stock ) for ingrediente in self._ingredientes.values()])