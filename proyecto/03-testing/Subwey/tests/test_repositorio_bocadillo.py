import unittest
from Subwey.infrastructure.repositorio_ingrediente import RepositorioIngrediente
from Subwey.infrastructure.repositorio_bocadillo import RepositorioBocadillo
from Subwey.domain.bocadillo import BocadilloPromocion


class TestRepositorioBocadillo(unittest.TestCase):

    # El repositorio crea estos bocadillos por defecto
    # Bocadillo("vegetal", [tomate, aguacate])
    # Bocadillo("caprese", [tomate, queso])

    def setUp(self):
        self.repo_ingrediente = RepositorioIngrediente()
        self.repo_bocadillo = RepositorioBocadillo(self.repo_ingrediente)

        self.tomate = self.repo_ingrediente.obtener_por_nombre("tomate")
        self.queso = self.repo_ingrediente.obtener_por_nombre("queso")

    # Test obtener_por_nombre

    def test_crea_bocadillos_iniciales(self):
        vegetal = self.repo_bocadillo.obtener_por_nombre("vegetal")
        caprese = self.repo_bocadillo.obtener_por_nombre("caprese")

        self.assertIsNotNone(vegetal)
        self.assertIsNotNone(caprese)

    # Test fallar obtener_por_nombre

    def test_obtener_inexistente_devuelve_none(self):
        self.assertIsNone(
            self.repo_bocadillo.obtener_por_nombre("no_existe")
        )

    # Test guardar

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

    # Test modificar_ingredientes

    def test_modificar_ingredientes(self):
        nuevos_ingredientes = [self.tomate]
        bocadillo = self.repo_bocadillo.modificar_ingredientes(
            "vegetal",
            nuevos_ingredientes
        )

        self.assertEqual(bocadillo.ingredientes, nuevos_ingredientes)

    def test_modificar_bocadillo_inexistente(self):
        with self.assertRaises(ValueError):
            self.repo_bocadillo.modificar_ingredientes(
                "no_existe",
                [self.tomate]
            )

    # Test eliminar

    def test_eliminar_bocadillo(self):
        self.repo_bocadillo.guardar("temporal", [self.tomate])
        self.repo_bocadillo.eliminar("temporal")

        self.assertIsNone(
            self.repo_bocadillo.obtener_por_nombre("temporal")
        )

    def test_eliminar_inexistente(self):
        with self.assertRaises(ValueError):
            self.repo_bocadillo.eliminar("no_existe")

    # Test listar

    def test_listar_devuelve_lista(self):
        lista = self.repo_bocadillo.listar()
        self.assertIsInstance(lista, list)

    def test_listar_vacio(self):
        # clear vacía la lista
        self.repo_bocadillo._bocadillos.clear()
        resultado = self.repo_bocadillo.listar()

        self.assertEqual(resultado, "(No hay bocadillos registrados)")


if __name__ == "__main__":
    unittest.main()
