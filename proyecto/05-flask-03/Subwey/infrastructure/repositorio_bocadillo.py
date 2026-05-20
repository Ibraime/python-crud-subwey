import sqlite3
from Subwey.domain.bocadillo import Bocadillo, BocadilloPromocion
from Subwey.domain.usuario import Usuario
from Subwey.domain.ingrediente import Ingrediente
from Subwey.infrastructure.errores import BocadilloDuplicadoError


class RepositorioBocadillo:

    def __init__(self, db_path="subwey.db"):
        self._db_path = db_path

    def _conectar(self):
        conn = sqlite3.connect(self._db_path)
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    def guardar(self, nombre, ingredientes, descuento=None, autor=None):
        """
        Guarda un nuevo bocadillo.
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
            """, [(nombre, ing.nombre) for ing in ingredientes])

            conn.commit()

        except sqlite3.IntegrityError:
            conn.rollback()
            raise BocadilloDuplicadoError("Ya existe un bocadillo con ese nombre.")

        finally:
            conn.close()

        return self.obtener_por_nombre(nombre)

    def obtener_por_nombre(self, nombre):
        """
        Obtiene un bocadillo por nombre.
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
            conn.close()
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
        conn.close()

        autor = Usuario(autor_nombre)

        if es_promo == 1:
            return BocadilloPromocion(nombre, ingredientes, descuento, autor)

        return Bocadillo(nombre, ingredientes, autor)

    def eliminar(self, nombre):
        """
        Elimina un bocadillo.
        """
        nombre = nombre.strip().lower()
        conn = self._conectar()

        try:
            conn.execute("DELETE FROM bocadillo_ingredientes WHERE bocadillo_nombre = ?", (nombre,))
            conn.execute("DELETE FROM bocadillos WHERE nombre = ?", (nombre,))
            conn.commit()

        finally:
            conn.close()

    def modificar(self, nombre_actual, nuevo_nombre, ingredientes, descuento=None):
        """
        Modifica completamente un bocadillo sin romper foreign keys.
        """

        nombre_actual = nombre_actual.strip().lower()
        nuevo_nombre = nuevo_nombre.strip().lower()

        conn = self._conectar()

        try:
            boc = self.obtener_por_nombre(nombre_actual)
            if not boc:
                raise ValueError("El bocadillo no existe.")

            if nombre_actual != nuevo_nombre:
                if self.obtener_por_nombre(nuevo_nombre):
                    raise BocadilloDuplicadoError("Ya existe un bocadillo con ese nombre.")

            conn.execute("BEGIN")

            # 1. BORRAR RELACIONES (IMPORTANTE PRIMERO)
            conn.execute("""
                DELETE FROM bocadillo_ingredientes
                WHERE bocadillo_nombre = ?
            """, (nombre_actual,))

            # 2. ACTUALIZAR BOCADILLO
            conn.execute("""
                UPDATE bocadillos
                SET nombre = ?,
                    es_promocion = ?,
                    descuento = ?
                WHERE nombre = ?
            """, (
                nuevo_nombre,
                1 if descuento is not None else 0,
                float(descuento) if descuento is not None else 0,
                nombre_actual
            ))

            # 3. REINSERTAR RELACIONES
            conn.executemany("""
                INSERT INTO bocadillo_ingredientes (bocadillo_nombre, ingrediente_nombre)
                VALUES (?, ?)
            """, [(nuevo_nombre, ing.nombre) for ing in ingredientes])

            conn.commit()

        except sqlite3.IntegrityError:
            conn.rollback()
            raise BocadilloDuplicadoError("Error de integridad (FK o duplicado).")

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()

        return self.obtener_por_nombre(nuevo_nombre)

    def listar(self):
        """
        Lista todos los bocadillos.
        """
        conn = self._conectar()

        cursor = conn.execute("SELECT nombre FROM bocadillos ORDER BY nombre")
        nombres = [n[0] for n in cursor.fetchall()]
        conn.close()

        return [self.obtener_por_nombre(n) for n in nombres]

    def es_promocional(self, nombre):
        boc = self.obtener_por_nombre(nombre)
        return boc.es_promocional() if boc else False