# REVISIONES PROYECTO

## REVISIÓN FASE 03 - 2026-02-20

Muy bien. Solo algunos detalles en la documentación de los tests de:

### Aspectos a mejorar

- Faltan pasos de preparación del entorno para testing/cobertura en la documentación en el archivo `TESTS_Y_PASOS.md` no aparecen pasos de venv, activación ni instalación (pip install coverage).
- En el archivo de documentación  `docs/DESCRIPCION_Y_ALCANCE.md` Dice “Tests por pasos (`test_*.py`)”, pero en esta fase los tests están en `Subwey/tests/`.
- En el archivo de documentación `docs/EJECUCION.md` no indicas como preparar el entorno ni como ejecutar tests y cobertura.

## REVISIÓN FASE 02 - 2026-02-20

La revisión se hace en la subcarpeta `03-testing`. Bien en general. Algunos:

### Aspectos a mejorar

- `docs/CASOS_DE_USO.md` línea 66 - en el menú de bocadillos pone “## 3. Eliminar ingrediente”; debería ser eliminar bocadillo.
- `docs/MODELO_DE_DOMINIO.md` línea 5 se habla de `Bocadillo` con `autor`, pero en dominio no existe ese atributo.
- `docs/REGLAS_DE_NEGOCIO.md` línea 14 regla de `autor` en bocadillo no aparece en la clase del dominio.
- `docs/CONTRATO_REPOSITORIO.md` varios errores. Revisa
- `docs/REGLAS_DE_NEGOCIO` no están todas ni coinciden algunas con el código real:
  - Bocadillo documenta autor, pero esa regla no está en la clase del dominio.
  - No se documenta claramente la restricción de ingredientes no repetidos que se aplica en la clase `Bocadillo`.- - Falta detallar reglas están en repositorio (por ejemplo, validaciones de existencia y consumo/reposición de stock en repositorio_ingrediente.py).
  - Usa cantidad (cantidad: entero >= 0) para Ingrediente, pero en código la propiedad/atributo es `stock`.
- En `README.md` principal faltan enlaces al índice y detalles de la documentación del proyecto y al `CHANGELOG.md`
- Faltan practicamente todos los **docstrings** en módulos/clases/métodos públicos
- Nombres elegidos en código. Bien en general. Algunas recomendaciones que **no se cumplen** (o se cumplen de forma débil) en el código son:
  - **Uso de nombres genéricos o opacos**:
    - `domain/ingrediente.py:14` y `domain/ingrediente.py:16` (`valor`, `texto`)  
    - `domain/bocadillo.py:16` y `proyecto/03-testing/Subwey/domain/bocadillo.py:17` (`valor`, `texto`)
  - **No se incluye unidades y forma**  
   Ejemplos:
    - `domain/ingrediente.py:4` (`precio`, `stock` sin unidad/tipo en nombre)  
    - `domain/bocadillo.py:54` (`descuento` sin indicar `%`)  
    - `domain/bocadillo.py:74` (`precio_base` sin unidad explícita)
  - **Booleans como preguntas.**  
    - `presentation/menu_bocadillos.py:92` (`promo` debería ser algo tipo `es_promocional`)

## REVISIÓN FASE 01 - 2026-02-20

Arreglados todos los aspectos de la revisión anterior. Solo un par de:

### Aspectos a mejorar
- En la capa de presentación hay dependencia directa del dominio y además aplica/consulta reglas de negocio de dominio desde presentación (tipos promocionales, autor, etc.)

En el archivo `presentation/menu_bocadillos.py` debería ser solo interfaz de usuario (leer `input`, mostrar `print`) y **no** conocer clases de dominio ni reglas de negocio.

- No debería haber imports de dominio (líneas 6 y 7):
- Deberías Mover a `application` la lógica de:
   - usuarios predeterminados (`USUARIOS_PREDETERMINADOS`)
   - resolución de autor por nombre
   - decidir promo/no promo y tipo de bocadillo
   - formateo “es promo” (hoy usa `isinstance(BocadilloPromocion)`)
- Desde presentación no se debería modificar atributos del dominio (`boc.autor = autor` línea 99).
- Desde presentación no se debería comprobar si un objeto es de una clase del dominio `isinstance(bocadillo, BocadilloPromocion)` línea 145. 

**La idea es que desde la capa de presentación:
   - solo recoge datos crudos: `nombre`, `ids/nombres ingredientes`, `autor_nombre`, `descuento_opcional`
   - llama a métodos de `ServicioBocadillo`
   - muestra resultados ya **listos para mostrar**

## REVISIÓN FASE 01 - 2026-02-03

### RECOMENDACIONES / COMENTARIOS

- Proyecto demasiado básico en el que no se puede verificar algunos de los aspectos vistos en clase.

### ASPECTOS A CAMBIAR / AÑADIR

- [x] Solo has creado una entidad para la aplicación, `Ingrediente`. No lo pone explícitamente en la checklist, pero en clase he indicado que el proyecto en esta fase debería tener, al menos 3 entidades creadas y al menos en una se debe aplicar herencia.
- [x]También debes usar otros aspectos de la POO que hemos visto en clase, por ejemplo usar decoradores para getters y setters.
- [x] La capa de aplicación debería usarse solo para orquestar y como mucho para validar las entradas de los usuarios. En tu caso en la capa de aplicación estás creando objetos y almacenandolos en el repositorio cuando simplemente deberías pasar los datos de entrada al dominio para que este se encargue de aplicar lógica de negocio.
- [x] Debería haber una clase para gestionar todos los ingredientes. Esta debería incluir el repositorio en memoria para guardar todos los ingredientes. De dicha clase debería existir un contrato para las operaciones de almacenar en el repositorio la lista de ingredientes.
