import sqlite3
from Subwey.domain.ingrediente import Ingrediente


class RepositorioIngrediente:
    """
    Repositorio basado en SQLite para la gestión de ingredientes.

    Permite crear, consultar, actualizar stock y eliminar ingredientes.
    """

    def __init__(self, db_path="subwey.db", conn=None):
        """
        Inicializa el repositorio con la ruta a la base de datos.

        Permite inyectar una conexión en tests.

        :param db_path: Ruta del fichero SQLite.
        :param conn: Conexión SQLite opcional (usada en tests).
        """
        self._db_path = db_path
        self._conn = conn

    def _conectar(self):
        """
        Crea o reutiliza una conexión a la base de datos SQLite.

        :return: Objeto conexión SQLite.
        """
        if self._conn:
            return self._conn

        conn = sqlite3.connect(self._db_path)
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    def guardar(self, nombre, precio_float, stock_int):
        """
        Guarda un nuevo ingrediente en la base de datos.

        :param nombre: Nombre del ingrediente.
        :param precio_float: Precio unitario.
        :param stock_int: Cantidad inicial disponible.
        :raises ValueError: Si el ingrediente ya existe o los datos son inválidos.
        """
        nombre = nombre.strip().lower()

        if precio_float is None or precio_float <= 0:
            raise ValueError("El precio es inválido.")

        if stock_int < 0:
            raise ValueError("El stock no puede ser negativo.")

        try:
            with self._conectar() as conn:
                conn.execute(
                    "INSERT INTO ingredientes (nombre, precio, stock) VALUES (?, ?, ?)",
                    (nombre, precio_float, stock_int),
                )
        except sqlite3.IntegrityError:
            raise ValueError("Ya existe un ingrediente con ese nombre.")

    def obtener_por_nombre(self, nombre):
        """
        Obtiene un ingrediente por su nombre.

        :param nombre: Nombre del ingrediente.
        :return: Objeto Ingrediente o None si no existe.
        """
        nombre = nombre.strip().lower()

        with self._conectar() as conn:
            cursor = conn.execute(
                "SELECT nombre, precio, stock FROM ingredientes WHERE nombre = ?",
                (nombre,),
            )
            fila = cursor.fetchone()

            if fila:
                return Ingrediente(*fila)

            return None

    def reponer(self, nombre, cantidad):
        """
        Aumenta el stock de un ingrediente.

        :param nombre: Nombre del ingrediente.
        :param cantidad: Cantidad a añadir.
        :raises ValueError: Si el ingrediente no existe o la cantidad es inválida.
        """
        if cantidad <= 0:
            raise ValueError("La cantidad a reponer debe ser mayor que cero.")

        ingrediente = self.obtener_por_nombre(nombre)

        if ingrediente is None:
            raise ValueError("No existe un ingrediente con ese nombre.")

        with self._conectar() as conn:
            conn.execute(
                "UPDATE ingredientes SET stock = stock + ? WHERE nombre = ?",
                (cantidad, nombre.strip().lower()),
            )

    def consumir(self, nombre, cantidad):
        """
        Reduce el stock de un ingrediente.

        :param nombre: Nombre del ingrediente.
        :param cantidad: Cantidad a consumir.
        :raises ValueError: Si no existe, cantidad inválida o stock insuficiente.
        """
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        ingrediente = self.obtener_por_nombre(nombre)

        if ingrediente is None:
            raise ValueError("No existe un ingrediente con ese nombre.")

        if cantidad > ingrediente.stock:
            raise ValueError("No se puede consumir: no hay suficiente stock.")

        with self._conectar() as conn:
            conn.execute(
                "UPDATE ingredientes SET stock = stock - ? WHERE nombre = ?",
                (cantidad, nombre.strip().lower()),
            )

    def eliminar(self, nombre):
        """
        Elimina un ingrediente del repositorio.

        :param nombre: Nombre del ingrediente.
        :raises ValueError: Si no existe o está en uso.
        """
        nombre = nombre.strip().lower()
        conn = self._conectar()

        cursor = conn.execute(
            "SELECT nombre FROM ingredientes WHERE nombre = ?",
            (nombre,)
        )

        if cursor.fetchone() is None:
            raise ValueError("El ingrediente no existe.")

        try:
            conn.execute(
                "DELETE FROM ingredientes WHERE nombre = ?",
                (nombre,)
            )

            if not self._conn:
                conn.commit()

        # Captura el error de clave foránea
        except sqlite3.IntegrityError:
            raise ValueError(
                "No se puede eliminar el ingrediente porque está en uso en un bocadillo."
            )

    def listar(self):
        """
        Devuelve una lista ordenada de ingredientes disponibles.

        :return: Lista de tuplas (nombre, precio, stock) o mensaje si está vacío.
        """
        with self._conectar() as conn:
            cursor = conn.execute(
                "SELECT nombre, precio, stock FROM ingredientes ORDER BY nombre"
            )
            filas = cursor.fetchall()

            if not filas:
                return "(No hay ingredientes registrados)"

            return filas