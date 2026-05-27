# Diseño de la Base de Datos - Subwey

## Mapeo Entidades → Tablas

| Clase de Dominio | Tabla SQL | Propósito |
|---|---|---|
| `Ingrediente` | `ingredientes` | Almacena ingredientes disponibles |
| `Usuario` | `usuarios` | Almacena usuarios/autores |
| `Bocadillo` | `bocadillos` | Almacena bocadillos creados |
| Relación Bocadillo-Ingrediente | `bocadillo_ingredientes` | Relaciona bocadillos con los ingredientes que contiene |

---

## Tabla `ingredientes`

**Propósito:** Guardar ingredientes con su precio y stock.

| Columna | Tipo | Restricciones |
|---|---|---|
| `nombre` | TEXT | PRIMARY KEY |
| `precio` | REAL | NOT NULL |
| `stock` | INTEGER | NOT NULL |

### Ejemplo

```text
nombre   | precio | stock
---------|--------|------
queso    | 1.20   | 15
jamon    | 2.50   | 10
lechuga  | 0.80   | 20
```

---

## Tabla `usuarios`

**Propósito:** Guardar usuarios del sistema.

| Columna | Tipo | Restricciones |
|---|---|---|
| `nombre` | TEXT | PRIMARY KEY |

### Ejemplo

```text
nombre
-------
juan
maria
admin
```

---

## Tabla `bocadillos`

**Propósito:** Guardar información principal de los bocadillos.

| Columna | Tipo | Restricciones |
|---|---|---|
| `nombre` | TEXT | PRIMARY KEY |
| `autor_nombre` | TEXT | FOREIGN KEY → usuarios(nombre) |
| `es_promocion` | INTEGER | DEFAULT 0 |
| `descuento` | REAL | DEFAULT 0 |

### Ejemplo

```text
nombre      | usuario_nombre | es_promocion | descuento
------------|----------------|--------------|-----------
mixto       | juan           | 1            | 20
vegetal     | maria          | 0            | 0
```

---

## Tabla `bocadillo_ingredientes`

**Propósito:** Relacionar bocadillos con ingredientes.

| Columna | Tipo | Restricciones |
|---|---|---|
| `bocadillo_nombre` | TEXT | FOREIGN KEY → bocadillos(nombre) |
| `ingrediente_nombre` | TEXT | FOREIGN KEY → ingredientes(nombre) |

### Ejemplo

```text
bocadillo_nombre | ingrediente_nombre
-----------------|-------------------
mixto            | jamon
mixto            | queso
vegetal          | lechuga
```

---

## Relaciones

```text
usuarios (1)
    ↑
    │
bocadillos (1-N)
    ↑
    │
bocadillo_ingredientes (N-M)
    │
    ↓
ingredientes (1-N)
```

**Tipo de relación:** Uno a cero-o-uno (1:0..1)

- Un `usuario` **puede crear** varios bocadillos.
- Un `bocadillo` **tiene un solo** autor usuario.
- Un `bocadillo` **puede tener** varios ingredientes.
- Un `ingrediente` **puede estar** en varios bocadillos.

---

## SQL de creación

Ver `crear_bd.py` para sentencias SQL completas y ejecutables.