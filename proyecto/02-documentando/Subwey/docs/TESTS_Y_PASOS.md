# Tests y pasos

Aquí se incluye como ejecutar los tests de la aplicación y que valida cada uno.
(TODO cuando hayan tests)
---

## Ejecucion de pruebas

Ejemplos:
```bash
python -m expendedora.test_item
python -m expendedora.test_item_descuento
python -m expendedora.test_paso2_repo_memoria
python -m expendedora.test_maquina_parte1
python -m expendedora.test_maquina_parte2
python -m expendedora.test_repo_no_sobrescribir
python -m expendedora.test_eliminar_repo
python -m expendedora.test_servicio
python -m expendedora.test_contrato
python -m expendedora.test_datos_iniciales
```

## Que valida cada test
- `test_item.py`: validaciones de Item.
- `test_item_descuento.py`: validaciones de ItemConDescuento.
- `test_paso2_repo_memoria.py`: alta y listado en repositorio memoria.
- `test_maquina_parte1.py`: agregar items y listado (nota: en esta fase la maquina requiere repositorio).
- `test_maquina_parte2.py`: seleccion, saldo y compra.
- `test_repo_no_sobrescribir.py`: evita duplicados.
- `test_eliminar_repo.py`: eliminar tras comprar.
- `test_servicio.py`: flujo basico via servicio.
- `test_contrato.py`: contrato base de repositorio.
- `test_datos_iniciales.py`: datos iniciales (nota: revisar nombre de funcion si cambia).

## Nota de compatibilidad
Algunos tests parecen corresponder a pasos previos (constructores sin repositorio). Ajustar tests o implementacion si se desea coherencia total.
