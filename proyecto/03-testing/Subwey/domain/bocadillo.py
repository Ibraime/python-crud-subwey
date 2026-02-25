# domain/bocadillo.py

from Subwey.domain.ingrediente import Ingrediente
from Subwey.domain.usuario import Usuario

class Bocadillo:

    def __init__(self, nombre, ingredientes, autor=Usuario("Anónimo")):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.autor = autor

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        texto = (valor or "").strip()
        # validar que el nombre no está vacío
        if not texto:
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = texto

    @property
    def ingredientes(self):
        return self._ingredientes
    
    @ingredientes.setter
    def ingredientes(self, valor):
        # validar que es una lista
        if not isinstance(valor, list):
            raise TypeError("Los ingredientes deben ser una lista.")
        # validar que la lista no está vacía
        if not valor:
            raise ValueError("El bocadillo debe tener al menos un ingrediente.")
        # validar que todos los elementos son ingredientes
        for ingrediente in valor:
            if not isinstance(ingrediente, Ingrediente):
                raise TypeError("Todos los elementos deben ser objetos tipo Ingrediente.")

        # evitar repetidos
        if len(valor) != len(set(valor)):
            raise ValueError("No se permiten ingredientes repetidos.")

        self._ingredientes = valor
    
    @property
    def autor(self):
        return self._autor
    
    @autor.setter
    def autor(self, valor):
        
        # validar que es un usuario
        if not isinstance(valor, Usuario):
            raise TypeError("El autor debe ser un usuario.")
        
        # validar que el usuario no está vacío
        if not valor:
            raise ValueError("Autor no puede estar vacío.")
        
        self._autor = valor


    @property
    def precio(self):
        return sum(ingrediente.precio for ingrediente in self._ingredientes)
    
    # Indica si el bocadillo es promocional o no
    def es_promocional(self):
        return False


# Bocadillo que aplica un descuento sobre el precio total de sus ingredientes.
class BocadilloPromocion(Bocadillo):

    # Crea un bocadillo añadiendo el descuento por la promoción
    def __init__(self, nombre, ingredientes, descuento=10, autor=Usuario("Anónimo")):
        super().__init__(nombre, ingredientes,autor)
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
    
    def es_promocional(self):
        return True
