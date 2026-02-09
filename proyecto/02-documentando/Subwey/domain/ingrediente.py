# domain/ingrediente.py
class Ingrediente:

    def __init__(self, nombre, precio, stock=0):
        self._nombre = nombre
        self._precio = precio
        self._stock = stock

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        # validar no vacio y sin espacios laterales
        texto = (valor or "").strip()
        if not texto:
            raise ValueError("El nombre no puede estar vacio.")
        self._nombre = texto

    @property
    def stock(self):
        return self._stock
    
    
    @stock.setter
    def stock(self, valor):
        # validar stock > 0
        if valor <= 0:
            raise ValueError("El stock no puede ser menor que cero.")
        self._precio = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        # validar precio > 0
        if valor <= 0:
            raise ValueError("El precio no puede ser menor que cero.")

    def disponible(self):
         return "Agotado" if self._stock == 0 else "Disponible"