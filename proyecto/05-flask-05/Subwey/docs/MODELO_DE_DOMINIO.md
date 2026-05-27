# Modelo de dominio

## Entidades
- `Ingrediente`: ingrediente con nombre, precio y cantidad.
- `Bocadillo`: bocadillo con nombre, ingredientes, autor y precio final calculado.
- `BocadilloPromocion`: bocadillo con porcentaje de descuento.
- `Usuario`: Usuario con nombre.

### Invariantes
- No puede haber ingredientes, bocadillos o usuarios con nombre duplicado en el repositorio.
- Cantidad siempre entero >= 0.
- Precio siempre > 0.

### Colaboraciones
- Usan unos repositorios con operaciones guardar/obtener/listar (y eliminar en memoria).
- Los servicios orquestan casos de uso y delegan en los repositorios.
