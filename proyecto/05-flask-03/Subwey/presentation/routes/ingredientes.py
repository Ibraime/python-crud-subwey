from flask import Blueprint, render_template, redirect, url_for  # type: ignore

from Subwey.infrastructure.repositorio_ingrediente import (
    crear_servicio_ingrediente
)

from Subwey.infrastructure.errores import (
    IngredienteEnUsoError,
    IngredienteDuplicadoError
)

bp_ingredientes = Blueprint(
    'ingredientes',
    __name__,
    url_prefix='/ingredientes'
)

servicio = crear_servicio_ingrediente()


def render_error(msg, code=400):
    return render_template(
        "error.html",
        msg=msg
    ), code


@bp_ingredientes.route('/')
def listar():
    ingredientes = servicio.listar_ingredientes()

    return render_template(
        "lista_ingredientes.html",
        ingredientes=ingredientes
    )


@bp_ingredientes.route('/<nombre>')
def detalle(nombre):
    ing = servicio.buscar_por_nombre(nombre)

    if ing is None:
        return render_error("Ingrediente no encontrado", 404)

    return render_template(
        "detalles_ingrediente.html",
        ing=ing
    )


@bp_ingredientes.route('/<nombre>/reponer/<int:cantidad>')
def reponer(nombre, cantidad):
    try:
        servicio.reponer_ingrediente(nombre, cantidad)

        return redirect(
            url_for('ingredientes.detalle', nombre=nombre)
        )

    except ValueError as e:
        return render_error(str(e), 400)


@bp_ingredientes.route('/<nombre>/consumir/<int:cantidad>')
def consumir(nombre, cantidad):
    try:
        servicio.consumir_ingrediente(nombre, cantidad)

        return redirect(
            url_for('ingredientes.detalle', nombre=nombre)
        )

    except ValueError as e:
        return render_error(str(e), 400)


@bp_ingredientes.route('/nuevo/<nombre>/<float:precio>/<int:stock>')
def crear(nombre, precio, stock):
    try:
        servicio.registrar_ingrediente(
            nombre,
            precio,
            stock
        )

        return redirect(
            url_for('ingredientes.listar')
        )

    except IngredienteDuplicadoError as e:
        return render_error(str(e), 409)

    except ValueError as e:
        return render_error(str(e), 400)


@bp_ingredientes.route('/<nombre>/eliminar')
def eliminar(nombre):
    try:
        servicio.eliminar_ingrediente(nombre)

        return redirect(
            url_for('ingredientes.listar')
        )

    except IngredienteEnUsoError as e:
        return render_error(str(e), 409)

    except ValueError as e:
        return render_error(str(e), 404)