# Ejecucion

Este documento debería incluir:

- Requisitos y comando para ejecutar el proyecto.

---

## Requisitos
- Python 3.10+.
- Ejecutar desde la raiz del paquete `expendedora/`.

## Ejecutar el menu
```bash
python -m expendedora.presentation.menu
```

## Flujo rapido de ejemplo
1. Opcion 1: Mostrar productos.
2. Opcion 2: Seleccionar producto (ej. A1).
3. Opcion 3: Insertar dinero (ej. 2.00).
4. Opcion 4: Comprar.

## Errores comunes
- "El codigo no existe." si se selecciona un codigo inexistente.
- "Saldo insuficiente" si no se inserta dinero suficiente.
- "No hay stock disponible" si la cantidad es 0.
