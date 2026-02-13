# Changelog

## [0.3.0] - 2026-02-13 (Fase 03: testing)

Versión disponible en la subcarpeta `03-testing`

### Added
- Paquete de pruebas tests/ con tests/test_ingrediente.py y tests/test_repositorio_ingrediente.py entre otros usando unittest y descubrimiento de pruebas.
- Archivo .gitignore para excluir el entorno virtual local (.venv/).
- Guia en docs/TESTS_Y_PASOS.md para ejecutar pruebas con python -m unittest y medir cobertura con coverage.

### Changed
- README.md actualizado con flujo de entorno virtual para preparar y ejecutar el proyecto.
- docs/EJECUCION.md actualizado con pasos de preparacion del entorno y ejecucion.

### Removed
- Tests por pasos en la raiz del paquete (test_*.py) reemplazados por la estructura de pruebas en tests/.

## [0.2.0] - 2026-01-30 (Fase 02: documentación)

Versión disponible en la subcarpeta `02-documentando`

### Added
- Documentación de la fase en `docs/` (descripción y alcance, ejecución, arquitectura por capas, casos de uso, reglas de negocio, modelo de dominio, contrato de repositorio, datos iniciales, tests/pasos y troubleshooting).
- Comentarios en el código centrados en el **por qué** (reglas de negocio, normalización, supuestos y efectos laterales) para aclarar segmentos no obvios.
- `CHANGELOG.md` para registrar la evolución por entregas.

### Changed
- Modificado `README.md` para incluir los aspectos recogidos en los apuntes sobre documentación

## [0.1.0]  - 2026-01-28 (Fase 01: versión inicial)

Versión disponible en la subcarpeta `01-capas`

### Added
- Aplicación base de máquina expendedora por capas:
  - Menú de consola en `presentation/`.
  - Servicios/casos de uso en `application/`.
  - Entidades y reglas de negocio en `domain/` (ingredientes, bocadillos y usuario).
  - Repositorio en memoria y datos iniciales en `infrastructure/`.
- Tests aún en desarrollo

