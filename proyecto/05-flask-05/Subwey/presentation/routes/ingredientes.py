from flask import Blueprint, render_template, redirect, request, url_for, flash, jsonify  # type: ignore

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
        titulo="400 — Error",
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
        
        flash(f"Se aumentó la cantidad del ingrediente {nombre}.", "exito")

        return redirect(
            url_for('ingredientes.detalle', nombre=nombre)
        )

    except ValueError as e:
        return render_error(str(e), 400)


@bp_ingredientes.route('/<nombre>/consumir/<int:cantidad>')
def consumir(nombre, cantidad):
    try:
        servicio.consumir_ingrediente(nombre, cantidad)
        
        flash(f"Se decrementó la cantidad del ingrediente {nombre}.", "exito")

        return redirect(
            url_for('ingredientes.detalle', nombre=nombre)
        )

    except ValueError as e:
        return render_error(str(e), 400)


@bp_ingredientes.route('/nuevo', methods=['GET', 'POST'])
def crear():

    error = None

    if request.method == 'POST':

        nombre = request.form['nombre']
        precio = float(request.form['precio'])
        stock = int(request.form['stock'])

        try:
            servicio.registrar_ingrediente(nombre, precio, stock)

            flash(f"Ingrediente {nombre} creado correctamente.", "exito")

            return redirect(
                url_for('ingredientes.listar')
            )

        except IngredienteDuplicadoError as e:
            error = str(e)

        except ValueError as e:
            error = str(e)

        return render_template(
            "form_ingrediente.html",
            nombre=nombre,
            precio=precio,
            stock=stock,
            error=error
        )

    return render_template(
        "form_ingrediente.html",
        nombre="",
        precio=0.0,
        stock=0,
        error=None
    )

@bp_ingredientes.route('/<nombre>/eliminar', methods=['GET', 'POST'])
def eliminar(nombre):

    if request.method == 'POST':
        try:
            servicio.eliminar_ingrediente(nombre)

            flash(f"Ingrediente {nombre} eliminado.", "info")

            return redirect(
                url_for('ingredientes.listar')
            )

        except IngredienteEnUsoError as e:
            return render_error(str(e), 409)

        except ValueError as e:
            return render_error(str(e), 404)

    return render_template(
        "confirmar_eliminar.html",
        nombre=nombre,
        url=url_for('ingredientes.listar')
    )

@bp_ingredientes.route('/api')
def api_ingredientes():

    ingredientes = servicio.listar_ingredientes()

    data = []

    for nombre, precio, stock in ingredientes:

        data.append({
            "nombre": nombre,
            "precio": precio,
            "stock": stock
        })

    return jsonify(data)

@bp_ingredientes.route('/api/<nombre>')
def api_ingrediente(nombre):

    ing = servicio.buscar_por_nombre(nombre)

    if ing is None:
        return jsonify({
            "error": "Ingrediente no encontrado"
        }), 404

    return jsonify({
        "nombre": ing.nombre,
        "precio": ing.precio,
        "stock": ing.stock
    })