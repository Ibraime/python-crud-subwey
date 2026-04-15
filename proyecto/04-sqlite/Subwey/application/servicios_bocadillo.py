# application/servicios_bocadillo.py
"""
Módulo que define el servicio de bocadillos.

Actúa como capa intermedia entre la presentación
y el repositorio de bocadillos.
"""

class ServicioBocadillo:
    """
    Servicio de aplicación para la gestión de bocadillos.

    Encapsula la lógica de negocio y delega la persistencia
    en el repositorio de bocadillos.
    """

    def __init__(self, repo_bocadillo):
        """
        Inicializa el servicio con un repositorio.

        :param repo_bocadillo: Repositorio de bocadillos.
        """
        self._repo = repo_bocadillo

    def crear_bocadillo(self, nombre, ingredientes, descuento=None, autor=None):
        """
        Crea un nuevo bocadillo.

        Puede ser promocional si se indica un descuento.

        :param nombre: Nombre del bocadillo.
        :param ingredientes: Lista de ingredientes.
        :param descuento: Porcentaje de descuento (opcional).
        :param autor: Usuario autor (opcional).
        :return: Bocadillo creado.
        """
        return self._repo.guardar(nombre, ingredientes, descuento, autor)

    def modificar_bocadillo(self, nombre, ingredientes):
        """
        Modifica los ingredientes de un bocadillo existente.

        :param nombre: Nombre del bocadillo.
        :param ingredientes: Nueva lista de ingredientes.
        :return: Bocadillo actualizado.
        """
        return self._repo.modificar_ingredientes(nombre, ingredientes)

    def eliminar_bocadillo(self, nombre):
        """
        Elimina un bocadillo.

        :param nombre: Nombre del bocadillo.
        :return: None
        """
        self._repo.eliminar(nombre)

    def listar_bocadillos(self):
        """
        Obtiene todos los bocadillos registrados.

        :return: Lista de bocadillos.
        """
        return self._repo.listar()

    def obtener_bocadillo(self, nombre):
        """
        Obtiene un bocadillo por su nombre.

        :param nombre: Nombre del bocadillo.
        :return: Bocadillo o None si no existe.
        """
        return self._repo.obtener_por_nombre(nombre)

    def es_promocional(self, nombre):
        """
        Indica si un bocadillo es promocional.

        :param nombre: Nombre del bocadillo.
        :return: True si es promocional, False en caso contrario.
        """
        return self._repo.es_promocional(nombre)