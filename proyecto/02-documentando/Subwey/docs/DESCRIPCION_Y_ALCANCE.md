# Descripcion y alcance

Este documento debería incluir:

- Descripcion funcional del proyecto: texto que explica el proyecto desde el punto de vista del usuario (qué hace y cómo se usa), sin entrar en detalles técnicos de implementación
- Objetivos de la fase.
- Alcance: funcionalidades incluidas/excluidas, supuestos y limites.

---

## Descripcion funcional
La aplicacion simula una maquina expendedora con un menu de consola. Permite listar productos, seleccionar un producto, insertar dinero, comprar, cancelar, reponer stock y agregar productos con descuento.

## Objetivos de la fase
- Practicar la separacion por capas (presentation, application, domain, infrastructure).
- Concentrar reglas de negocio en el dominio.
- Mostrar como un repositorio abstracto permite cambiar el almacenamiento.
- Documentar el proyecto aplicando los criterios y recomendaciones vistos en clase.

## Alcance
Incluye:
- Menu de consola (`presentation/menu.py`).
- Servicio de aplicacion (`application/servicios.py`).
- Entidades y reglas del dominio (`domain/item.py`, `domain/maquina.py`).
- Repositorio en memoria y datos iniciales (`infrastructure/`).
- Tests de comprobacion por pasos (`test_*.py`).

No incluye:
- Persistencia real (BD/archivos), interfaz grafica, pagos reales, autenticacion.
- Gestión de monedas/billetes con inventario.
- Concurrencia o multiples usuarios.

## Supuestos y limites
- Precios y saldo en euros (float).
- Codigo de producto con letra + numero (ej. A1).
- Stock entero >= 0.
