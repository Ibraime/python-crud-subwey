# Sistema de Gestión de Ingredientes Subwey

Este proyecto es una **aplicación de consola desarrollada en Python** que permite gestionar el inventario de ingredientes de un restaurante de tipo *"subway"*. El sistema está orientado a realizar operaciones básicas de administración de stock de ingredientes mediante un menú interactivo.

La aplicación implementa operaciones **CRUD** (Crear, Leer, Actualizar y Eliminar), un control simple pero efectivo de los ingredientes disponibles, su precio y la cantidad en stock.

---

## 🧩 Funcionalidades

- **Registrar ingrediente**  
  Permite añadir un nuevo ingrediente indicando su nombre, precio y cantidad inicial.

- **Consumir ingrediente**  
  Reduce la cantidad disponible de un ingrediente cuando se utiliza en una preparación.

- **Reponer ingrediente**  
  Incrementa el stock de un ingrediente existente.

- **Eliminar ingrediente**  
  Elimina completamente un ingrediente del sistema.

- **Listar ingredientes**  
  Muestra todos los ingredientes registrados junto con su precio y cantidad actual. (Por defecto se crean 3 ingredientes, para probar más rápido)

---

## ▶️ Ejemplo de uso

Para ejecutar la aplicación desde la raíz del proyecto:

```bash
python -m Subwey.frontend.menu_ingredientes
```

### Ejemplo salida del programa

```text
=== SUBWEY ===
1. Registrar ingrediente
2. Consumir ingrediente
3. Reponer ingrediente
4. Eliminar ingrediente
5. Listar ingredientes
6. Salir
Elige una opción: 5

Listado de ingredientes:

aguacate   - 7.00 € - 8.00  unidades
queso      - 2.00 € - 42.00 unidades
tomate     - 3.00 € - 20.00 unidades
```

---

## 🗂️ Estructura del proyecto

```text
proyecto/
├── Subwey/
│   ├── backend/
│   │   └── __init__.py
│   │   └── repositorio_ingrediente.py
│   ├── entidades/
│   │   └── __init__.py
│   │   └── ingrediente.py
│   ├── frontend/
│   │   └── __init__.py
│   │   └── menu_ingredientes.py
│   ├── servicios/
│   │   └── __init__.py
│   │   └── servicios_ingrediente.py
└── README.md
```

### Descripción de carpetas

- **backend/**  
  Se encarga de la persistencia y gestión de los datos de los ingredientes.

- **entidades/**  
  Contiene las entidades de la base de datos, como `Ingrediente`, que es la base del sistema que usamos como ejemplo en esta ocasión.

- **frontend/**  
  Maneja la interacción con el usuario mediante un menú en consola.

- **servicios/**  
  Implementa la lógica del programa, coordinando las operaciones entre el frontend y el backend.

---