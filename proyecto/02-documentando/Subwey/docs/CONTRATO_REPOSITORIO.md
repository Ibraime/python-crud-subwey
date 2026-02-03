# Contrato de repositorio

Describe el contrato de RepositorioIngredientes:
- guardar
- obtener
- listar

Y el metodo eliminar del repositorio en memoria.
---
## Contenido sugerido

### Contrato RepositorioIngredientes (backend)
- `guardar(ingrediente)`: almacena un ingrediente.
- `obtener_por_nombre(nombre)`: devuelve ingrediente o `None`.
- `eliminar_por_nombre(nombre)`: elimina si existe; no debería llegar a ejecutarse si no existe.
- `listar()`: devuelve lista de ingredientes.

### Sustitucion por persistencia real
Cualquier repositorio alternativo debe respetar el contrato anterior para no romper el dominio.
