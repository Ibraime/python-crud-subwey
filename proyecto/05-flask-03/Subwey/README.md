# Sistema de Gestión de Ingredientes Subwey

Este proyecto es una **aplicación web desarrollada en Python con Flask** que permite gestionar el inventario de ingredientes de un restaurante de tipo *"subway"*. El sistema está orientado a realizar operaciones básicas de administración de stock de ingredientes mediante un menú interactivo.

La aplicación implementa operaciones **CRUD** (Crear, Leer, Actualizar y Eliminar), un control simple pero efectivo de los ingredientes disponibles, su precio y la cantidad en stock.
Así como crear varios bocadillos con distintas combinaciones de los mismos.

---

## Requisitos mínimos

- **Python**
  Necesario para usar el comando python -m para ejecutar el programa. Probado con la versión 3.13.7 (64 bit) 

---

## 🧩 Funcionalidades

- **Registrar ingrediente**  
  Permite añadir un nuevo ingrediente indicando su nombre, precio y cantidad inicial.

- **Reponer y consumir ingrediente**  
  Incrementa o decrementa el stock de un ingrediente existente.

- **Registrar bocadillo**  
  Permite crear un bocadillo indicando su nombre, lista de ingredientes y su autor (el precio se calcula con la suma de los ingredientes).
  También se puede crear uno de promoción que tendrá un porcentaje de descuento.


- **Modificar ingredientes del bocadillo**  
  Como su nombre indica permite cambiar los ingredientes del bocadillo, también modificar el descuento o quitarlo.

- **Eliminar un ingrediente/bocadillo/usuario**  
  Elimina un ingrediente/bocadillo/usuario de la base de datos.

---

## ▶️ Ejemplo de uso

Primero preparamos el entorno para no falten dependencias

```bash
cd Subwey
python -m venv .venv
.venv/Scripts/activate               # GitBash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass #Si da error de UnauthorizedAcess en PowerShell
.venv/Scripts/Activate.ps1           # PowerShell
pip install -r requirements.txt
cd ..
```

Segundo hay que usar el script de crear_bd para asegurar que la base de datos tiene los datos iniciales

```bash
python -m crear_bd.py  
```

Para ejecutar la aplicación desde la raíz del proyecto (Desde la carpeta padre de Subwey (05-flask-01, en adelante)):

```bash
python -m Subwey.presentation.app
```

### Ejemplo salida del programa

Al ejecutarlo nos dará una url, con la que podemos ver la página en el nuestro navegador

```bash
 * Running on http://127.0.0.1:5000
```

## Alternativamente se puede testear con el menú en consola
```bash
python -m Subwey.presentation.menu_ingredientes
```

### Ejemplo salida del menú

```
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
pan        - 1.50 € - 10.00 unidades
queso      - 2.00 € - 42.00 unidades
tomate     - 3.00 € - 20.00 unidades
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
│   │   └── repositorio_usuario.py
│   │   └── errores.py
│   ├── domain/
│   │   └── __init__.py
│   │   └── ingrediente.py
│   │   └── bocadillo.py
│   │   └── usuario.py
│   ├── presentation/
│   │   └── __init__.py
│   │   └── menu_ingredientes.py
│   │   └── menu_bocadillos.py
│   │   └── app.py
│   │   ├── routes/
│   │   │   └── __init__.py
│   │   │   └── ingredientes.py
│   │   │   └── bocadillos.py
│   │   │   └── usuarios.py
│   │   └── templates/
│   │       └── __init__.py
│   │       └── base.html
│   ├─── application/
│   │   └── __init__.py
│   │   └── servicios_ingrediente.py
│   │   └── servicios_bocadillo.py
│   │   └── servicios_usuario.py
│   └─── tests/...
└── README.md
```

### Descripción de carpetas

- **infrastructure/**  
  Se encarga de la persistencia, gestión y verificación de los datos de los ingredientes y bocadillos.

- **domain/**  
  Contiene las entidades de la base de datos, como `Ingrediente`, `Bocadillo` y `Usuario`, son la base del sistema que usamos como ejemplo (Sin incluir cesta de la compra y demás).

- **presentation/**  
  Maneja la interacción con el usuario mediante la interfaz de la aplicación web.

- **application/**  
  Implementa la lógica del programa, coordinando las operaciones entre el presentation e infrastructure.

- **tests/**  
  Para comprobar rapidamente que todo sigue funcionando, en caso de modificar algo por error

---