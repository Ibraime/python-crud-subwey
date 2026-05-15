# Ejecucion

## Requisitos
- Python 3.10+.
- Ejecutar desde la raiz del paquete por encima de Subwey `02-documentando/`/'`03-testing/`' etc.
- `coverage` para generar reportes de cobertura de tests.

## Clonar repositorio
```bash
git clone git@github.com:Ibraime/python-crud-subwey.git
cd python-crud-subwey/proyecto/04-sqlite
```

## Preparar entorno
```bash
cd Subwey
python -m venv .venv
.venv/Scripts/activate               # GitBash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass #Si da error de UnauthorizedAcess en PowerShell
.venv/Scripts/Activate.ps1           # PowerShell
pip install -r requirements.txt
cd ..
```

## Preparar o reiniciar base de datos
```bash
python -m crear_bd  
```

## Ejecutar la aplicación web
```bash
python -m Subwey.presentation.app
```

Al ejecutarlo nos dará una url, con la que podemos ver la página en el nuestro navegador

```bash
 * Running on http://127.0.0.1:5000
```

## Alternativamente se puede testear con el menú en consola
```bash
python -m Subwey.presentation.menu_ingredientes
```

### Ejemplo salida del menú

```
=== SUBWEY (ingredientes) ===
1. Registrar ingrediente
2. Consumir ingrediente
3. Reponer ingrediente
4. Eliminar ingrediente
5. Listar ingredientes
6. Menú de bocadillos
7. Salir
Elige una opción: 5

Listado de ingredientes:

aguacate   - 7.00 € - 8.00  unidades
pan        - 1.50 € - 10.00 unidades
queso      - 2.00 € - 42.00 unidades
tomate     - 3.00 € - 20.00 unidades
```

## Ejecutar tests y cobertura
```bash
python -m unittest
python -m coverage run -m unittest
python -m coverage report
```

## Flujo rapido de ejemplo
1. Opcion 6: Menú bocadillos.
2. Opcion 1: Registrar bocadillo.
3. Opcion 4: Listar bocadillos.

## Errores comunes
- "El ingrediente/bocadillo no existe." si se selecciona un nombre inexistente.
- "Stock insuficiente" si se intenta consumir una cantidad de ingrediente superior de la que hay.
- "No hay stock disponible" si la cantidad es 0.
