from flask import Flask, render_template_string # type: ignore
from Subwey.presentation.routes.ingredientes import bp_ingredientes
from Subwey.presentation.routes.bocadillos import bp_bocadillos
from Subwey.presentation.routes.usuarios import bp_usuarios

app = Flask(__name__)

@app.route('/')
def home():
    content = """
        <h1>🥪 Subwey</h1>

        <a class="btn" href="/ingredientes/">Ingredientes</a>
        <a class="btn" href="/bocadillos/">Bocadillos</a>
        <a class="btn" href="/usuarios/">Usuarios</a>
    """
    return render_template_string("base.html", content=content)

@app.errorhandler(404)
def no_encontrado(e):
    return (f"<h2>404 — No encontrado</h2><p>{e}</p>"
            f"<a href='/'>Volver</a>"), 404


@app.errorhandler(500)
def error_servidor(e):
    return ("<h2>500 — Error del servidor</h2>"
            "<p>Algo ha fallado. Prueba más tarde.</p>"
            "<a href='/'>Volver</a>"), 500

app.register_blueprint(bp_ingredientes)
app.register_blueprint(bp_bocadillos)
app.register_blueprint(bp_usuarios)

if __name__ == '__main__':
    app.run(debug=True)