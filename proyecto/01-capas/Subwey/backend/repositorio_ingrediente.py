# infrastructure/repositorio_memoria.py
# Se encarga de la persistencia y gestión de los datos de los ingredientes.
# No verifica nada salvo obtener_por_nombre(), de eso se encargará el servicio
from Subwey.entidades.ingrediente import Ingrediente

# Crea 3 ingredientes por defecto cuando se ejecuta el programa, para que sea más fácil probar
def crear_ingredientes_iniciales():
    """Devuelve una lista de items iniciales para la maquina."""
    return {
        "tomate":Ingrediente("tomate", 3, 20),
        "aguacate":Ingrediente("aguacate", 7, 8),
        "queso":Ingrediente("queso", 2, 42),
    }

class RepositorioIngrediente:
    def __init__(self):
        self._ingredientes = crear_ingredientes_iniciales()

    # Añade un ingrediente a la lista
    def guardar(self, ingrediente):
        self._ingredientes[ingrediente.nombre().lower()] = ingrediente

    # Obtiene un ingrediente en específico por su nombre
    def obtener_por_nombre(self, nombre):
        nombre = nombre.strip()
        if not nombre:
            return None

        if nombre.lower() in self._ingredientes.keys():
            return self._ingredientes[nombre.lower()]
        else:
            return None
    
    # Elimina un ingrediente de la lista
    def eliminar_por_nombre(self, nombre):
        self._ingredientes.pop(nombre.lower())

    # Muestra todos los ingredientes que existen actualmente en la lista
    def lista_ingredientes(self):
        return [(ingrediente.nombre(), ingrediente.precio(), ingrediente.stock() ) for ingrediente in self._ingredientes.values()]