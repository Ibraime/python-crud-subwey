import unittest
from Subwey.domain.ingrediente import Ingrediente

class TestIngrediente(unittest.TestCase):

    # Validar creación

    def test_creacion_valida(self):
        ingrediente = Ingrediente("Tomate", 10, 5)
        self.assertEqual(ingrediente.nombre, "Tomate")
        self.assertEqual(ingrediente.precio, 10)
        self.assertEqual(ingrediente.stock, 5)

    def test_nombre_se_normaliza(self):
        ingrediente = Ingrediente("  Lechuga  ", 8, 3)
        self.assertEqual(ingrediente.nombre, "Lechuga")
    
    def test_stock_por_defecto(self):
        ingrediente = Ingrediente("Lechuga", 8)
        self.assertEqual(ingrediente.stock, 0)

    # Validar nombre

    def test_nombre_vacio_lanza_error(self):
        with self.assertRaises(ValueError):
            Ingrediente("", 10, 5)

    def test_nombre_solo_espacios_lanza_error(self):
        with self.assertRaises(ValueError):
            Ingrediente("   ", 10, 5)

    # Validar precio

    def test_precio_cero_lanza_error(self):
        with self.assertRaises(ValueError):
            Ingrediente("Tomate", 0, 5)

    def test_precio_negativo_lanza_error(self):
        with self.assertRaises(ValueError):
            Ingrediente("Tomate", -10, 5)

    # Validar stock

    def test_stock_negativo_lanza_error(self):
        with self.assertRaises(ValueError):
            Ingrediente("Tomate", 10, -5)

    # Metodo disponible

    def test_disponible_retorna_disponible(self):
        ingrediente = Ingrediente("Tomate", 10, 5)
        self.assertEqual(ingrediente.disponible(), "Disponible")

    def test_disponible_retorna_agotado(self):
        ingrediente = Ingrediente("Tomate", 10)
        self.assertEqual(ingrediente.disponible(), "Agotado")


if __name__ == "__main__":
    unittest.main()
