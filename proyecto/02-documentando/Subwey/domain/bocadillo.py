# domain/bocadillo.py

from Subwey.domain.ingrediente import Ingrediente
class Bocadillo:

    def __init__(self, nombre, ingredientes):
        self._nombre = nombre
        self._ingredientes = {}
        self._precio = 0

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        # validar no vacio y sin espacios laterales
        texto = (valor or "").strip()
        if not texto:
            raise ValueError("El nombre no puede estar vacio.")
        self._nombre = texto

    @property
    def ingredientes(self):
        return self._ingredientes
    
    @ingredientes.setter
    def ingredientes(self, valor):
        # validar que el diccionario no esté vacío
        lista = (valor or "").strip()
        if not lista:
            raise ValueError("No se puede hacer un bocadillo sin ingredientes.")
        self._ingredientes = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        # validar precio > 0
        if valor <= 0:
            raise ValueError("El precio no puede ser menor que cero.")

    def disponible(self):
         return "Agotado" if self._stock == 0 else "Disponible"