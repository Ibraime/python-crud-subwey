# Descripcion y alcance

## Descripcion funcional
La aplicacion simula un restaurante de bocadillos personalizados con un menu de consola. Permite listar ingredientes, añadir nuevos, reponer stock y crear bocadillos con los ingredientes.

## Objetivos de la fase
- Practicar la separacion por capas (presentation, application, domain, infrastructure).
- Concentrar reglas de negocio en el dominio.
- Mostrar como un repositorio abstracto permite cambiar el almacenamiento.
- Documentar el proyecto aplicando los criterios y recomendaciones vistos en clase.

## Alcance
Incluye:
- Menus de consola (`presentation/menu_ingredientes.py`), (`presentation/menu_bocadillo.py`).
- Servicios de aplicacion (`application/servicios_ingrediente.py`), (`application/servicios_bocadillo.py`).
- Entidades y reglas del dominio (`domain/ingrediente.py`, `domain/bocadillo.py`, `domain/usuario.py`).
- Repositorio en memoria y datos iniciales (`infrastructure/`).
- Tests de comprobacion por pasos (`test_*.py`).

No incluye:
- Persistencia real (BD/archivos), interfaz grafica, pagos reales, autenticacion.
- Gestión de dinero ni carro de la compra.
- Login y registro real de usuarios.

## Supuestos y limites
- Precios en euros (float).
- Nombre únicos para ingredientes y bocadillos.
- Stock entero >= 0.
