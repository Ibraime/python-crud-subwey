# Contrato de repositorioIngrediente

Describe el contrato de RepositorioIngredientes:
- guardar
- obtener_por_nombre
- reponer
- consumir
- eliminar
- listar

---
## Contenido sugerido

### Contrato RepositorioIngredientes (backend)
- `guardar(nombre, precio, stock)`: almacena un ingrediente.
- `obtener_por_nombre(nombre)`: devuelve ingrediente o `None`.
- `reponer(nombre, cantidad)`: Aumenta la cantidad de stock del ingrediente según la cantidad.
- `consumir(nombre, cantidad)`: Disminuye la cantidad de stock del ingrediente según la cantidad.
- `eliminar(nombre)`: elimina si existe; da error si no.
- `listar()`: devuelve una lista de ingredientes.

---

# Contrato de repositorioBocadillo

Describe el contrato de RepositorioIngredientes:
- guardar
- obtener_por_nombre
- modificar_ingredientes
- eliminar
- listar
- es_promocional
- crear_usuarios_iniciales


---
## Contenido sugerido

### Contrato RepositorioIngredientes (backend)
- `guardar(nombre, ingredientes, descuento, autor)`: almacena un bocadillo (puede ser de promo si se específica).
- `obtener_por_nombre(nombre)`: devuelve bocadillo o `None`.
- `modificar_ingredientes(nombre, ingredientes)`: Cambia los ingredientes que contiene el bocadillo.
- `eliminar(nombre)`: elimina si existe; da error si no.
- `listar()`: devuelve una lista de bocadillos.
- `es_promocional()`: devuelve true si el bocadillo es promocional, false si no.
- `crear_usuarios_iniciales()`: crea unos usuarios por defecto que se usarán como autores de los bocadillos.
  
---

### Sustitucion por persistencia real
Cualquier repositorio alternativo debe respetar el contrato anterior para no romper el dominio.
