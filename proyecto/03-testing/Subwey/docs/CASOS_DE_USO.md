# Casos de uso

Las opciones del menu de ingredientes son:

1. Registrar ingrediente
2. Consumir ingrediente
3. Reponer ingrediente
4. Eliminar ingrediente
5. Listar ingredientes
6. Menú de bocadillos
7. Salir

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

## 6. Menú de bocadillos
- Accede al menú de bocadillos.
  
## 7. Salir
- Termina el programa.

## Errores representativos 

- `ValueError`: nombre inexistente, cantidad no valida, stock insuficiente.


---

Las opciones del menu de bocadillos son:

1. Registrar bocadillo
2. Modificar ingredientes del bocadillo
3. Eliminar bocadillo
4. Listar bocadillos
5. Volver a ingredientes

## 1. Registrar bocadillo
- Entrada: nombre, lista de ingredientes, autor, es promo o no (el % de descuento).
- Validaciones: nombre unico, número de ingredientes distintos > 0.

## 2. Modificar ingredientes del bocadillo
- Entrada: nombre, lista de ingredientes.
- Validaciones: nombre existe, número de ingredientes distintos > 0
- Salida: bocadillo actualizado.

## 3. Eliminar ingrediente
- Entrada: nombre.
- Validaciones: nombre existe
- Salida: bocadillo eliminado.

## 4. Listar bocadillos
- Entrada: ninguna.
- Salida: listado (nombre, ingredientes, autor) y promo si aplica.

## 5. Volver a ingredientes
- Vuelve al menú de ingredientes.