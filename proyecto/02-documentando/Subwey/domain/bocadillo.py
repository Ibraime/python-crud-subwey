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
