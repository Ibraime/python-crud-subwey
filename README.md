# PROYECTO. Sistema de Bocadillos Personalizados tipo Subway

## Descripción general

El proyecto consiste en el diseño y desarrollo de un sistema para la gestión de una tienda de bocadillos personalizados,
inspirada en el modelo de Subway, donde los clientes pueden crear bocadillos a partir de ingredientes a elección.

El sistema controla el stock y el precio de cada ingrediente, calcula el precio final del bocadillo, permite guardar
combinaciones personalizadas y gestiona la cesta de la compra, clientes y valoraciones.

---

## Objetivos

### Objetivo general
Desarrollar un sistema modular que permita gestionar la creación de bocadillos personalizados, el inventario de ingredientes,
las compras de clientes y la valoración de productos.

### Objetivos específicos

- Gestionar ingredientes con stock y precio.
- Permitir la creación de bocadillos personalizados.
- Calcular el precio final según los ingredientes seleccionados.
- Gestionar clientes y su historial de compras.
- Implementar una cesta de la compra.
- Guardar combinaciones personalizadas de bocadillos.
- Permitir valoraciones y reseñas de bocadillos.

---

## Entidades principales

### Ingredientes
- id
- nombre
- precio
- stock

### Bocadillos (tacos, croissant, hamburguesas)
- id
- nombre
- tipo de pan
- imagen (elegir entre unas por defecto)
- lista de ingredientes
- precio total
- creador (cliente)
- valoraciones

### Clientes
- id
- nombre
- password
- saldo
- historial de pedidos

### Cesta de la compra
- id
- cliente
- bocadillos añadidos
- precio total

### Valoraciones
- id
- cliente
- bocadillo
- recomendado (si-no)
- puntuación (1-5)
- comentario
- fecha

### Ofertas (Más adelante)
- id
- nombre
- imagen
- descripcion
- lista de bocadillos
- precio total

---

## Funcionalidades principales

### Gestión de ingredientes
- Alta, baja y modificación de ingredientes.
- Actualizar el stock automaticamente al realizar compras.
- Bloqueo de ingredientes sin stock.

### Creación de bocadillos
- Selección guiada de ingredientes.
- Validación de disponibilidad.
- Cálculo automático del precio final.
- Guardado de combinaciones personalizadas.

### Cesta y compra
- Añadir y eliminar bocadillos de la cesta.
- Visualización del precio total.
- Confirmación de compra.
- Actualización de stock tras el pago.

### Clientes
- Registro y autenticación.
- Historial de pedidos.
- Acceso a bocadillos personalizados guardados.

### Valoraciones
- Valorar bocadillos comprados.
- Mostrar puntuaciones medias.
- Opiniones visibles para otros clientes.

---

## Reglas de negocio

- No se pueden comprar bocadillos con ingredientes sin stock.
- El precio del bocadillo es la suma de sus ingredientes.
- Solo clientes registrados pueden valorar.

---

## Alcance del proyecto

### Incluye
- Gestión completa de bocadillos personalizados.
- Control de inventario y precios.
- Sistema de compra con cesta.
- Valoraciones de clientes.

### No incluye
- Pasarelas de pago reales.
- Gestión avanzada de usuarios con roles.
- Envíos a domicilio.
