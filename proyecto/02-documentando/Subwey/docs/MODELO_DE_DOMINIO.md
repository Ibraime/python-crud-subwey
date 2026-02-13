# Modelo de dominio

Aquí se incluyen:

- Las entidades principales del proyecto
- Invariates: condiciones que siempre deben cumplirse para que una entidad del dominio sea válida, antes y después de cualquier operación
- Colaboraciones: son las relaciones e interacciones que una entidad tiene con otras partes del dominio o con contratos (interfaces) para cumplir su responsabilidad

---

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
