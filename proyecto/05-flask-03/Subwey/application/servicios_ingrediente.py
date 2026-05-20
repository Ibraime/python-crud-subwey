# application/servicios_ingrediente.py
"""
Módulo que define el servicio de ingredientes.

Actúa como capa intermedia entre la presentación
y el repositorio de ingredientes.
"""

class ServicioIngrediente:
    """
    Servicio de aplicación para la gestión de ingredientes.

    Encapsula la lógica de negocio y delega la persistencia
    en el repositorio de ingredientes.
    """

    def __init__(self, repo):
        """
        Inicializa el servicio con un repositorio.

        :param repo: Repositorio de ingredientes.
        """
        self._repo = repo

    def registrar_ingrediente(self, nombre, precio, stock):
        """
        Registra un nuevo ingrediente.

        :param nombre: Nombre del ingrediente.
        :param precio: Precio del ingrediente.
        :param stock: Cantidad inicial disponible.
        :return: Ingrediente creado.
        """
        return self._repo.guardar(nombre, precio, stock)

    def reponer_ingrediente(self, nombre, cantidad):
        """
        Aumenta el stock de un ingrediente.

        :param nombre: Nombre del ingrediente.
        :param cantidad: Cantidad a añadir.
        :return: Ingrediente actualizado.
        """
        return self._repo.reponer(nombre, cantidad)

    def consumir_ingrediente(self, nombre, cantidad):
        """
        Reduce el stock de un ingrediente.

        :param nombre: Nombre del ingrediente.
        :param cantidad: Cantidad a consumir.
        :return: Ingrediente actualizado.
        """
        return self._repo.consumir(nombre, cantidad)

    def eliminar_ingrediente(self, nombre):
        """
        Elimina un ingrediente.

        :param nombre: Nombre del ingrediente.
        :return: None
        """
        return self._repo.eliminar(nombre)

    def listar_ingredientes(self):
        """
        Obtiene todos los ingredientes registrados.

        :return: Lista de ingredientes.
        """
        return self._repo.listar()

    def buscar_por_nombre(self, nombre: str):
        """
        Busca un ingrediente por su nombre.

        :param nombre: Nombre del ingrediente.
        :return: Ingrediente o None si no existe.
        """
        return self._repo.obtener_por_nombre(nombre)