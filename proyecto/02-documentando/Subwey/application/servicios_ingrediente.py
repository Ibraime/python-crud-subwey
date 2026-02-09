# application/servicios_ingrediente.py
# Implementa la lógica del programa, coordinando las operaciones entre el frontend y el backend. (El menú y el repositorio)
# Verifica que las variables están en un formato correcto y si no hay errores llama al repositorio para manejar la base de datos
from Subwey.domain.ingrediente import Ingrediente
from Subwey.infrastructure.repositorio_ingrediente import RepositorioIngrediente

class ServicioIngrediente:
    def __init__(self, repo):
        self._repo = repo

    # Añade un ingrediente a la lista
    def registrar_ingrediente(self, nombre, precio, stock):
        return self._repo.guardar(nombre, precio, stock)
    
    # Aumenta el stock de ingrediente en una cantidad específica
    def reponer_ingrediente(self, nombre, cantidad):
        return self._repo.reponer(nombre, cantidad)

    # Decrementa el stock de ingrediente en una cantidad específica
    def consumir_ingrediente(self, nombre, cantidad):
        return self._repo.consumir(nombre, cantidad)
    
    # Elimina un ingrediente de la lista
    def eliminar_ingrediente(self, nombre):
        return self._repo.eliminar(nombre)

    # Muestra todos los ingredientes que existen actualmente en la lista
    def listar_ingredientes(self):
        return self._repo.listar()

    # Obtiene el ingrediente correspondiente al nombre
    def buscar_por_nombre(self, nombre: str):
        return self._repo.obtener_por_nombre(nombre)
