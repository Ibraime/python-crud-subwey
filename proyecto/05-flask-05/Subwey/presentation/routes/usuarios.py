from flask import (  # type: ignore  
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    flash,
    jsonify
) 

from Subwey.infrastructure.repositorio_usuario import (
    crear_servicio_usuario
)

from Subwey.infrastructure.errores import (
    UsuarioDuplicadoError,
    UsuarioEnUsoError
)

bp_usuarios = Blueprint(
    'usuarios',
    __name__,
    url_prefix='/usuarios'
)

servicio = crear_servicio_usuario()


def render_error(msg, code=400):

    titulos = {
        400: "400 — Error",
        404: "404 — No encontrado",
        409: "409 — Conflicto"
    }

    return render_template(
        "error.html",
        titulo=titulos.get(code, "Error"),
        msg=msg
    ), code


@bp_usuarios.route('/')
def listar():

    usuarios = servicio.listar_usuarios()

    return render_template(
        "lista_usuarios.html",
        usuarios=usuarios
    )

@bp_usuarios.route('/nuevo', methods=['GET', 'POST'])
def crear():

    error = None

    if request.method == 'POST':

        nombre = request.form['nombre']

        try:

            servicio.crear_usuario(nombre)

            flash("Usuario creado correctamente.", "exito")

            return redirect(
                url_for('usuarios.listar')
            )

        except UsuarioDuplicadoError as e:
            error = str(e)

        except ValueError as e:
            error = str(e)

        return render_template(
            "form_usuario.html",
            editar=False,
            nombre=nombre,
            error=error
        )

    return render_template(
        "form_usuario.html",
        editar=False,
        nombre="",
        error=None
    )


@bp_usuarios.route('/<nombre>/editar', methods=['GET', 'POST'])
def modificar(nombre):

    error = None

    if request.method == 'POST':

        nuevo_nombre = request.form['nombre']

        try:

            servicio.actualizar_usuario(
                nombre,
                nuevo_nombre
            )

            flash("Usuario actualizado correctamente.", "exito")

            return redirect(
                url_for('usuarios.listar')
            )

        except UsuarioDuplicadoError as e:
            error = str(e)

        except ValueError as e:
            error = str(e)

        return render_template(
            "form_usuario.html",
            editar=True,
            nombre=nuevo_nombre,
            error=error
        )

    return render_template(
        "form_usuario.html",
        editar=True,
        nombre=nombre,
        error=None
    )

@bp_usuarios.route('/<nombre>/eliminar', methods=['GET', 'POST'])
def eliminar(nombre):

    if request.method == 'POST':
        try:
            servicio.eliminar_usuario(nombre)

            flash(f"Usuario {nombre} eliminado.", "info")

            return redirect(url_for('usuarios.listar'))

        except UsuarioEnUsoError as e:
            return render_error(str(e), 409)

        except ValueError as e:
            return render_error(str(e), 404)

    return render_template(
        "confirmar_eliminar.html",
        nombre=nombre,
        url=url_for('usuarios.listar')
    )

@bp_usuarios.route('/api')
def api_usuarios():

    usuarios = servicio.listar_usuarios()

    return jsonify([
        {
            "nombre": u.nombre
        }
        for u in usuarios
    ])


@bp_usuarios.route('/api/<nombre>')
def api_usuario(nombre):

    usuarios = servicio.listar_usuarios()

    usuario = next(
        (u for u in usuarios if u.nombre == nombre),
        None
    )

    if usuario is None:
        return jsonify({
            "error": "Usuario no encontrado"
        }), 404

    return jsonify({
        "nombre": usuario.nombre
    })