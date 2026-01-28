# application/servicios_ingrediente.py
from Subwey.entidades.ingrediente import Ingrediente
from Subwey.backend.repositorio_ingrediente import RepositorioIngrediente

class ServicioIngrediente:
    def __init__(self, repo):
        self._repo = repo

    def registrar_ingrediente(self, nombre, precio, stock=0):
        if self._repo.obtener_por_nombre(nombre.lower()) is not None:
            raise ValueError("Ya existe un ingrediente con ese nombre.")
        if precio <= 0 or precio is None:
            raise ValueError("El precio es inválido.")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        ingrediente = Ingrediente(nombre.lower(), precio, stock)
        self._repo.guardar(ingrediente)
        pass

    def reponer_ingrediente(self, nombre, cantidad):
        ingrediente = self._repo.obtener_por_nombre(nombre.lower())
        if ingrediente is None:
            raise ValueError("No existe un ingrediente con ese nombre")
        ingrediente.reponer(cantidad)

    def consumir_ingrediente(self, nombre, cantidad):
        ingrediente = self._repo.obtener_por_nombre(nombre.lower())
        if ingrediente is None:
            raise ValueError("No existe un ingrediente con ese nombre")
        ingrediente.consumir(cantidad)
    
    def eliminar_ingrediente(self, nombre):
        if self._repo.obtener_por_nombre(nombre.lower()) is None:
            raise ValueError("El ingrediente no existe.")
        self._repo.eliminar_por_nombre(nombre)

    def listar_ingredientes(self):
        return sorted(self._repo.lista_ingredientes())
