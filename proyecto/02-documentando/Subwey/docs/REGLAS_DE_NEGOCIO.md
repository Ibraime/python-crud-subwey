# Reglas de negocio

Aquí se incluyen las reglas de negocio implementadas.

---

En el dominio las reglas de negocio que aplican son:

## Reglas de Item
- `codigo`: letra + numero, sin espacios laterales, normalizado a mayusculas.
- `nombre`: no vacio, sin espacios laterales.
- `precio`: float > 0.
- `cantidad`: entero >= 0.

## Reglas de ItemConDescuento
- `porcentaje_descuento`: float entre 0 y 100.
- `precio_final`: aplica descuento sobre el precio base.

## Reglas de MaquinaExpendedora
- No permite agregar items con codigo duplicado.
- Para comprar: debe haber seleccion, stock > 0 y saldo suficiente.
- Si el stock llega a 0 tras comprar, se elimina del repositorio.
- `cancelar` devuelve saldo y reinicia estado.

## Reglas de dinero
- `insertar_dinero` solo acepta cantidades positivas.
- Cambio = saldo - precio final.
