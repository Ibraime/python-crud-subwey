# Arquitectura por capas

El proyecto ha sido estructurado usando el diseño por capas.

## Capas y responsabilidades
- presentation: entrada/salida por consola. No contiene reglas de negocio.
- application: orquesta casos de uso sobre el dominio.
- domain: Las distintas entidades.
- infrastructure: repositorios concretos, validaciones y datos iniciales.

## Dependencias permitidas
- presentation -> application -> infrastructure
- infrastructure -> domain

No se debe depender de presentation desde domain ni application.

## Mapa de archivos
- `presentation/menu_ingredientes.py`, `presentation/menu_bocadillo.py`: UI de consola.
- `domain/ingrediente.py`, `infrastructure/repositorio_ingredientes.py`: nucleo.
- `application/servicios_ingrediente.py`, `application/servicios_bocadillo.py`: adaptadores.
