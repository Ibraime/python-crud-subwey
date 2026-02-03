# REVISIÓN FASE 01

## RECOMENDACIONES / COMENTARIOS

- Proyecto demasiado básico en el que no se puede verificar algunos de los aspectos vistos en clase.

## ASPECTOS A CAMBIAR / AÑADIR

- Solo has creado una entidad para la aplicación, `Ingrediente`. No lo pone explícitamente en la checklist, pero en clase he indicado que el proyecto en esta fase debería tener, al menos 3 entidades creadas y al menos en una se debe aplicar herencia.
- También debes usar otros aspectos de la POO que hemos visto en clase, por ejemplo usar decoradores para getters y setters.
- La capa de aplicación debería usarse solo para orquestar y como mucho para validar las entradas de los usuarios. En tu caso en la capa de aplicación estás creando objetos y almacenandolos en el repositorio cuando simplemente deberías pasar los datos de entrada al dominio para que este se encargue de aplicar lógica de negocio.
- Debería haber una clase para gestionar todos los ingredientes. Esta debería incluir el repositorio en memoria para guardar todos los ingredientes. De dicha clase debería existir un contrato para las operaciones de almacenar en el repositorio la lista de ingredientes.
