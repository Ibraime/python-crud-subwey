# Arquitectura por capas

Este documento debería incluir:

- Descripcion de la estructura que se la ha dado al proyecto.
- Dependencias permitidas y responsabilidades.
---

El proyecto ha sido estructurado usando el diseño por capas.

## Capas y responsabilidades
- frontend: entrada/salida por consola. No contiene reglas de negocio.
- servicios: orquesta casos de uso sobre el dominio, validaciones.
- entidades: Las distintas entidades.
- backend: repositorios concretos y datos iniciales.

## Dependencias permitidas
- frontend -> servicios -> backend
- backend -> entidades

No se debe depender de frontend desde entidades ni servicios.

## Mapa de archivos
- `frontend/menu_ingredientes.py`: UI de consola.
- `servicios/servicios_ingrediente.py`: casos de uso.
- `entidades/ingrediente.py`, `backend/repositorio_ingredientes.py`: nucleo.
- `servicios/servicios_ingrediente.py`: adaptadores.
