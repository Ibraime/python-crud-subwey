# Reglas de negocio

En el dominio las reglas de negocio que aplican son:

## Reglas de Ingrediente
- `nombre`: no vacio, sin espacios laterales.
- `precio`: float > 0.
- `stock`: entero >= 0.
- `reponer(nombre,cantidad)`: cantidad > 0
- `consumir(nombre,cantidad)`: cantidad <= stock
  
## Reglas de Bocadillo
- `nombre`: no vacio, sin espacios laterales.
- `ingredientes`: al menos uno, tienen que ser únicos, no repetidos.
- `precio`: float > 0 (se calcula automáticamente).
- `autor`: un usuario, Anónimo por defecto.

## Reglas de BocadilloPromocion
- `porcentaje_descuento`: float entre 1 y 90.
- `precio`: aplica el descuento sobre el precio calculado.

## Reglas de Usuario
- `nombre`: no vacio, sin espacios laterales.

