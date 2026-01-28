# infrastructure/repositorio_memoria.py

from Subwey.entidades.ingrediente import Ingrediente


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

    def guardar(self, ingrediente):
        self._ingredientes[ingrediente.nombre().lower()] = ingrediente

    def obtener_por_nombre(self, nombre):
        nombre = nombre.strip()
        if not nombre:
            return None

        if nombre.lower() in self._ingredientes.keys():
            return self._ingredientes[nombre.lower()]
        else:
            return None
    
    def eliminar_por_nombre(self, nombre):
        self._ingredientes.pop(nombre.lower())

    def lista_ingredientes(self):
        return [(ingrediente.nombre(), ingrediente.precio(), ingrediente.stock() ) for ingrediente in self._ingredientes.values()]