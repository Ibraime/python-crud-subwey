# Changelog

## [0.5.4] - 2026-05-25 (Fase 09: Formularios y mejoras UX)

### Added
- Formularios POST para crear usuarios, bocadillos e ingredientes.
- Plantilla genérica de confirmación de eliminación.
- Mensajes de error en formularios sin salir de la vista.

### Changed
- Migración de rutas con parámetros en URL a formularios POST.
- Bocadillos: creación y edición ahora permite cambiar el usuario autor.
- Usuarios: creación y modificación mediante formularios.
- Ingredientes: creación con formulario.
- Repositorios SQLite mejorados para evitar errores de integridad.

### Fixed
- Errores de Flask (`UnboundLocalError`, `TypeError`).
- `FOREIGN KEY constraint failed` gestionado correctamente.
- Problemas de selección de usuario e ingredientes en edición.
- Eliminación sin control convertida a flujo seguro con confirmación.

## [0.5.3] - 2026-05-20 (Fase 08: Plantillas Jinja2 + arreglos Flask y SQLite)

### Added
- Plantillas Jinja2 para crear usuarios e ingredientes, y editar bocadillos en un mismo formulario. Sin tener html en los routes ni consulta sql.
- Persistencia de datos en formularios (ingredientes seleccionados, modo edición).
- Mejora de navegación entre vistas (crear, editar, detalle).

### Changed
- Refactor de `RepositorioBocadillo`, `RepositorioUsuario` y `RepositorioIngrediente` para un manejo más estable de SQLite.
- Se añadió método modificar a `RepositorioBocadillo` para modificarlo completo, no solo ingredientes
- Unificación del uso de conexiones para evitar errores de bloqueo (`database is locked`).
- Ajuste del flujo de modificación de bocadillos (cambio de nombre + relaciones) dio muchos problemas por no tener un id aparte que no se modifique.

### Fixed
- Error `database is locked` al modificar datos.
- Error al cambiar nombre de bocadillo (conflictos de integridad).
- Error `UnboundLocalError` en el formulario de creación.
- Error `FOREIGN KEY constraint failed` al actualizar relaciones.

## [0.5.2] - 2026-05-15 (Fase 06 y 07: Observabilidad y manejadores globales)

### Added
- `presentation/app.py`: manejadores globales `@app.errorhandler(404)` y `@app.errorhandler(500)`.
- `presentation/app.py`: route `/ayuda` que lista todas las rutas registradas mediante `app.url_map`.
- `presentation/app.py`: logging de peticiones con `@app.before_request`; se genera `subwey.log` al arrancar.
- `presentation/app.py`: tabla de equivalencia `menu_ingredientes.py` y `menu_bocadillos.py` ↔ `app.py` como comentario inicial.
- `.gitignore`: entrada `*.log` para no versionar ficheros de log y `*.db` para no versionarla cada vez que haya un cambio probando.

## [0.5.1] - 2026-05-13 (Fase 05 A1: Flask capa de presentación)

### Added
- `presentation/app.py`: interfaz web con flask, que funciona como el menú de consola, para modificar y crear ingredientes bocadillos y usuarios
- `presentation/routes/`: para que sea más manejable separé la ruta para cada entidad en 3 archivos distintos.

### Changed
- `infrastructure/repositorio_x`: Se añadió una función a los repositorios usuarios e ingredientes para que sean más compatibles con flask, no afecta al resto del código.
- `README.md`: nuevas instrucciones de cómo ejecutar la página web y explicación sobre nuevos archivos
- `docs/EJECUCION.md`: pasos de cómo ejecutar la página web
  

## [0.4.1] - 2026-04-22 (Fase 04: SQLite + tests de repositorio)

### Added
- `errores.py`: excepciones para los errores de sqlite, y que no tenga todo value error.

### Changed
- `tests/*`: tests actualizados para simular que usa la base de datos.
- `README.md`: nuevas instrucciones de cómo ejecutar el script de inicialización
- `docs/EJECUCION.md`: pasos de como crear o reiniciar la base de datos.
  
## [0.4.0] - 2026-04-15 (Fase 04: SQLite + tests de repositorio)

### Added
- `crear_bd.py`: script para crear el esquema e insertar datos iniciales.
- `subwey.db`: base de datos SQLite con los datos iniciales.
- `repositorio_usuario`: repositorio básico para manejar la tabla de usuario.
- `servicio_usuario`: servicio para conectar el repositorio de usuarios con el menú de bocadillos.


### Changed
- `tests/*`: tests actualizados para simular que usa la base de datos.
- `infrastructure/*`: repositorios actualizados para usar la base de datos sqlite.
- `docs/EJECUCION.md`: pasos de como crear o reiniciar la base de datos.
  
## [0.3.1] - 2026-04-10 (Fase 03: Testing)

### Changed
- Corregida la documentación, sobre env y coverage, y añadir docstrings
- Corrección de algunos errores del código

## [0.3.0] - 2026-02-13 (Fase 03: Testing)

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

## [0.2.0] - 2026-01-30 (Fase 02: Documentación)

Versión disponible en la subcarpeta `02-documentando`

### Added
- Documentación de la fase en `docs/` (descripción y alcance, ejecución, arquitectura por capas, casos de uso, reglas de negocio, modelo de dominio, contrato de repositorio, datos iniciales, tests/pasos y troubleshooting).
- Comentarios en el código centrados en el **por qué** (reglas de negocio, normalización, supuestos y efectos laterales) para aclarar segmentos no obvios.
- `CHANGELOG.md` para registrar la evolución por entregas.

### Changed
- Modificado `README.md` para incluir los aspectos recogidos en los apuntes sobre documentación

## [0.1.0]  - 2026-01-28 (Fase 01: Versión inicial)

Versión disponible en la subcarpeta `01-capas`

### Added
- Aplicación base de subwey por capas:
  - Menú de consola en `presentation/`.
  - Servicios/casos de uso en `application/`.
  - Entidades y reglas de negocio en `domain/` (ingredientes, bocadillos y usuario).
  - Repositorio en memoria y datos iniciales en `infrastructure/`.
- Tests aún en desarrollo

