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

from flask import Flask, render_template, request  # type: ignore

from Subwey.presentation.routes.ingredientes import bp_ingredientes
from Subwey.presentation.routes.bocadillos import bp_bocadillos
from Subwey.presentation.routes.usuarios import bp_usuarios

import logging

app = Flask(__name__)

app.secret_key = 'clave-placeholder-717'

logging.basicConfig(
    filename='subwey.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
)


@app.before_request
def log_peticion():
    app.logger.info(f"{request.method} {request.path}")


@app.route('/')
def home():

    return render_template("home.html")


@app.route('/ayuda')
def ayuda():

    rutas = []

    for regla in app.url_map.iter_rules():

        if regla.endpoint != 'static':

            rutas.append({
                "ruta": regla.rule,
                "endpoint": regla.endpoint
            })

    return render_template(
        "ayuda.html",
        rutas=rutas
    )


@app.errorhandler(404)
def no_encontrado(e):
    
    return render_template(
        "error.html",
        titulo="404 — No encontrado",
        msg="La página solicitada no existe."
    ), 404


@app.errorhandler(500)
def error_servidor(e):

    return render_template(
        "error.html",
        titulo="500 — Error del servidor",
        msg="Ha ocurrido un error interno."
    ), 500


app.register_blueprint(bp_ingredientes)
app.register_blueprint(bp_bocadillos)
app.register_blueprint(bp_usuarios)


if __name__ == '__main__':
    app.run(debug=True)