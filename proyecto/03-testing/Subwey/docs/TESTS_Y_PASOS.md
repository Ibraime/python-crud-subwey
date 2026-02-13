# Tests y pasos

## Ejecucion de pruebas
Desde la carpeta padre que contiene el paquete `Subwey/`:

```bash
python -m unittest
```

Tambien puedes ejecutar solo para un módulo concreto:

Ejemplos:
```bash
python -m Subwey.tests.test_ingrediente
python -m Subwey.tests.test_bocadillo
python -m Subwey.tests.test_repositorio_ingrediente
python -m Subwey.tests.test_repositorio_bocadillo
```

## Que valida cada test
- `test_ingrediente.py`: validaciones de Ingrediente.
- `test_bocadillo.py`: validaciones de Bocadillo y BocadilloPromocional.
- `test_repositorio_ingrediente.py`: guardar, reponer, consumir, obtener, eliminar y listado en repositorio ingrediente.
- `test_repositorio_bocadillo.py`: guardar, modificar ingredientes, obtener, eliminar y listado en repositorio bocadillo.

## Nota de compatibilidad
Algunos tests tienen dependencia con otros archivos al parte del que testea principalmente, romper una función puede hacer que fallen varios.

## Pruebas de coverage
Desde la carpeta padre que contiene el paquete `Subwey/`:

```bash
coverage run -m unittest
```

Generar reporte en consola:

```bash
coverage report
```

Generar reporte HTML:

```bash
coverage html
```

El reporte se consulta en `htmlcov/index.html`.
