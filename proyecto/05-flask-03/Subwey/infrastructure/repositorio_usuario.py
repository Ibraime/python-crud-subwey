import sqlite3
from Subwey.domain.usuario import Usuario
from Subwey.application.servicios_usuario import ServicioUsuario
from Subwey.infrastructure.errores import UsuarioDuplicadoError


class RepositorioUsuario:
    """
    Repositorio de usuarios basado en SQLite.
    """

    def __init__(self, db_path="subwey.db"):
        """
        Inicializa el repositorio de usuarios.

        :param db_path: Ruta del fichero SQLite.
        """
        self._db_path = db_path

    def _conectar(self):
        """
        Crea una conexión a la base de datos SQLite.

        :return: Conexión activa a SQLite.
        """
        conn = sqlite3.connect(self._db_path)
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    def listar(self):
        """
        Obtiene todos los usuarios registrados.

        :return: Lista de objetos Usuario.
        """
        conn = self._conectar()

        try:
            cursor = conn.execute(
                "SELECT nombre FROM usuarios ORDER BY nombre"
            )
            return [Usuario(f[0]) for f in cursor.fetchall()]

        finally:
            conn.close()

    def crear(self, nombre):
        """
        Crea un nuevo usuario en la base de datos.
        """
        nombre = nombre.strip().lower()

        conn = self._conectar()

        try:
            conn.execute(
                "INSERT INTO usuarios (nombre) VALUES (?)",
                (nombre,)
            )
            conn.commit()

        except sqlite3.IntegrityError:
            conn.rollback()
            raise UsuarioDuplicadoError("Ya existe un usuario con ese nombre.")

        finally:
            conn.close()

    def eliminar(self, nombre):
        """
        Elimina un usuario por su nombre.
        """
        nombre = nombre.strip().lower()

        conn = self._conectar()

        try:
            conn.execute(
                "DELETE FROM usuarios WHERE nombre = ?",
                (nombre,)
            )
            conn.commit()

        finally:
            conn.close()

    def actualizar(self, antiguo_nombre, nuevo_nombre):
        """
        Actualiza el nombre de un usuario existente.
        """
        antiguo_nombre = antiguo_nombre.strip().lower()
        nuevo_nombre = nuevo_nombre.strip().lower()

        conn = self._conectar()

        try:
            conn.execute(
                "UPDATE usuarios SET nombre = ? WHERE nombre = ?",
                (nuevo_nombre, antiguo_nombre)
            )
            conn.commit()

        except sqlite3.IntegrityError:
            conn.rollback()
            raise UsuarioDuplicadoError("Ya existe un usuario con ese nombre.")

        finally:
            conn.close()


def crear_servicio_usuario(db_path="subwey.db"):
    """
    Crea una instancia completa del servicio de usuarios.

    :param db_path: Ruta del fichero SQLite.
    :return: ServicioUsuario listo para usar.
    """
    repo = RepositorioUsuario(db_path=db_path)
    return ServicioUsuario(repo)