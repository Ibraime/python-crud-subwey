"""
Módulo que define la entidad Usuario.

Representa a un usuario del sistema identificado por su nombre.
"""

class Usuario:
    """
    Entidad de dominio que representa un usuario.

    Actualmente solo contiene el nombre, pero está preparada
    para ampliaciones futuras.
    """

    def __init__(self, nombre):
        """
        Inicializa un usuario.

        Si el nombre está vacío o contiene solo espacios,
        se asigna "Anónimo" por defecto.

        :param nombre: Nombre del usuario.
        """
        self.nombre = nombre.strip() or "Anónimo"

    def __repr__(self):
        """
        Devuelve la representación en texto del usuario.

        :return: Nombre del usuario.
        """
        return f"{self.nombre}"