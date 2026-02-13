import unittest
from Subwey.infrastructure.repositorio_ingrediente import RepositorioIngrediente


class TestRepositorioIngrediente(unittest.TestCase):

    # El repositorio crea este ingrediente por defecto "tomate":Ingrediente("tomate", 3, 20)

    def setUp(self):
        self.repo = RepositorioIngrediente()

    # Test obtener_por_nombre

    def test_crea_ingredientes_iniciales(self):
        tomate = self.repo.obtener_por_nombre("tomate")
        self.assertIsNotNone(tomate)
        self.assertEqual(tomate.stock, 20)

    # Test fallar obtener_por_nombre

    def test_obtener_inexistente_devuelve_none(self):
        self.assertIsNone(self.repo.obtener_por_nombre("no_existe"))

    # Test guardar

    def test_guardar_nuevo_ingrediente(self):
        self.repo.guardar("cebolla", 5, 10)
        ingrediente = self.repo.obtener_por_nombre("cebolla")
        self.assertIsNotNone(ingrediente)
        self.assertEqual(ingrediente.precio, 5)

    def test_no_permite_nombre_repetido(self):
        with self.assertRaises(ValueError):
            self.repo.guardar("tomate", 4, 10)

    def test_precio_invalido_lanza_error(self):
        with self.assertRaises(ValueError):
            self.repo.guardar("lechuga", 0, 10)

    def test_stock_negativo_lanza_error(self):
        with self.assertRaises(ValueError):
            self.repo.guardar("lechuga", 5, -1)

    # Test reponer

    def test_reponer_aumenta_stock(self):
        tomate = self.repo.obtener_por_nombre("tomate")
        stock_inicial = tomate.stock

        self.repo.reponer("tomate", 5)

        self.assertEqual(tomate.stock, stock_inicial + 5)

    def test_reponer_ingrediente_inexistente(self):
        with self.assertRaises(ValueError):
            self.repo.reponer("no_existe", 5)

    def test_reponer_cantidad_invalida(self):
        with self.assertRaises(ValueError):
            self.repo.reponer("tomate", 0)

    # Test consumir

    def test_consumir_reduce_stock(self):
        tomate = self.repo.obtener_por_nombre("tomate")
        stock_inicial = tomate.stock

        self.repo.consumir("tomate", 5)

        self.assertEqual(tomate.stock, stock_inicial - 5)

    def test_consumir_mas_de_lo_disponible(self):
        tomate = self.repo.obtener_por_nombre("tomate")

        with self.assertRaises(ValueError):
            self.repo.consumir("tomate", tomate.stock + 1)

    def test_consumir_ingrediente_inexistente(self):
        with self.assertRaises(ValueError):
            self.repo.consumir("no_existe", 5)

    # Test eliminar

    def test_eliminar_ingrediente(self):
        self.repo.guardar("pepino", 3, 5)
        self.repo.eliminar("pepino")
        self.assertIsNone(self.repo.obtener_por_nombre("pepino"))

    def test_eliminar_inexistente(self):
        with self.assertRaises(ValueError):
            self.repo.eliminar("no_existe")

    # Test listar

    def test_listar_devuelve_lista_ordenada(self):
        lista = self.repo.listar()
        self.assertIsInstance(lista, list)
        for item in lista:
            self.assertEqual(len(item), 3)

    def test_listar_sin_elementos(self):
        self.repo._ingredientes.clear()
        resultado = self.repo.listar()
        self.assertEqual(resultado, "(No hay ingredientes registrados)")


if __name__ == "__main__":
    unittest.main()
