# Contrato de repositorio

Describe el contrato de RepositorioProductos:
- guardar
- obtener
- listar

Y el metodo eliminar del repositorio en memoria.
---
## Contenido sugerido

### Contrato RepositorioProductos (domain)
- `guardar(item)`: almacena un item; error si codigo duplicado.
- `obtener(codigo)`: devuelve item o `None`.
- `listar()`: devuelve lista de items.

### Implementacion en memoria
- `RepositorioProductosMemoria` usa un diccionario por codigo.
- `eliminar(codigo)`: elimina si existe; no falla si no existe.

### Sustitucion por persistencia real
Cualquier repositorio alternativo debe respetar el contrato anterior para no romper el dominio.
