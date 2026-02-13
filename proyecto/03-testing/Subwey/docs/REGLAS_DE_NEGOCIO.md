# Reglas de negocio

En el dominio las reglas de negocio que aplican son:

## Reglas de Ingrediente
- `nombre`: no vacio, sin espacios laterales.
- `precio`: float > 0.
- `cantidad`: entero >= 0.
  
## Reglas de Bocadillo
- `nombre`: no vacio, sin espacios laterales.
- `ingredientes`: al menos uno.
- `precio`: float > 0 (se calcula automáticamente).
- `autor`: un usuario, anónimo por defecto.

## Reglas de BocadilloPromocion
- `porcentaje_descuento`: float entre 1 y 90.
- `precio`: aplica el descuento sobre el precio calculado.

## Reglas de Usuario
- `nombre`: no vacio, sin espacios laterales.

