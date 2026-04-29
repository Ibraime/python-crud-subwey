from flask import Blueprint, render_template, redirect, url_for # type: ignore
from Subwey.infrastructure.repositorio_usuario import crear_servicio_usuario
from Subwey.infrastructure.errores import UsuarioDuplicadoError

bp_usuarios = Blueprint('usuarios', __name__, url_prefix='/usuarios')

servicio = crear_servicio_usuario()


@bp_usuarios.route('/')
def listar():
    usuarios = servicio.listar_usuarios()

    content = "<h2>👤 Usuarios</h2><ul>"

    for u in usuarios:
        content += f"""
        <li>
            <span>{u.nombre}</span>
            <span>
                <a class="btn" href="{u.nombre}/editar/demo_modificado">modificar</a>
                <a class="btn btn-danger" href="{u.nombre}/eliminar">eliminar</a>
            </span>
        </li>
        """

    content += "</ul>"

    content += """
        <div class="center">
            <a class="btn" href="/usuarios/nuevo/demo">crear usuario demo</a>
            <a class="btn btn-secondary" href="/">Inicio</a>
        </div>
    """

    return render_template("base.html", content=content)


@bp_usuarios.route('/nuevo/<nombre>')
def crear(nombre):
    try:
        servicio.crear_usuario(nombre)
        return redirect(url_for('usuarios.listar'))
    except UsuarioDuplicadoError as e:
        return render_template("base.html", content=f"""
            <h2>⚠️ Error</h2>
            <p>{e}</p>
            <a class="btn btn-secondary" href="/usuarios">Volver</a>
        """)


@bp_usuarios.route('/<nombre>/eliminar')
def eliminar(nombre):
    servicio.eliminar_usuario(nombre)
    return redirect(url_for('usuarios.listar'))


@bp_usuarios.route('/<antiguo>/editar/<nuevo>')
def modificar(antiguo, nuevo):
    servicio.actualizar_usuario(antiguo, nuevo)
    return redirect(url_for('usuarios.listar'))