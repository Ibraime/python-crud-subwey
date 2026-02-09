# domain/bocadillo.py

from Subwey.domain.ingrediente import Ingrediente

class Bocadillo:

    def __init__(self, nombre, ingredientes):
        self.nombre = nombre
        self.ingredientes = ingredientes

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        texto = (valor or "").strip()
        if not texto:
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = texto

    @property
    def ingredientes(self):
        return self._ingredientes
    
    @ingredientes.setter
    def ingredientes(self, valor):

        if not isinstance(valor, list):
            raise TypeError("Los ingredientes deben ser una lista.")

        if not valor:
            raise ValueError("El bocadillo debe tener al menos un ingrediente.")

        for ingrediente in valor:
            if not isinstance(ingrediente, Ingrediente):
                raise TypeError("Todos los elementos deben ser objetos tipo Ingrediente.")

        # evitar repetidos
        if len(valor) != len(set(valor)):
            raise ValueError("No se permiten ingredientes repetidos.")

        self._ingredientes = valor

    @property
    def precio(self):
        return sum(ingrediente.precio for ingrediente in self._ingredientes)

# Bocadillo que aplica un descuento sobre el precio total de sus ingredientes.
class BocadilloPromocion(Bocadillo):

    # Crea un bocadillo añadiendo el descuento por la promoción
    def __init__(self, nombre, ingredientes, descuento=10):
        super().__init__(nombre, ingredientes)
        if not (1 <= descuento <= 90):
            raise ValueError("El descuento debe estar entre 1 y 90.")
        self._descuento = descuento

    @property
    def descuento(self):
        return self._descuento

    # Comprueba que no sea un porcentaje negativo o demasiado alto
    @descuento.setter
    def descuento(self, valor):
        if not (1 <= valor <= 90):
            raise ValueError("El descuento debe estar entre 1 y 90.")
        self._descuento = valor

    # Devuelve el precio total con el descuento aplicado.
    @property
    def precio(self):
        precio_base = super().precio
        return precio_base * (1 - self._descuento / 100)
