# domain/ingrediente.py
"""
Módulo que define la entidad Ingrediente del dominio.

Un ingrediente tiene nombre, precio y stock disponible.
Incluye validaciones para garantizar la integridad de los datos.
"""


class Ingrediente:
    """
    Representa un ingrediente que puede formar parte de un bocadillo.

    :param nombre: Nombre del ingrediente.
    :param precio_float: Precio unitario del ingrediente (debe ser mayor que 0).
    :param stock_int: Cantidad disponible en stock (no puede ser negativa).
    """

    def __init__(self, nombre, precio_float, stock_int=0):
        self.nombre = nombre
        self.precio = precio_float
        self.stock = stock_int

    @property
    def nombre(self):
        """
        Devuelve el nombre del ingrediente.
        """
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        """
        Establece el nombre del ingrediente.

        El nombre no puede estar vacío ni contener solo espacios.

        :raises ValueError: Si el nombre está vacío.
        """
        texto = (nombre or "").strip()
        if not texto:
            raise ValueError("El nombre no puede estar vacio.")
        self._nombre = texto

    @property
    def stock(self):
        """
        Devuelve la cantidad disponible en stock.
        """
        return self._stock
    
    @stock.setter
    def stock(self, stock):
        """
        Establece la cantidad disponible en stock.

        :raises ValueError: Si el stock es negativo.
        """
        if stock < 0:
            raise ValueError("El stock no puede ser menor que cero.")
        self._stock = stock

    @property
    def precio(self):
        """
        Devuelve el precio unitario del ingrediente.
        """
        return self._precio

    @precio.setter
    def precio(self, precio):
        """
        Establece el precio del ingrediente.

        El precio debe ser mayor que cero.

        :raises ValueError: Si el precio es menor o igual a cero.
        """
        if precio <= 0:
            raise ValueError("El precio no puede ser menor que cero.")
        self._precio = precio

    def disponible(self):
        """
        Indica si el ingrediente está disponible según su stock.

        :return: "Agotado" si el stock es 0, en caso contrario "Disponible".
        """
        return "Agotado" if self._stock == 0 else "Disponible"