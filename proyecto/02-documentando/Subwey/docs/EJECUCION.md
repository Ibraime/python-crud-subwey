# Ejecucion

Este documento debería incluir:

- Requisitos y comando para ejecutar el proyecto.

---

## Requisitos
- Python 3.10+.
- Ejecutar desde la raiz del paquete `02-documentando/` o la carpeta del mismo tipo correspondiente.

## Ejecutar el menu
```bash
python -m Subwey.presentation.menu_ingredientes
```

## Flujo rapido de ejemplo
1. Opcion 6: Menú bocadillos.
2. Opcion 1: Registrar bocadillo.
3. Opcion 4: Listar bocadillos.

## Errores comunes
- "El ingrediente/bocadillo no existe." si se selecciona un nombre inexistente.
- "Stock insuficiente" si se intenta consumir una cantidad de ingrediente superior de la que hay.
- "No hay stock disponible" si la cantidad es 0.
