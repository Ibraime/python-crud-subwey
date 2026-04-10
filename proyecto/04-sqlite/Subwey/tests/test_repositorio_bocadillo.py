import unittest
import sqlite3
from pathlib import Path

from Subwey.infrastructure.repositorio_bocadillo import RepositorioBocadillo
from Subwey.infrastructure.repositorio_ingrediente import RepositorioIngrediente
from Subwey.domain.bocadillo import BocadilloPromocion


class TestRepositorioBocadillo(unittest.TestCase):

    # El repositorio crea estos bocadillos por defecto
    # Bocadillo("vegetal", [tomate, aguacate])
    # Bocadillo("caprese", [tomate, queso])

    BD_TEST = Path("test_subway.db")

    def setUp(self):
        # eliminar BD anterior si existe
        if self.BD_TEST.exists():
            try:
                self.BD_TEST.unlink()
            except PermissionError:
                pass

        # crear esquema limpio SOLO PARA TEST
        conn = sqlite3.connect(self.BD_TEST)
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")

        # TABLAS
        cursor.execute("""
            CREATE TABLE ingredientes (
                nombre TEXT PRIMARY KEY,
                precio REAL NOT NULL,
                stock INTEGER NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE usuarios (
                nombre TEXT PRIMARY KEY
            )
        """)

        cursor.execute("""
            CREATE TABLE bocadillos (
                nombre TEXT PRIMARY KEY,
                autor_nombre TEXT,
                es_promocion INTEGER,
                descuento REAL
            )
        """)

        cursor.execute("""
            CREATE TABLE bocadillo_ingredientes (
                bocadillo_nombre TEXT,
                ingrediente_nombre TEXT,
                PRIMARY KEY (bocadillo_nombre, ingrediente_nombre)
            )
        """)

        # DATOS INICIALES
        cursor.executemany("""
            INSERT INTO ingredientes VALUES (?, ?, ?)
        """, [
            ("tomate", 3, 20),
            ("queso", 2, 10),
            ("aguacate", 4, 5)
        ])

        cursor.execute("INSERT INTO usuarios VALUES ('Anónimo')")

        cursor.executemany("""
            INSERT INTO bocadillos VALUES (?, ?, ?, ?)
        """, [
            ("vegetal", "Anónimo", 0, 0),
            ("caprese", "Anónimo", 0, 0)
        ])

        cursor.executemany("""
            INSERT INTO bocadillo_ingredientes VALUES (?, ?)
        """, [
            ("vegetal", "tomate"),
            ("vegetal", "aguacate"),
            ("caprese", "tomate"),
            ("caprese", "queso")
        ])

        conn.commit()
        conn.close()

        # repositorios apuntando a BD de test
        self.repo_ingrediente = RepositorioIngrediente(str(self.BD_TEST))
        self.repo_bocadillo = RepositorioBocadillo(str(self.BD_TEST))

        self.tomate = self.repo_ingrediente.obtener_por_nombre("tomate")
        self.queso = self.repo_ingrediente.obtener_por_nombre("queso")

    def tearDown(self):
        try:
            if self.BD_TEST.exists():
                self.BD_TEST.unlink()
        except PermissionError:
            pass

    # TESTS

    def test_crea_bocadillos_iniciales(self):
        vegetal = self.repo_bocadillo.obtener_por_nombre("vegetal")
        caprese = self.repo_bocadillo.obtener_por_nombre("caprese")

        self.assertIsNotNone(vegetal)
        self.assertIsNotNone(caprese)

    def test_obtener_inexistente_devuelve_none(self):
        self.assertIsNone(
            self.repo_bocadillo.obtener_por_nombre("no_existe")
        )

    def test_guardar_bocadillo_normal(self):
        bocadillo = self.repo_bocadillo.guardar(
            "tomate y queso",
            [self.tomate, self.queso]
        )

        self.assertIsNotNone(
            self.repo_bocadillo.obtener_por_nombre("tomate y queso")
        )
        self.assertEqual(bocadillo.nombre, "tomate y queso")

    def test_guardar_bocadillo_repetido(self):
        with self.assertRaises(ValueError):
            self.repo_bocadillo.guardar("vegetal", [self.tomate])

    def test_guardar_bocadillo_promocion(self):
        bocadillo = self.repo_bocadillo.guardar(
            "promo",
            [self.tomate, self.queso],
            descuento=20
        )

        self.assertIsInstance(bocadillo, BocadilloPromocion)
        self.assertEqual(bocadillo.descuento, 20)

    def test_modificar_ingredientes(self):
        nuevos = [self.tomate]

        bocadillo = self.repo_bocadillo.modificar_ingredientes(
            "vegetal",
            nuevos
        )

        self.assertEqual(len(bocadillo.ingredientes), 1)

    def test_eliminar_bocadillo(self):
        self.repo_bocadillo.eliminar("vegetal")
        self.assertIsNone(
            self.repo_bocadillo.obtener_por_nombre("vegetal")
        )

    def test_listar_devuelve_lista(self):
        lista = self.repo_bocadillo.listar()
        self.assertIsInstance(lista, list)


if __name__ == "__main__":
    unittest.main()