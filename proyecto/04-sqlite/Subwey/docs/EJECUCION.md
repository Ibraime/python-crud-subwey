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

## Ejecutar el menu
```bash
cd python-crud-subwey/proyecto/04-sqlite
python -m Subwey.presentation.menu_ingredientes
```

## Ejecutar tests y cobertura
```bash
python -m unittest
coverage run -m unittest
coverage report
```

## Flujo rapido de ejemplo
1. Opcion 6: Menú bocadillos.
2. Opcion 1: Registrar bocadillo.
3. Opcion 4: Listar bocadillos.

## Errores comunes
- "El ingrediente/bocadillo no existe." si se selecciona un nombre inexistente.
- "Stock insuficiente" si se intenta consumir una cantidad de ingrediente superior de la que hay.
- "No hay stock disponible" si la cantidad es 0.
