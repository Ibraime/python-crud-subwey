# infrastructure/repositorio_ingrediente.py
"""
Módulo que define el repositorio de bocadillos.

Se encarga de la persistencia en memoria, creación, consulta
y eliminación de bocadillos, incluyendo versiones promocionales.
"""

from Subwey.domain.bocadillo import Bocadillo, BocadilloPromocion
from Subwey.domain.usuario import Usuario


def crear_bocadillos_iniciales(repo_ingrediente):
    """
    Crea un conjunto inicial de bocadillos utilizando
    los ingredientes disponibles en el repositorio.

    :param repo_ingrediente: Repositorio de ingredientes.
    :return: Diccionario de bocadillos indexados por nombre.
    """
    tomate = repo_ingrediente.obtener_por_nombre("tomate")
    aguacate = repo_ingrediente.obtener_por_nombre("aguacate")
    queso = repo_ingrediente.obtener_por_nombre("queso")

    bocadillos = {}

    # Solo se crean si los ingredientes existen en el sistema
    if tomate and aguacate:
        vegetal = Bocadillo("vegetal", [tomate, aguacate])
        bocadillos[vegetal.nombre.lower()] = vegetal

    if tomate and queso:
        caprese = Bocadillo("caprese", [tomate, queso])
        bocadillos[caprese.nombre.lower()] = caprese

    return bocadillos


class RepositorioBocadillo:
    """
    Repositorio en memoria para la gestión de bocadillos.

    Permite crear, consultar, modificar y eliminar bocadillos,
    incluyendo versiones promocionales.
    """

    def __init__(self, repo_ingrediente):
        """
        Inicializa el repositorio con bocadillos por defecto.

        :param repo_ingrediente: Repositorio de ingredientes.
        """
        self._bocadillos = crear_bocadillos_iniciales(repo_ingrediente)

    def guardar(self, nombre, ingredientes, descuento=None, autor=None):
        """
        Guarda un nuevo bocadillo en el repositorio.

        Si se indica descuento, se crea como BocadilloPromocion.

        :param nombre: Nombre del bocadillo.
        :param ingredientes: Lista de ingredientes.
        :param descuento: Porcentaje de descuento (opcional).
        :param autor: Usuario autor (opcional).
        :return: Bocadillo creado.
        :raises ValueError: Si ya existe un bocadillo con ese nombre.
        """
        nombre = nombre.strip().lower()

        if nombre in self._bocadillos:
            raise ValueError("Ya existe un bocadillo con ese nombre.")

        if descuento is not None:
            bocadillo = BocadilloPromocion(nombre, ingredientes, descuento, autor)
        else:
            bocadillo = Bocadillo(nombre, ingredientes, autor)

        self._bocadillos[nombre] = bocadillo
        return bocadillo

    def obtener_por_nombre(self, nombre):
        """
        Obtiene un bocadillo por su nombre.

        :param nombre: Nombre del bocadillo.
        :return: Bocadillo o None si no existe.
        """
        nombre = nombre.strip().lower()
        return self._bocadillos.get(nombre)

    def modificar_ingredientes(self, nombre, ingredientes):
        """
        Modifica los ingredientes de un bocadillo existente.

        :param nombre: Nombre del bocadillo.
        :param ingredientes: Nueva lista de ingredientes.
        :return: Bocadillo actualizado.
        :raises ValueError: Si el bocadillo no existe.
        """
        nombre = nombre.strip().lower()
        bocadillo = self._bocadillos.get(nombre)

        if not bocadillo:
            raise ValueError("Bocadillo no existe.")

        bocadillo.ingredientes = ingredientes
        return bocadillo

    def eliminar(self, nombre):
        """
        Elimina un bocadillo del repositorio.

        :param nombre: Nombre del bocadillo.
        :raises ValueError: Si el bocadillo no existe.
        """
        nombre = nombre.strip().lower()

        if nombre not in self._bocadillos:
            raise ValueError("El bocadillo no existe.")

        self._bocadillos.pop(nombre)

    def listar(self):
        """
        Devuelve una lista ordenada de bocadillos por nombre.

        :return: Lista de objetos Bocadillo.
        """
        return sorted(self._bocadillos.values(), key=lambda b: b.nombre)

    def es_promocional(self, nombre):
        """
        Indica si un bocadillo es promocional.

        :param nombre: Nombre del bocadillo.
        :return: True si es promocional, False en caso contrario.
        """
        bocadillo = self.obtener_por_nombre(nombre)
        return bocadillo.es_promocional() if bocadillo else False

    def crear_usuarios_iniciales(self):
        """
        Crea usuarios por defecto para pruebas del sistema.

        :return: Lista de objetos Usuario.
        """
        return [
            Usuario("Anónimo"),
            Usuario("Oficial"),
            Usuario("usuario_test"),
        ]