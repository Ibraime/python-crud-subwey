# infrastructure/repositorio_usuario.py
"""
Módulo que define el repositorio de usuarios.

Se encarga de la persistencia en base de datos SQLite
y de la consulta de usuarios registrados en el sistema.
"""

import sqlite3
from Subwey.domain.usuario import Usuario


class RepositorioUsuario:
    """
    Repositorio basado en SQLite para la gestión de usuarios.

    Permite consultar usuarios registrados en la base de datos.
    """

    def __init__(self, db_path="subwey.db"):
        """
        Inicializa el repositorio con la ruta de la base de datos.

        :param db_path: Ruta del fichero SQLite.
        """
        self._db_path = db_path

    def _conectar(self):
        """
        Crea una conexión a la base de datos SQLite.

        :return: Objeto conexión SQLite.
        """
        conn = sqlite3.connect(self._db_path)
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    def listar(self):
        """
        Devuelve una lista de todos los usuarios registrados.

        :return: Lista de objetos Usuario.
        """
        with self._conectar() as conn:
            cursor = conn.execute(
                "SELECT nombre FROM usuarios ORDER BY nombre"
            )
            return [Usuario(fila[0]) for fila in cursor.fetchall()]