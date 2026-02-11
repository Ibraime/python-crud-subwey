# Changelog

En este documento se incluyen los cambios por entrega/version (nuevas funcionalidades, cambios, correcciones y notas de compatibilidad):
- Added
- Changed
- Fixed
- Removed
- Security
-  Compatibility / Breaking changes (Compatibilidad)

---

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

