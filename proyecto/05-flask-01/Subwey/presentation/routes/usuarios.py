from flask import Blueprint, render_template # type: ignore

bp_usuarios = Blueprint('usuarios', __name__, url_prefix='/usuarios')


@bp_usuarios.route('/')
def listar():
    content = """
        <h2>👤 Usuarios</h2>

        <p>Este módulo está en construcción</p>

        <ul>
            <li>Usuario 1 (placeholder)</li>
            <li>Usuario 2 (placeholder)</li>
        </ul>

        <a class="btn btn-secondary" href="/">Inicio</a>
    """

    return render_template("base.html", content=content)