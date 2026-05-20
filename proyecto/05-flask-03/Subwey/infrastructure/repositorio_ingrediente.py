import sqlite3
from Subwey.domain.ingrediente import Ingrediente
from Subwey.infrastructure.errores import IngredienteDuplicadoError, IngredienteEnUsoError
from Subwey.application.servicios_ingrediente import ServicioIngrediente


class RepositorioIngrediente:
    """
    Repositorio SQLite para la gestión de ingredientes.
    """

    def __init__(self, db_path="subwey.db"):
        """
        Inicializa el repositorio.

        :param db_path: Ruta de la base de datos SQLite.
        """
        self._db_path = db_path

    def _conectar(self):
        """
        Crea una conexión nueva a SQLite.

        :return: conexión SQLite.
        """
        conn = sqlite3.connect(self._db_path)
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    def guardar(self, nombre, precio_float, stock_int):
        """
        Guarda un ingrediente nuevo.
        """

        nombre = nombre.strip().lower()

        if precio_float is None or precio_float <= 0:
            raise ValueError("Precio inválido.")

        if stock_int < 0:
            raise ValueError("Stock inválido.")

        conn = self._conectar()

        try:
            conn.execute(
                "INSERT INTO ingredientes (nombre, precio, stock) VALUES (?, ?, ?)",
                (nombre, precio_float, stock_int),
            )
            conn.commit()

        except sqlite3.IntegrityError:
            conn.rollback()
            raise IngredienteDuplicadoError("Ingrediente ya existe.")

        finally:
            conn.close()

    def obtener_por_nombre(self, nombre):
        """
        Obtiene un ingrediente por nombre.
        """

        nombre = nombre.strip().lower()
        conn = self._conectar()

        try:
            cursor = conn.execute(
                "SELECT nombre, precio, stock FROM ingredientes WHERE nombre = ?",
                (nombre,),
            )
            fila = cursor.fetchone()

            if not fila:
                return None

            return Ingrediente(*fila)

        finally:
            conn.close()

    def reponer(self, nombre, cantidad):
        """
        Aumenta stock de ingrediente.
        """

        if cantidad <= 0:
            raise ValueError("Cantidad inválida.")

        nombre = nombre.strip().lower()
        conn = self._conectar()

        try:
            conn.execute(
                "UPDATE ingredientes SET stock = stock + ? WHERE nombre = ?",
                (cantidad, nombre),
            )
            conn.commit()

        finally:
            conn.close()

    def consumir(self, nombre, cantidad):
        """
        Reduce stock de ingrediente.
        """

        if cantidad <= 0:
            raise ValueError("Cantidad inválida.")

        ingrediente = self.obtener_por_nombre(nombre)

        if not ingrediente:
            raise ValueError("Ingrediente no existe.")

        if cantidad > ingrediente.stock:
            raise ValueError("Stock insuficiente.")

        conn = self._conectar()

        try:
            conn.execute(
                "UPDATE ingredientes SET stock = stock - ? WHERE nombre = ?",
                (cantidad, nombre.strip().lower()),
            )
            conn.commit()

        finally:
            conn.close()

    def eliminar(self, nombre):
        """
        Elimina un ingrediente.
        """

        nombre = nombre.strip().lower()
        conn = self._conectar()

        try:
            cursor = conn.execute(
                "SELECT nombre FROM ingredientes WHERE nombre = ?",
                (nombre,)
            )

            if cursor.fetchone() is None:
                raise ValueError("Ingrediente no existe.")

            conn.execute(
                "DELETE FROM ingredientes WHERE nombre = ?",
                (nombre,)
            )
            conn.commit()

        except sqlite3.IntegrityError:
            conn.rollback()
            raise IngredienteEnUsoError(
                "No se puede eliminar: está en uso."
            )

        finally:
            conn.close()

    def listar(self):
        """
        Lista todos los ingredientes.
        """

        conn = self._conectar()

        try:
            cursor = conn.execute(
                "SELECT nombre, precio, stock FROM ingredientes ORDER BY nombre"
            )
            return cursor.fetchall()

        finally:
            conn.close()
    
def crear_servicio_ingrediente(db_path="subwey.db"):
        """
        Crea una instancia completa del servicio de ingredientes
        utilizando un repositorio SQLite.

        :param db_path: Ruta del fichero SQLite.
        :return: ServicioIngrediente listo para usar.
        """
        repo = RepositorioIngrediente(db_path=db_path)
        return ServicioIngrediente(repo)    