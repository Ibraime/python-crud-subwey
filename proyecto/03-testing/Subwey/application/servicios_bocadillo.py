# application/servicios_bocadillo.py

class ServicioBocadillo:

    def __init__(self, repo_bocadillo):
        self._repo = repo_bocadillo

    # Añade un bocadillo a la lista (con o sin descuento)
    def crear_bocadillo(self, nombre, ingredientes, descuento=None, autor=None):
        return self._repo.guardar(nombre, ingredientes, descuento, autor)

    # Modifica los ingredientes del bocadillo
    def modificar_bocadillo(self, nombre, ingredientes):
        return self._repo.modificar_ingredientes(nombre, ingredientes)

    # Elimina un bocadillo de la lista
    def eliminar_bocadillo(self, nombre):
        self._repo.eliminar(nombre)

    # Muestra todos los bocadillos que existen actualmente en la lista
    def listar_bocadillos(self):
        return self._repo.listar()

    # Obtiene el bocadillo correspondiente al nombre
    def obtener_bocadillo(self, nombre):
        return self._repo.obtener_por_nombre(nombre)
    
    def es_promocional(self, nombre):
        return self._repo.es_promocional(nombre)
    
    # Obtiene los usuarios por defecto
    def obtener_usuarios_iniciales(self):
        return self._repo.crear_usuarios_iniciales()
