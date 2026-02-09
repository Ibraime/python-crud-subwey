# Más adelante tendrá más funcionalidades, pero ahora mismo sirve simplemente con el nombre
# domain/Usuario.py
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre.strip() or "Anónimo"

    def __repr__(self):
        return f"{self.nombre}"
