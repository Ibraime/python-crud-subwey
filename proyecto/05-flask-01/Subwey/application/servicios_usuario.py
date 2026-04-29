# application/servicio_usuario.py
"""
Módulo que define el servicio de usuarios.

Actúa como capa intermedia entre la presentación
y el repositorio de usuarios.
"""

from Subwey.infrastructure.repositorio_usuario import RepositorioUsuario


class ServicioUsuario:
    """
    Servicio de usuarios.

    Encapsula la lógica de acceso a usuarios del sistema.
    """

    def __init__(self, repositorio_usuario=None):
        """
        Inicializa el servicio con su repositorio.

        :param repositorio_usuario: Repositorio de usuarios.
        """
        self._repo_usuario = repositorio_usuario or RepositorioUsuario()

    def listar_usuarios(self):
        """
        Obtiene todos los usuarios registrados.

        :return: Lista de objetos Usuario.
        """
        return self._repo_usuario.listar()