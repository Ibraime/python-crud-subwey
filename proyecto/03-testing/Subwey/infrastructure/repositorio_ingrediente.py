# infrastructure/repositorio_ingrediente.py
# Se encarga de la persistencia, gestión y verificación de los datos de los ingredientes.
from Subwey.domain.ingrediente import Ingrediente

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
    def guardar(self, nombre, precio, stock):
        
        if self.obtener_por_nombre(nombre.lower()) is not None:
            raise ValueError("Ya existe un ingrediente con ese nombre.")
        if precio is None or precio <= 0:
            raise ValueError("El precio es inválido.")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        ingrediente = Ingrediente(nombre.lower(), precio, stock)

        self._ingredientes[ingrediente.nombre.lower()] = ingrediente

    # Obtiene un ingrediente en específico por su nombre
    def obtener_por_nombre(self, nombre):
        nombre = nombre.strip().lower()

        if nombre.lower() in self._ingredientes.keys():
            return self._ingredientes[nombre]
        else:
            return None

    # Aumenta el stock de ingrediente en una cantidad específica
    def reponer(self, nombre, cantidad):
        ingrediente = self.obtener_por_nombre(nombre.lower())
        if ingrediente is None:
            raise ValueError("No existe un ingrediente con ese nombre")
        
        if cantidad <= 0:
            raise ValueError("No se puede reponer una cantidad negativa.")
        else:
            ingrediente._stock += cantidad

    # Decrementa el stock de ingrediente en una cantidad específica
    def consumir(self, nombre, cantidad):
        ingrediente = self.obtener_por_nombre(nombre.lower())
        if ingrediente is None:
            raise ValueError("No existe un ingrediente con ese nombre")
        #ingrediente.consumir(cantidad)

        if cantidad > ingrediente.stock:
            raise ValueError("No se puede consumir: no hay suficiente stock.")
        else:
            ingrediente._stock -= cantidad
    
    # Elimina un ingrediente de la lista
    def eliminar(self, nombre):
        if self.obtener_por_nombre(nombre.lower()) is None:
            raise ValueError("El ingrediente no existe.")
        self._ingredientes.pop(nombre.lower())

    # Muestra todos los ingredientes que existen actualmente en la lista
    def listar(self):
        if not self._ingredientes:
            return "(No hay ingredientes registrados)"
        return sorted([(ingrediente.nombre, ingrediente.precio, ingrediente.stock ) for ingrediente in self._ingredientes.values()])
