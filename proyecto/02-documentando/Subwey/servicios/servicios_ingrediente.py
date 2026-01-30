# application/servicios_ingrediente.py
# Implementa la lógica del programa, coordinando las operaciones entre el frontend y el backend. (El menú y el repositorio)
# Verifica que las variables están en un formato correcto y si no hay errores llama al repositorio para manejar la base de datos
from Subwey.entidades.ingrediente import Ingrediente
from Subwey.backend.repositorio_ingrediente import RepositorioIngrediente

class ServicioIngrediente:
    def __init__(self, repo):
        self._repo = repo

    # Añade un ingrediente a la lista, el stock es opcional, si no se pone nada por defecto valdrá 0
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

    # Aumenta el stock de ingrediente en una cantidad específica
    def reponer_ingrediente(self, nombre, cantidad):
        ingrediente = self._repo.obtener_por_nombre(nombre.lower())
        if ingrediente is None:
            raise ValueError("No existe un ingrediente con ese nombre")
        ingrediente.reponer(cantidad)

    # Decrementa el stock de ingrediente en una cantidad específica
    def consumir_ingrediente(self, nombre, cantidad):
        ingrediente = self._repo.obtener_por_nombre(nombre.lower())
        if ingrediente is None:
            raise ValueError("No existe un ingrediente con ese nombre")
        ingrediente.consumir(cantidad)
    
    # Elimina un ingrediente de la lista
    def eliminar_ingrediente(self, nombre):
        if self._repo.obtener_por_nombre(nombre.lower()) is None:
            raise ValueError("El ingrediente no existe.")
        self._repo.eliminar_por_nombre(nombre)

    # Muestra todos los ingredientes que existen actualmente en la lista
    def listar_ingredientes(self):
        return sorted(self._repo.lista_ingredientes())
