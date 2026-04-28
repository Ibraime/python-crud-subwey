# Guía de rutas Flask — Subwey (ibraime)

**Dominio**: Subwey gestiona ingredientes, bocadillos y usuarios; un bocadillo agrupa
ingredientes (precio = suma de precios de ingredientes) y puede ser promocional con
descuento porcentual. `BocadilloPromocion` es una clase que hereda de `Bocadillo` y
añade el descuento. Cuando llamas a `bocadillo.precio`, Python usa automáticamente el
cálculo correcto según el tipo de bocadillo (con o sin descuento), aunque en el código
no necesitas distinguirlos explícitamente.

---

## Inventario completo del menú

Operaciones reales extraídas de `presentation/menu_ingredientes.py` y
`presentation/menu_bocadillos.py` (fase `04-sqlite`).

| #  | Sección      | Operación                        | Método del servicio                                          | Categoría   | Excepciones posibles                          |
|----|--------------|----------------------------------|--------------------------------------------------------------|-------------|-----------------------------------------------|
| 1  | Ingrediente  | Registrar ingrediente            | `servicio_ingrediente.registrar_ingrediente(nombre, precio, stock)` | Acción | `IngredienteDuplicadoError`, `ValueError`     |
| 2  | Ingrediente  | Consumir ingrediente             | `servicio_ingrediente.consumir_ingrediente(nombre, cantidad)`  | Acción     | `ValueError` (no existe / stock insuficiente) |
| 3  | Ingrediente  | Reponer ingrediente              | `servicio_ingrediente.reponer_ingrediente(nombre, cantidad)`   | Acción     | `ValueError` (no existe / cantidad <= 0)      |
| 4  | Ingrediente  | Eliminar ingrediente             | `servicio_ingrediente.eliminar_ingrediente(nombre)`           | Acción      | `ValueError`, `IngredienteEnUsoError`         |
| 5  | Ingrediente  | Listar ingredientes              | `servicio_ingrediente.listar_ingredientes()`                  | Lectura     | —                                             |
| 6  | Ingrediente  | Buscar ingrediente por nombre    | `servicio_ingrediente.buscar_por_nombre(nombre)`              | Lectura     | —  (devuelve `None` si no existe)             |
| 7  | Bocadillo    | Registrar bocadillo              | `servicio_bocadillo.crear_bocadillo(nombre, ingredientes, descuento, autor)` | Acción | `BocadilloDuplicadoError`, `ValueError` |
| 8  | Bocadillo    | Modificar ingredientes           | `servicio_bocadillo.modificar_bocadillo(nombre, ingredientes)` | Acción     | `ValueError` (bocadillo no existe)            |
| 9  | Bocadillo    | Eliminar bocadillo               | `servicio_bocadillo.eliminar_bocadillo(nombre)`               | Acción      | `ValueError` (bocadillo no existe)            |
| 10 | Bocadillo    | Listar bocadillos                | `servicio_bocadillo.listar_bocadillos()`                      | Lectura     | —                                             |
| 11 | Bocadillo    | Obtener bocadillo por nombre     | `servicio_bocadillo.obtener_bocadillo(nombre)`                | Lectura     | —  (devuelve `None` si no existe)             |
| 12 | Bocadillo    | Comprobar si es promocional      | `servicio_bocadillo.es_promocional(nombre)`                   | Lectura     | —                                             |
| 13 | Usuario      | Listar usuarios                  | `servicio_usuario.listar_usuarios()`                          | Lectura     | —                                             |

---

## Rutas sugeridas (API completa)

Una fila por operación del menú. Convenio de nombres: sustantivos en plural para
colecciones, singular con `<nombre>` para recursos individuales. Todas las rutas
los parámetros de escritura van en segmentos de URL.

### Ingredientes

| Ruta Flask | Método del servicio | Descripción |
|------------|---------------------|-------------|
| `/ingredientes` | `listar_ingredientes()` | Lista todos los ingredientes |
| `/ingredientes/<nombre>` | `buscar_por_nombre(nombre)` | Detalle; 404 si no existe |
| `/ingredientes/nuevo/<nombre>/<float:precio>/<int:stock>` | `registrar_ingrediente(nombre, precio, stock)` | Registra ingrediente; 409 si ya existe; 400 si datos inválidos |
| `/ingredientes/<nombre>/reponer/<int:cantidad>` | `reponer_ingrediente(nombre, cantidad)` | Repone stock; 404 si no existe; 400 si cantidad inválida |
| `/ingredientes/<nombre>/consumir/<int:cantidad>` | `consumir_ingrediente(nombre, cantidad)` | Consume stock; 404 si no existe; 400 si stock insuficiente |
| `/ingredientes/<nombre>/eliminar` | `eliminar_ingrediente(nombre)` | Elimina ingrediente; 404 si no existe; 409 si está en uso |

### Bocadillos

| Ruta Flask | Método del servicio | Descripción |
|------------|---------------------|-------------|
| `/bocadillos` | `listar_bocadillos()` | Lista todos los bocadillos |
| `/bocadillos/<nombre>` | `obtener_bocadillo(nombre)` | Detalle; 404 si no existe |
| `/bocadillos/nuevo/<nombre>/<ingredientes>/<float:descuento>/<autor>` | `crear_bocadillo(nombre, ingredientes, descuento, autor)` | Registra bocadillo; ingredientes como cadena separada por guiones (p. ej. `jamon-queso`); 409 si ya existe; 400 si datos inválidos |
| `/bocadillos/<nombre>/modificar/<ingredientes>` | `modificar_bocadillo(nombre, ingredientes)` | Actualiza ingredientes; ingredientes como cadena separada por guiones; 404 si no existe |
| `/bocadillos/<nombre>/eliminar` | `eliminar_bocadillo(nombre)` | Elimina bocadillo; 404 si no existe |

### Usuarios

| Ruta Flask | Método del servicio | Descripción |
|------------|---------------------|-------------|
| `/usuarios` | `listar_usuarios()` | Lista todos los usuarios |

### Raíz

| Ruta Flask | Descripción |
|------------|-------------|
| `/` | Bienvenida con enlaces a las secciones principales |

---

### Ejemplo: cómo quedaría `app.py` con dos rutas ya hechas

El siguiente fragmento muestra la estructura mínima de `app.py` con dos rutas implementadas
para que puedas tomar el patrón y aplicarlo al resto:

```python
from flask import Flask
from Subwey.infrastructure.repositorio_ingrediente import RepositorioIngrediente
from Subwey.infrastructure.repositorio_bocadillo import RepositorioBocadillo
from Subwey.application.servicios_ingrediente import ServicioIngrediente
from Subwey.application.servicios_bocadillo import ServicioBocadillo

app = Flask(__name__)

repo_ingredientes = RepositorioIngrediente()
repo_bocadillos = RepositorioBocadillo()
servicio_ingrediente = ServicioIngrediente(repo_ingredientes)
servicio_bocadillo = ServicioBocadillo(repo_bocadillos)


@app.route("/")
def bienvenida():
    return (
        "Bienvenido a Subwey\n"
        "  /ingredientes  → lista todos los ingredientes\n"
        "  /bocadillos    → lista todos los bocadillos\n"
    )


@app.route("/ingredientes")
def listar_ingredientes():
    ingredientes = servicio_ingrediente.listar_ingredientes()
    if not isinstance(ingredientes, list):
        return "No hay ingredientes registrados."
    return "\n".join(str(i) for i in ingredientes)


if __name__ == "__main__":
    app.run(debug=True)
```

**Lo que hace cada parte:**

- El repositorio y el servicio se crean **una sola vez** fuera de las vistas, al arrancar la
  aplicación. Así todas las rutas comparten el mismo estado en memoria.
- Cada función de vista llama al método del servicio correspondiente y devuelve texto plano.
- Para rutas con `ValueError` puedes devolver una tupla `(mensaje, código)`:
  `return "No encontrado", 404` o `return "Ya existe", 409`.

---

## Puntos de atención

### Herencia `Bocadillo` → `BocadilloPromocion`

- `Bocadillo.es_promocional()` devuelve `False`; `BocadilloPromocion.es_promocional()` devuelve `True`.
- Solo `BocadilloPromocion` expone la propiedad `.descuento` (porcentaje entero, 1–90).
- En el route, usa `bocadillo.es_promocional()` para saber si hay descuento y mostrarlo:

```python
linea = f"{boc.nombre} — {boc.precio}€"
if boc.es_promocional():
    linea += f" (descuento {boc.descuento}%)"
return linea
```

### Precio calculado, nunca almacenado

- `Bocadillo.precio` es una `@property` que suma `ingrediente.precio` para cada
  ingrediente en `self._ingredientes`.
- `BocadilloPromocion.precio` aplica `precio_base * (1 - descuento / 100)`.
- El route no calcula nada; usa directamente `bocadillo.precio`.

### `listar_ingredientes()` devuelve tuplas, no objetos

- `ServicioIngrediente.listar_ingredientes()` llama a `repositorio.listar()`, que
  devuelve una lista de tuplas `(nombre, precio, stock)` (o el string
  `"(No hay ingredientes registrados)"` si la tabla está vacía).
- Cuando la lista está vacía el repositorio devuelve un `str`, no una lista.
  El route debe comprobar `isinstance(resultado, list)` antes de serializar.

```python
resultado = servicio_ingrediente.listar_ingredientes()
if not isinstance(resultado, list):
    return "No hay ingredientes registrados."
return "\n".join(f"{n} — {p}€ — stock: {s}" for n, p, s in resultado)
```

> Nota: comprobar `isinstance(resultado, list)` es específico de este servicio, que devuelve un `str` cuando no hay ingredientes en lugar de una lista vacía. En el resto de rutas Flask basta con `if not lista:`.


### Ingredientes referenciados en bocadillos

- `bocadillo.ingredientes` devuelve una lista de objetos `Ingrediente` con atributos
  `.nombre`, `.precio` y `.stock`.
- Al mostrar el detalle de un bocadillo, recorrer la lista e incluir cada ingrediente
  en el texto de respuesta con `str(ingrediente)` o accediendo a sus atributos.

### Excepciones definidas en `infrastructure/errores.py`

| Excepción                  | Cuándo se lanza                                                     | HTTP sugerido |
|----------------------------|---------------------------------------------------------------------|---------------|
| `IngredienteDuplicadoError`| Alta de ingrediente con nombre ya existente                         | 409 Conflict  |
| `BocadilloDuplicadoError`  | Alta de bocadillo con nombre ya existente                           | 409 Conflict  |
| `IngredienteEnUsoError`    | Eliminación de ingrediente presente en algún bocadillo              | 409 Conflict  |
| `UsuarioDuplicadoError`    | (definida, sin uso aún en el menú)                                  | 409 Conflict  |
| `ValueError`               | Validaciones de dominio o repositorio (nombre vacío, stock negativo, etc.) | 404 si no existe / 400 si datos inválidos |
