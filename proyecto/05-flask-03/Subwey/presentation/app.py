# EQUIVALENCIA menu.py <-> app.py
#
# | menu_ingredientes.py y menu_bocadillos.py | app.py (Flask)                                                        |
# |-------------------------------------------|-----------------------------------------------------------------------|
# | if opcion == "1": registrar_ingrediente() | @app.route('/ingredientes/nuevo/<nombre>/<float:precio>/<int:stock>') |
# | if opcion == "2": consumir_ingrediente()  | @app.route('/ingredientes/<nombre>/consumir/<int:cantidad>')          |
# | if opcion == "3": reponer_ingrediente()   | @app.route('/ingredientes/<nombre>/reponer/<int:cantidad>')           |
# | if opcion == "4": eliminar_ingrediente()  | @app.route('/ingredientes/<nombre>/eliminar')                         |
# | if opcion == "5": listar_ingredientes()   | @app.route('/ingredientes/')                                          |
# |-------------------------------------------|-----------------------------------------------------------------------|
# | if opcion == "1": crear_bocadillo()       | @app.route('/bocadillos/nuevo')                                       |
# | if opcion == "2": modificar_bocadillo()   | @app.route('/bocadillos/<nombre>/editar')                             |
# | if opcion == "3": eliminar_bocadillo()    | @app.route('/bocadillos/<nombre>/eliminar')                           |
# | if opcion == "4": listar_bocadillos()     | @app.route('/bocadillos/eliminar/<codigo>')                           |
# | input("Código: ")                         | <codigo> en la URL                                                    |
# | print("X " + str(e))                      | return str(e), 4xx                                                    |
# | servicios                                 | (igual, sin cambios)                                                  |
#
# Solo se modificó este archivo
# Comprobado que el menú comparte la misma base de datos que la aplicación web

from flask import Flask, render_template_string, request # type: ignore
from Subwey.presentation.routes.ingredientes import bp_ingredientes
from Subwey.presentation.routes.bocadillos import bp_bocadillos
from Subwey.presentation.routes.usuarios import bp_usuarios

app = Flask(__name__)

@app.before_request
def log_peticion():
    app.logger.info(f"{request.method} {request.path}")

BASE_HTML = """
<!doctype html>
<html>
<head>
<meta charset="utf-8">

<style>
body {
    font-family: Arial;
    background: #f4f6f8;
    display: flex;
    justify-content: center;
    margin: 0;
}

.container {
    width: 750px;
    margin-top: 40px;
    background: white;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    text-align: center;
}

.btn {
    display: inline-block;
    padding: 10px 15px;
    margin: 5px;
    background: #007bff;
    color: white;
    text-decoration: none;
    border-radius: 6px;
}
</style>

</head>

<body>
<div class="container">
{{ content | safe }}
</div>
</body>
</html>
"""

@app.route('/')
def home():
    content = """
        <h1>🥪 Subwey</h1>

        <a class="btn" href="/ingredientes/">Ingredientes</a>
        <a class="btn" href="/bocadillos/">Bocadillos</a>
        <a class="btn" href="/usuarios/">Usuarios</a>
    """
    return render_template_string(BASE_HTML, content=content)

@app.errorhandler(404)
def no_encontrado(e):
    return (f"<h2>404 — No encontrado</h2><p>{e}</p>"
            f"<a href='/'>Volver</a>"), 404


@app.errorhandler(500)
def error_servidor(e):
    return ("<h2>500 — Error del servidor</h2>"
            "<p>Algo ha fallado. Prueba más tarde.</p>"
            "<a href='/'>Volver</a>"), 500

@app.route('/ayuda')
def ayuda():
    lineas = ['<h2>Rutas disponibles</h2><ul>']
    for regla in app.url_map.iter_rules():
        if regla.endpoint != 'static':
            lineas.append(
                f"<li><code>{regla.rule}</code> — {regla.endpoint}</li>"
            )
    lineas.append('</ul>')
    return '\n'.join(lineas)

import logging

logging.basicConfig(
    filename='subwey.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
)



app.register_blueprint(bp_ingredientes)
app.register_blueprint(bp_bocadillos)
app.register_blueprint(bp_usuarios)

if __name__ == '__main__':
    app.run(debug=True)