# Casos de uso

En este documento se describen las diferentes operaciones que se pueden realizar al interactuar con la aplicación.

Para cada caso se especifica: entrada, validaciones, salida y errores.

---

las opciones del menu son:

1. Mostrar productos
2. Seleccionar producto
3. Insertar dinero
4. Comprar
5. Cancelar
6. Reponer
7. Agregar producto con descuento
8. Salir

## 1. Mostrar productos
- Entrada: ninguna.
- Salida: listado (codigo, nombre, precio final, stock).

## 2. Seleccionar producto
- Entrada: codigo.
- Validaciones: codigo existe.
- Salida: producto seleccionado.

## 3. Insertar dinero
- Entrada: cantidad > 0.
- Salida: saldo actualizado.

## 4. Comprar
- Precondicion: producto seleccionado, stock disponible, saldo suficiente.
- Salida: cambio (saldo - precio).
- Efectos: reduce stock, puede eliminar producto si stock llega a 0.

## 5. Cancelar
- Salida: devuelve saldo y reinicia seleccion.

## 6. Reponer
- Entrada: codigo existente, unidades >= 0.
- Efecto: aumenta stock.

## 7. Agregar producto con descuento
- Entrada: codigo, nombre, precio, cantidad, porcentaje.
- Validaciones: codigo unico, precio > 0, cantidad entero >= 0, 0 <= descuento <= 100.

## 8. Salir
- Termina el programa.

## Errores representativos 

- `ValueError`: codigo inexistente, cantidad no valida, saldo insuficiente.
