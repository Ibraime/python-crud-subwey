import sqlite3
from Subwey.domain.usuario import Usuario
from Subwey.application.servicios_usuario import ServicioUsuario
from Subwey.infrastructure.errores import UsuarioDuplicadoError
class RepositorioUsuario:
    """
    Repositorio de usuarios basado en SQLite.

    Se encarga de la persistencia, consulta y modificación
    de usuarios en la base de datos del sistema Subwey.
    """

    def __init__(self, db_path="subwey.db"):
        """
        Inicializa el repositorio de usuarios.

        :param db_path: Ruta del fichero SQLite donde se almacenan los usuarios.
        """
        self._db_path = db_path

    def _conectar(self):
        """
        Crea una conexión a la base de datos SQLite.

        Activa las claves foráneas para mantener integridad referencial.

        :return: Conexión activa a SQLite.
        """
        conn = sqlite3.connect(self._db_path)
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    def listar(self):
        """
        Obtiene todos los usuarios registrados.

        :return: Lista de objetos Usuario ordenados alfabéticamente.
        """
        with self._conectar() as conn:
            cursor = conn.execute(
                "SELECT nombre FROM usuarios ORDER BY nombre"
            )
            return [Usuario(f[0]) for f in cursor.fetchall()]

    def crear(self, nombre):
        """
        Crea un nuevo usuario en la base de datos.

        :param nombre: Nombre del usuario.
        """
        nombre = nombre.strip().lower()

        try:
            with self._conectar() as conn:
                conn.execute(
                    "INSERT INTO usuarios (nombre) VALUES (?)",
                    (nombre,)
                )
        except sqlite3.IntegrityError:
            raise UsuarioDuplicadoError("Ya existe un usuario con ese nombre.")

    def eliminar(self, nombre):
        """
        Elimina un usuario por su nombre.

        :param nombre: Nombre del usuario a eliminar.
        """
        nombre = nombre.strip().lower()

        with self._conectar() as conn:
            conn.execute(
                "DELETE FROM usuarios WHERE nombre = ?",
                (nombre,)
            )

    def actualizar(self, antiguo_nombre, nuevo_nombre):
        """
        Actualiza el nombre de un usuario existente.

        :param antiguo_nombre: Nombre actual del usuario.
        :param nuevo_nombre: Nuevo nombre a asignar.
        """
        antiguo_nombre = antiguo_nombre.strip().lower()
        nuevo_nombre = nuevo_nombre.strip().lower()

        with self._conectar() as conn:
            conn.execute(
                "UPDATE usuarios SET nombre = ? WHERE nombre = ?",
                (nuevo_nombre, antiguo_nombre)
            )

def crear_servicio_usuario(db_path="subwey.db"):
    """
    Crea una instancia completa del servicio de usuarios.

    Encapsula la creación del repositorio SQLite y del servicio
    de aplicación correspondiente.

    :param db_path: Ruta del fichero SQLite.
    :return: ServicioUsuario listo para usar.
    """
    repo = RepositorioUsuario(db_path=db_path)
    return ServicioUsuario(repo)