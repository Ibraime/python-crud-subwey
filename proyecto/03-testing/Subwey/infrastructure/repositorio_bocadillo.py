# infrastructure/repositorio_ingrediente.py
# Se encarga de la persistencia, gestión y verificación de los datos de los bocadillos.

# infrastructure/repositorio_bocadillo.py

from Subwey.domain.bocadillo import Bocadillo
from Subwey.domain.bocadillo import BocadilloPromocion
from Subwey.domain.usuario import Usuario

# Crea 2 bocadillos por defecto usando los ingredientes por defecto.
def crear_bocadillos_iniciales(repo_ingrediente):

    tomate = repo_ingrediente.obtener_por_nombre("tomate")
    aguacate = repo_ingrediente.obtener_por_nombre("aguacate")
    queso = repo_ingrediente.obtener_por_nombre("queso")

    bocadillos = {}

    if tomate and aguacate:
        vegetal = Bocadillo("vegetal", [tomate, aguacate])
        bocadillos[vegetal.nombre.lower()] = vegetal

    if tomate and queso:
        caprese = Bocadillo("caprese", [tomate, queso])
        bocadillos[caprese.nombre.lower()] = caprese

    return bocadillos


class RepositorioBocadillo:

    def __init__(self, repo_ingrediente):
        self._bocadillos = crear_bocadillos_iniciales(repo_ingrediente)

    # Añade un bocadillo a la lista
    def guardar(self, nombre, ingredientes, descuento=None, autor="Anónimo"):
        nombre = nombre.strip().lower()
        if nombre in self._bocadillos:
            raise ValueError("Ya existe un bocadillo con ese nombre.")

        if descuento is not None:
            bocadillo = BocadilloPromocion(nombre, ingredientes, descuento, autor)
        else:
            bocadillo = Bocadillo(nombre, ingredientes, autor)

        self._bocadillos[nombre] = bocadillo
        return bocadillo
    
    # Obtiene el bocadillo correspondiente al nombre
    def obtener_por_nombre(self, nombre):

        nombre = nombre.strip().lower()

        if nombre in self._bocadillos:
            return self._bocadillos[nombre]
        return None
    
    # Modifica los ingredientes del bocadillo
    def modificar_ingredientes(self, nombre, ingredientes):
        nombre = nombre.strip().lower()
        bocadillo = self._bocadillos.get(nombre)
        if not bocadillo:
            raise ValueError("Bocadillo no existe.")
        bocadillo.ingredientes = ingredientes
        return bocadillo


    # Elimina un bocadillo de la lista
    def eliminar(self, nombre):

        nombre = nombre.strip().lower()

        if nombre not in self._bocadillos:
            raise ValueError("El bocadillo no existe.")

        self._bocadillos.pop(nombre)

    # Muestra todos los bocadillos que existen actualmente en la lista
    def listar(self):

        if not self._bocadillos:
            return "(No hay bocadillos registrados)"

        return sorted(self._bocadillos.values(), key=lambda b: b.nombre)
    
    # Comprueba si el bocadillo es promocional
    def es_promocional(self, nombre):
        bocadillo = self.obtener_por_nombre(nombre)

        if bocadillo and bocadillo.es_promocional():
            return True
        else:
            return False
    
    # Crea 3 usuarios por defecto, no haría un repositorio_usuario aún solo para esto
    def crear_usuarios_iniciales(self):
        return [
            Usuario("Anónimo"),
            Usuario("Oficial"),
            Usuario("usuario_test")
        ]
