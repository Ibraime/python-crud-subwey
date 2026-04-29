from flask import Blueprint, render_template # type: ignore

bp_bocadillos = Blueprint('bocadillos', __name__, url_prefix='/bocadillos')


@bp_bocadillos.route('/')
def listar():
    content = """
        <h2>🥪 Bocadillos</h2>

        <p>Este módulo está en construcción</p>

        <ul>
            <li>Bocadillo 1 (placeholder)</li>
            <li>Bocadillo 2 (placeholder)</li>
        </ul>

        <a class="btn btn-secondary" href="/">Inicio</a>
    """

    return render_template("base.html", content=content)


@bp_bocadillos.route('/<id>')
def detalle(id):
    content = f"""
        <h2>Bocadillo {id}</h2>

        <p>Detalle en construcción</p>

        <a class="btn btn-secondary" href="/bocadillos">Volver</a>
    """

    return render_template("base.html", content=content)