# Casos de uso

En este documento se describen las diferentes operaciones que se pueden realizar al interactuar con la aplicación.

Para cada caso se especifica: entrada, validaciones, salida y errores.

---

las opciones del menu son:

1. Registrar ingrediente
2. Consumir ingrediente
3. Reponer ingrediente
4. Eliminar ingrediente
5. Listar ingredientes
6. Salir

## 1. Registrar ingrediente
- Entrada: nombre, precio, stock.
- Validaciones: nombre unico, precio > 0, cantidad > -1.

## 2. Consumir ingrediente
- Entrada: nombre, cantidad.
- Validaciones: nombre existe, cantidad > 0
- Salida: stock actualizado.

## 3. Reponer ingrediente
- Entrada: nombre, cantidad.
- Validaciones: nombre existe, cantidad > 0
- Salida: stock actualizado.

## 4. Eliminar ingrediente
- Entrada: nombre.
- Validaciones: nombre existe
- Salida: ingrediente eliminado.

## 5. Listar ingredientes
- Entrada: ninguna.
- Salida: listado (nombre, precio, stock).

## 6. Salir
- Termina el programa.

## Errores representativos 

- `ValueError`: nombre inexistente, cantidad no valida, stock insuficiente.
