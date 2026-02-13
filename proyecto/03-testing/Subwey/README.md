# Sistema de Gestión de Ingredientes Subwey

Este proyecto es una **aplicación de consola desarrollada en Python** que permite gestionar el inventario de ingredientes de un restaurante de tipo *"subway"*. El sistema está orientado a realizar operaciones básicas de administración de stock de ingredientes mediante un menú interactivo.

La aplicación implementa operaciones **CRUD** (Crear, Leer, Actualizar y Eliminar), un control simple pero efectivo de los ingredientes disponibles, su precio y la cantidad en stock.

---

## Requisitos mínimos

- **Python**
  Necesario para usar el comando python -m para ejecutar el programa. Probado con la versión 3.13.7 (64 bit) 


---

## 🧩 Funcionalidades

- **Registrar ingrediente**  
  Permite añadir un nuevo ingrediente indicando su nombre, precio y cantidad inicial.

- **Registrar bocadillo**  
  Permite crear un bocadillo indicando su nombre, lista de ingredientes y su autor (el precio se calcula con la suma de los ingredientes).

- **Consumir ingrediente**  
  Reduce la cantidad disponible de un ingrediente cuando se utiliza en una preparación.

- **Reponer ingrediente**  
  Incrementa el stock de un ingrediente existente.

- **Modificar ingredientes del bocadillo**  
  Como su nombre indica permite cambiar los ingredientes del bocadillo, borra los que tiene y empiezas a elegir de 0, si cancelas se
  queda como estaba.

- **Eliminar ingrediente/bocadillo**  
  Elimina un ingrediente/bocadillo de la lista.

- **Listar ingredientes**  
  Muestra todos los ingredientes registrados junto con su precio y cantidad actual. (Por defecto se crean 3 ingredientes, para probar más rápido)

- **Listar bocadillos**  
  Muestra todos los bocadillos registrados junto con su precio final, ingredientes y autor. (Por defecto se crean 2 bocadillos, para probar más rápido)

---

## ▶️ Ejemplo de uso

Para ejecutar la aplicación desde la raíz del proyecto (En este caso desde la carpeta padre de Subwey (01-capas, 02-documentando, 03-testing, etc)):

```bash
python -m Subwey.presentation.menu_ingredientes
```

### Ejemplo salida del programa

```text
=== SUBWEY (ingredientes) ===
1. Registrar ingrediente
2. Consumir ingrediente
3. Reponer ingrediente
4. Eliminar ingrediente
5. Listar ingredientes
6. Menú de bocadillos
7. Salir
Elige una opción: 5

Listado de ingredientes:

aguacate   - 7.00 € - 8.00  unidades
queso      - 2.00 € - 42.00 unidades
tomate     - 3.00 € - 20.00 unidades
```

```text
=== SUBWEY (bocadillos) ===
1. Registrar bocadillo
2. Modificar ingredientes del bocadillo
3. Eliminar bocadillo
4. Listar bocadillos
5. Volver a ingredientes
Elige una opción: 4

Listado de bocadillos:
              caprese          - 5.00 € - tomate, queso - Autor: Anónimo
              vegetal          - 10.00€ - tomate, aguacate - Autor: Anónimo
```

---

## 🗂️ Estructura del proyecto

```text
proyecto/
├── Subwey/
│   ├── infrastructure/
│   │   └── __init__.py
│   │   └── repositorio_ingrediente.py
│   │   └── repositorio_bocadillo.py
│   ├── domain/
│   │   └── __init__.py
│   │   └── ingrediente.py
│   │   └── bocadillo.py
│   │   └── usuario.py
│   ├── presentation/
│   │   └── __init__.py
│   │   └── menu_ingredientes.py
│   │   └── menu_bocadillos.py
│   └── application/
│       └── __init__.py
│       └── servicios_ingrediente.py
│       └── servicios_bocadillo.py
└── README.md
```

### Descripción de carpetas

- **infrastructure/**  
  Se encarga de la persistencia, gestión y verificación de los datos de los ingredientes y bocadillos.

- **domain/**  
  Contiene las entidades de la base de datos, como `Ingrediente`, `Bocadillo` y `Usuario`, son la base del sistema que usamos como ejemplo (Sin incluir cesta de la compra y demás).

- **presentation/**  
  Maneja la interacción con el usuario mediante dos menús en consola que se conectan entre ellos.

- **application/**  
  Implementa la lógica del programa, coordinando las operaciones entre el presentation e infrastructure.

---