from flask import Blueprint, render_template, request, redirect, url_for

from Subwey.infrastructure.repositorio_bocadillo import RepositorioBocadillo
from Subwey.infrastructure.repositorio_usuario import RepositorioUsuario
from Subwey.infrastructure.repositorio_ingrediente import crear_servicio_ingrediente

from Subwey.domain.usuario import Usuario
from Subwey.domain.ingrediente import Ingrediente

from Subwey.infrastructure.errores import (
    BocadilloDuplicadoError
)

bp_bocadillos = Blueprint(
    'bocadillos',
    __name__,
    url_prefix='/bocadillos'
)

repo_bocadillo = RepositorioBocadillo()
repo_usuario = RepositorioUsuario()
servicio_ingrediente = crear_servicio_ingrediente()


def render_error(msg, code=400):
    return render_template(
        "error.html",
        msg=msg
    ), code


@bp_bocadillos.route('/')
def listar():

    bocadillos = repo_bocadillo.listar()

    return render_template(
        "lista_bocadillos.html",
        bocadillos=bocadillos
    )


@bp_bocadillos.route('/nuevo/', methods=['GET', 'POST'])
def crear():

    usuarios = repo_usuario.listar()
    ingredientes = servicio_ingrediente.listar_ingredientes()

    if request.method == 'POST':

        nombre = request.form['nombre']
        usuario_nombre = request.form['usuario']
        ingredientes_sel = request.form.getlist('ingredientes')

        promo = request.form.get("promo")

        descuento = int(request.form.get("descuento") or 10)
        descuento = max(1, min(90, descuento))

        if not ingredientes_sel:
            return render_error("Debes seleccionar al menos un ingrediente", 400)

        try:
            autor = Usuario(usuario_nombre)

            ingredientes_obj = [
                Ingrediente(n, p, s)
                for n, p, s in ingredientes
                if n in ingredientes_sel
            ]

            repo_bocadillo.guardar(
                nombre,
                ingredientes_obj,
                descuento=descuento if promo else None,
                autor=autor
            )

            return redirect(url_for('bocadillos.listar'))

        except BocadilloDuplicadoError as e:
            return render_error(str(e), 409)

        except ValueError as e:
            return render_error(str(e), 400)

    return render_template(
        "form_bocadillo.html",
        editar=False,
        usuarios=usuarios,
        ingredientes=ingredientes,
        ingredientes_actuales=[],
        promo=False,
        descuento=10
    )

@bp_bocadillos.route('/<nombre>')
def detalle(nombre):

    bocadillo = repo_bocadillo.obtener_por_nombre(nombre)

    if bocadillo is None:
        return render_error(
            "Bocadillo no encontrado",
            404
        )

    return render_template(
        "detalles_bocadillo.html",
        bocadillo=bocadillo
    )

@bp_bocadillos.route('/<nombre>/editar', methods=['GET', 'POST'])
def editar(nombre):

    bocadillo = repo_bocadillo.obtener_por_nombre(nombre)

    if bocadillo is None:
        return render_error(
            "Bocadillo no existe",
            404
        )

    ingredientes = servicio_ingrediente.listar_ingredientes()

    if request.method == 'POST':

        nuevo_nombre = request.form['nombre']

        ingredientes_sel = request.form.getlist(
            'ingredientes'
        )

        if not ingredientes_sel:
            return render_error(
                "Debes seleccionar al menos un ingrediente",
                400
            )

        ingredientes_obj = [
            Ingrediente(n, p, s)
            for n, p, s in ingredientes
            if n in ingredientes_sel
        ]

        promo = request.form.get("promo")

        descuento = int(
            request.form.get("descuento") or 10
        )

        descuento = max(1, min(90, descuento))

        try:

            repo_bocadillo.modificar(
                nombre_actual=nombre,
                nuevo_nombre=nuevo_nombre,
                ingredientes=ingredientes_obj,
                descuento=descuento if promo else None
            )

            return redirect(
                url_for(
                    'bocadillos.detalle',
                    nombre=nuevo_nombre
                )
            )

        except BocadilloDuplicadoError as e:
            return render_error(str(e), 409)

        except ValueError as e:
            return render_error(str(e), 400)

    ingredientes_actuales = [
        i.nombre for i in bocadillo.ingredientes
    ]

    descuento_val = (
        bocadillo.descuento
        if bocadillo.es_promocional()
        else 10
    )

    return render_template(
        "form_bocadillo.html",
        editar=True,
        nombre=nombre,
        ingredientes=ingredientes,
        ingredientes_actuales=ingredientes_actuales,
        promo=bocadillo.es_promocional(),
        descuento=descuento_val
    )

@bp_bocadillos.route('/<nombre>/eliminar')
def eliminar(nombre):

    try:

        repo_bocadillo.eliminar(nombre)

        return redirect(
            url_for('bocadillos.listar')
        )

    except ValueError as e:
        return render_error(str(e), 404)