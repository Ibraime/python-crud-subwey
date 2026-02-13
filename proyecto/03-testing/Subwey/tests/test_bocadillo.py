import unittest
from Subwey.domain.ingrediente import Ingrediente
from Subwey.domain.bocadillo import Bocadillo, BocadilloPromocion


class TestBocadillo(unittest.TestCase):
    # Creamos 3 ingredientes para los tests de bocadillos
    def setUp(self):
        self.pan = Ingrediente("Pan", 2, 10)
        self.queso = Ingrediente("Queso", 3, 5)
        self.jamon = Ingrediente("Jamón", 4, 8)

    # Validar creación

    def test_creacion_valida(self):
        bocadillo = Bocadillo("Sandwich mixto", [self.pan, self.queso])
        self.assertEqual(bocadillo.nombre, "Sandwich mixto")
        self.assertEqual(len(bocadillo.ingredientes), 2)

    def test_nombre_se_normaliza(self):
        bocadillo = Bocadillo("  Especial  ", [self.pan])
        self.assertEqual(bocadillo.nombre, "Especial")

    # Validar nombre

    def test_nombre_vacio_lanza_error(self):
        with self.assertRaises(ValueError):
            Bocadillo("", [self.pan])

    def test_nombre_solo_espacios_lanza_error(self):
        with self.assertRaises(ValueError):
            Bocadillo("   ", [self.pan])

    # Validar ingredientes

    def test_ingredientes_no_es_lista(self):
        with self.assertRaises(TypeError):
            Bocadillo("Sandwich mixto", self.pan)

    def test_lista_vacia_lanza_error(self):
        with self.assertRaises(ValueError):
            Bocadillo("Sandwich mixto", [])

    def test_elemento_no_es_ingrediente(self):
        with self.assertRaises(TypeError):
            Bocadillo("Sandwich mixto", [self.pan, "queso"])

    def test_no_permite_ingredientes_repetidos(self):
        with self.assertRaises(ValueError):
            Bocadillo("Sandwich mixto", [self.pan, self.pan])

    # Validar precio

    def test_precio_es_suma_de_ingredientes(self):
        bocadillo = Bocadillo("Sandwich mixto", [self.pan, self.queso, self.jamon])
        self.assertEqual(bocadillo.precio, 2 + 3 + 4)


class TestBocadilloPromocion(unittest.TestCase):

    def setUp(self):
        self.pan = Ingrediente("Pan", 2, 10)
        self.queso = Ingrediente("Queso", 3, 5)

    # Validar creación

    def test_creacion_valida_con_descuento(self):
        bocadillo = BocadilloPromocion("Promo", [self.pan, self.queso], 20)
        self.assertEqual(bocadillo.descuento, 20)

    # Validar descuento

    def test_descuento_menor_a_1_lanza_error(self):
        with self.assertRaises(ValueError):
            BocadilloPromocion("Promo", [self.pan], 0)

    def test_descuento_mayor_a_90_lanza_error(self):
        with self.assertRaises(ValueError):
            BocadilloPromocion("Promo", [self.pan], 100)

    def test_setter_descuento_invalido(self):
        bocadillo = BocadilloPromocion("Promo", [self.pan], 10)
        with self.assertRaises(ValueError):
            bocadillo.descuento = 95

    # Validar precio con descuento

    def test_precio_aplica_descuento(self):
        # precio base = 2 + 3 = 5€
        bocadillo = BocadilloPromocion("Promo", [self.pan, self.queso], 20)
        self.assertEqual(bocadillo.precio, 5 * 0.8)


if __name__ == "__main__":
    unittest.main()
