"""
Módulo que define el repositorio de bocadillos.

Se encarga de la persistencia en base de datos SQLite, creación, consulta
y eliminación de bocadillos, incluyendo versiones promocionales.
"""

import sqlite3
from Subwey.domain.bocadillo import Bocadillo, BocadilloPromocion
from Subwey.domain.usuario import Usuario
from Subwey.domain.ingrediente import Ingrediente


class RepositorioBocadillo:
    """
    Repositorio basado en SQLite para la gestión de bocadillos.

    Permite crear, consultar, modificar y eliminar bocadillos,
    incluyendo versiones promocionales.
    """

    def __init__(self, conn=None, db_path="subway.db"):
        """
        Inicializa el repositorio con la base de datos.

        :param db_path: Ruta del fichero SQLite.
        """
        self._conn = conn
        self._db_path = db_path

    def _conectar(self):
        """
        Crea una conexión a la base de datos SQLite.

        :return: Objeto conexión SQLite.
        """
        if self._conn:
            return self._conn

        conn = sqlite3.connect(self._db_path)
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    def guardar(self, nombre, ingredientes, descuento=None, autor=None):
        """
        Guarda un nuevo bocadillo en la base de datos.

        Si se indica descuento, se crea como BocadilloPromocion.

        :param nombre: Nombre del bocadillo.
        :param ingredientes: Lista de ingredientes.
        :param descuento: Porcentaje de descuento (opcional).
        :param autor: Usuario autor (opcional).
        :return: Bocadillo creado.
        :raises ValueError: Si ya existe un bocadillo con ese nombre.
        """
        nombre = nombre.strip().lower()
        autor = autor or Usuario("Anónimo")

        conn = self._conectar()

        try:
            conn.execute("""
                INSERT INTO bocadillos (nombre, autor_nombre, es_promocion, descuento)
                VALUES (?, ?, ?, ?)
            """, (
                nombre,
                autor.nombre,
                1 if descuento is not None else 0,
                float(descuento) if descuento is not None else 0
            ))

            conn.executemany("""
                INSERT INTO bocadillo_ingredientes (bocadillo_nombre, ingrediente_nombre)
                VALUES (?, ?)
            """, [
                (nombre, ing.nombre) for ing in ingredientes
            ])

            if not self._conn:
                conn.commit()

        except sqlite3.IntegrityError:
            raise ValueError("Ya existe un bocadillo con ese nombre.")

        if descuento is not None:
            return BocadilloPromocion(nombre, ingredientes, descuento, autor)

        return Bocadillo(nombre, ingredientes, autor)

    def obtener_por_nombre(self, nombre):
        """
        Obtiene un bocadillo por su nombre.

        :param nombre: Nombre del bocadillo.
        :return: Bocadillo o None si no existe.
        """
        nombre = nombre.strip().lower()
        conn = self._conectar()

        cursor = conn.execute("""
            SELECT nombre, autor_nombre, es_promocion, descuento
            FROM bocadillos
            WHERE nombre = ?
        """, (nombre,))

        fila = cursor.fetchone()

        if not fila:
            return None

        nombre, autor_nombre, es_promo, descuento = fila

        cursor = conn.execute("""
            SELECT i.nombre, i.precio, i.stock
            FROM ingredientes i
            JOIN bocadillo_ingredientes bi
            ON i.nombre = bi.ingrediente_nombre
            WHERE bi.bocadillo_nombre = ?
        """, (nombre,))

        ingredientes = [Ingrediente(*f) for f in cursor.fetchall()]
        autor = Usuario(autor_nombre)

        if es_promo == 1:
            return BocadilloPromocion(nombre, ingredientes, descuento, autor)

        return Bocadillo(nombre, ingredientes, autor)

    def modificar_ingredientes(self, nombre, ingredientes):
        """
        Modifica los ingredientes de un bocadillo existente.

        :param nombre: Nombre del bocadillo.
        :param ingredientes: Nueva lista de ingredientes.
        :return: Bocadillo actualizado.
        :raises ValueError: Si el bocadillo no existe.
        """
        nombre = nombre.strip().lower()
        conn = self._conectar()

        if self.obtener_por_nombre(nombre) is None:
            raise ValueError("Bocadillo no existe.")

        conn.execute("""
            DELETE FROM bocadillo_ingredientes
            WHERE bocadillo_nombre = ?
        """, (nombre,))

        conn.executemany("""
            INSERT INTO bocadillo_ingredientes (bocadillo_nombre, ingrediente_nombre)
            VALUES (?, ?)
        """, [
            (nombre, ing.nombre) for ing in ingredientes
        ])

        if not self._conn:
            conn.commit()

        return self.obtener_por_nombre(nombre)

    def eliminar(self, nombre):
        """
        Elimina un bocadillo del repositorio.

        :param nombre: Nombre del bocadillo.
        :raises ValueError: Si el bocadillo no existe.
        """
        nombre = nombre.strip().lower()
        conn = self._conectar()

        if self.obtener_por_nombre(nombre) is None:
            raise ValueError("El bocadillo no existe.")

        conn.execute("""
            DELETE FROM bocadillo_ingredientes
            WHERE bocadillo_nombre = ?
        """, (nombre,))

        conn.execute("""
            DELETE FROM bocadillos
            WHERE nombre = ?
        """, (nombre,))

        if not self._conn:
            conn.commit()

    def listar(self):
        """
        Devuelve una lista ordenada de bocadillos por nombre.

        :return: Lista de objetos Bocadillo.
        """
        conn = self._conectar()

        cursor = conn.execute("""
            SELECT nombre FROM bocadillos ORDER BY nombre
        """)

        nombres = [fila[0] for fila in cursor.fetchall()]

        resultado = []
        for nombre in nombres:
            boc = self.obtener_por_nombre(nombre)
            if boc is not None:
                resultado.append(boc)

        return resultado

    def es_promocional(self, nombre):
        """
        Indica si un bocadillo es promocional.

        :param nombre: Nombre del bocadillo.
        :return: True si es promocional, False en caso contrario.
        """
        bocadillo = self.obtener_por_nombre(nombre)
        return bocadillo.es_promocional() if bocadillo else False