# domain/ingrediente.py
class Ingrediente:

    def __init__(self, nombre_ingrediente, precio, stock=0):
        nombre = nombre_ingrediente.strip()
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = nombre
        self._precio = precio
        self._stock = stock

    def nombre(self):
        return self._nombre

    def stock(self):
        return self._stock

    def precio(self):
        return self._precio

    def consumir(self,cantidad):
        if cantidad > self._stock:
            raise ValueError("No se puede consumir: no hay suficiente stock.")
        else:
            self._stock -= cantidad

    def reponer(self,cantidad):
        if cantidad <= 0:
            raise ValueError("No se puede reponer una cantidad negativa.")
        else:
            self._stock += cantidad

    def disponible(self):
         return "Agotado" if self._stock == 0 else "Disponible"