"""
Módulo de excepciones de dominio.
"""


class IngredienteDuplicadoError(Exception):
    """
    Se lanza cuando se intenta crear un ingrediente
    con un nombre que ya existe.
    """
    pass


class BocadilloDuplicadoError(Exception):
    """
    Se lanza cuando se intenta crear un bocadillo
    con un nombre que ya existe.
    """
    pass

class BocadilloSinIngredientesError(Exception):
    """
    Se lanza cuando se intenta crear o modificar un bocadillo
    sin ningún ingrediente.
    """
    pass


class UsuarioEnUsoError(Exception):
    """
    Se lanza cuando se intenta eliminar un usuario
    que está siendo usado en un bocadillo.
    """
    pass

class UsuarioDuplicadoError(Exception):
    """
    Se lanza cuando se intenta crear un usuario
    con un nombre que ya existe.
    """
    pass

class IngredienteEnUsoError(Exception):
    """
    Se lanza cuando se intenta eliminar un ingrediente
    que está siendo usado en un bocadillo.
    """
    pass