# domain/bocadillo.py
"""
Módulo que define las entidades Bocadillo y BocadilloPromocion.

Un bocadillo está compuesto por un nombre, una lista de ingredientes
y un autor. La versión promocional aplica un descuento sobre el precio total.
"""

from Subwey.domain.ingrediente import Ingrediente
from Subwey.domain.usuario import Usuario


class Bocadillo:
    """
    Representa un bocadillo compuesto por una lista de ingredientes.

    :param nombre: Nombre del bocadillo.
    :param ingredientes: Lista de objetos Ingrediente.
    :param autor: Usuario autor del bocadillo.
    """

    def __init__(self, nombre, ingredientes, autor=None):
        # El autor es Anónimo por defecto
        if autor is None:
            autor = Usuario("Anónimo")

        self.nombre = nombre
        self.ingredientes = ingredientes
        self.autor = autor

    @property
    def nombre(self):
        """Devuelve el nombre del bocadillo."""
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        """
        Establece el nombre del bocadillo.

        :raises ValueError: Si el nombre está vacío.
        """
        texto = (nombre or "").strip()
        if not texto:
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = texto

    @property
    def ingredientes(self):
        """Devuelve la lista de ingredientes del bocadillo."""
        return self._ingredientes

    @ingredientes.setter
    def ingredientes(self, ingredientes):
        """
        Establece los ingredientes del bocadillo.

        :raises TypeError: Si no es una lista de Ingrediente.
        :raises ValueError: Si está vacía o contiene repetidos.
        """
        if not isinstance(ingredientes, list):
            raise TypeError("Los ingredientes deben ser una lista.")

        if not ingredientes:
            raise ValueError("El bocadillo debe tener al menos un ingrediente.")

        for ingrediente in ingredientes:
            if not isinstance(ingrediente, Ingrediente):
                raise TypeError(
                    "Todos los elementos deben ser objetos tipo Ingrediente."
                )

        # Comprobamos repetidos usando set().
        if len(ingredientes) != len(set(ingredientes)):
            raise ValueError("No se permiten ingredientes repetidos.")

        self._ingredientes = ingredientes

    @property
    def autor(self):
        """Devuelve el usuario autor del bocadillo."""
        return self._autor

    @autor.setter
    def autor(self, autor):
        """
        Establece el autor del bocadillo.

        :raises TypeError: Si no es un objeto Usuario.
        """
        if not isinstance(autor, Usuario):
            raise TypeError("El autor debe ser un usuario.")

        self._autor = autor

    @property
    def precio(self):
        """
        Calcula el precio total del bocadillo como la suma
        de los precios de sus ingredientes.
        """
        return float(sum(ingrediente.precio for ingrediente in self._ingredientes))

    def es_promocional(self):
        """
        Indica si el bocadillo es promocional.

        :return: False en la clase base.
        """
        return False


class BocadilloPromocion(Bocadillo):
    """
    Representa un bocadillo promocional que aplica un descuento
    porcentual sobre el precio total.

    :param descuento_porcentaje: Porcentaje de descuento (1–90).
    """

    def __init__(self, nombre, ingredientes, descuento_porcentaje=10, autor=None):
        super().__init__(nombre, ingredientes, autor)

        if not (1 <= descuento_porcentaje <= 90):
            raise ValueError("El descuento debe estar entre 1 y 90.")

        self._descuento = descuento_porcentaje

    @property
    def descuento(self):
        """Devuelve el porcentaje de descuento aplicado."""
        return self._descuento

    @descuento.setter
    def descuento(self, descuento):
        """
        Establece el porcentaje de descuento.

        :raises ValueError: Si el descuento no está entre 1 y 90.
        """
        if not (1 <= descuento <= 90):
            raise ValueError("El descuento debe estar entre 1 y 90.")

        self._descuento = descuento

    @property
    def precio(self):
        """
        Devuelve el precio final aplicando el descuento al precio base.
        """
        precio_base = super().precio
        return precio_base * (1 - self._descuento / 100)

    def es_promocional(self):
        """
        Indica que el bocadillo es promocional.

        :return: True.
        """
        return True
