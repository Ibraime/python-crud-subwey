from flask import Blueprint, render_template, redirect, url_for  # type: ignore

from Subwey.infrastructure.repositorio_usuario import (
    crear_servicio_usuario
)

from Subwey.infrastructure.errores import (
    UsuarioDuplicadoError
)

bp_usuarios = Blueprint(
    'usuarios',
    __name__,
    url_prefix='/usuarios'
)

servicio = crear_servicio_usuario()


def render_error(msg, code=400):
    return render_template(
        "error.html",
        titulo="400 — Error",
        msg=msg
    ), code


@bp_usuarios.route('/')
def listar():
    usuarios = servicio.listar_usuarios()

    return render_template(
        "lista_usuarios.html",
        usuarios=usuarios
    )


@bp_usuarios.route('/nuevo/<nombre>')
def crear(nombre):
    try:
        servicio.crear_usuario(nombre)

        return redirect(
            url_for('usuarios.listar')
        )

    except UsuarioDuplicadoError as e:
        return render_error(str(e), 409)

    except ValueError as e:
        return render_error(str(e), 400)


@bp_usuarios.route('/<nombre>/eliminar')
def eliminar(nombre):
    try:
        servicio.eliminar_usuario(nombre)

        return redirect(
            url_for('usuarios.listar')
        )

    except ValueError as e:
        return render_error(str(e), 404)


@bp_usuarios.route('/<antiguo>/editar/<nuevo>')
def modificar(antiguo, nuevo):
    try:
        servicio.actualizar_usuario(
            antiguo,
            nuevo
        )

        return redirect(
            url_for('usuarios.listar')
        )

    except UsuarioDuplicadoError as e:
        return render_error(str(e), 409)

    except ValueError as e:
        return render_error(str(e), 400)