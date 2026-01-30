# Modelo de dominio

Auí se incluyen:

- Las entidades principales del proyecto
- Invariates: condiciones que siempre deben cumplirse para que una entidad del dominio sea válida, antes y después de cualquier operación
- Colaboraciones: son las relaciones e interacciones que una entidad tiene con otras partes del dominio o con contratos (interfaces) para cumplir su responsabilidad

---

## Entidades
- `Item`: producto con codigo, nombre, precio y cantidad.
- `ItemConDescuento`: item con porcentaje de descuento y precio final calculado.
- `MaquinaExpendedora`: coordina seleccion, saldo y compra.

### Invariantes
- No puede haber items con codigo duplicado en el repositorio.
- Cantidad siempre entero >= 0.
- Precio siempre > 0.

### Colaboraciones
- MaquinaExpendedora usa un repositorio con operaciones guardar/obtener/listar (y eliminar en memoria).
- ServicioExpendedora orquesta casos de uso y delega en MaquinaExpendedora.
