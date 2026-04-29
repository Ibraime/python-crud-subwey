from flask import Blueprint, render_template, redirect, url_for # type: ignore
from Subwey.infrastructure.repositorio_ingrediente import crear_servicio_ingrediente
from Subwey.infrastructure.errores import IngredienteEnUsoError, IngredienteDuplicadoError

bp_ingredientes = Blueprint('ingredientes', __name__, url_prefix='/ingredientes')

servicio = crear_servicio_ingrediente()


def render_error(msg, code=400):
    content = f"""
        <h2>⚠️ Error</h2>
        <p>{msg}</p>

        <a class="btn btn-secondary" href="javascript:history.back()">Volver</a>
    """
    return render_template("base.html", content=content), code


@bp_ingredientes.route('/')
def listar():
    ingredientes = servicio.listar_ingredientes()

    content = "<h2>🧀 Ingredientes</h2><ul>"

    for n, p, s in ingredientes:
        content += f"""
        <li>
            <span>{n} — {p:.2f}€ — stock: {s}</span>
            <span>
                <a class="btn" href="{n}">ver</a>
                <a class="btn btn-danger" href="{n}/eliminar">eliminar</a>
            </span>
        </li>
        """

    content += "</ul>"

    content += """
        <div class="center">
            <a class="btn btn-secondary" href="/">Inicio</a>
            <a class="btn" href="/ingredientes/nuevo/pan/1.5/10">Crear ejemplo (pan)</a>
        </div>
    """

    return render_template("base.html", content=content)


@bp_ingredientes.route('/<nombre>')
def detalle(nombre):
    ing = servicio.buscar_por_nombre(nombre)

    if ing is None:
        return render_error("Ingrediente no encontrado", 404)

    content = f"""
        <h2>{ing.nombre}</h2>

        <p>💰 Precio: {ing.precio}€</p>
        <p>📦 Stock: {ing.stock}</p>

        <a class="btn" href="{nombre}/reponer/1">+1 stock</a>
        <a class="btn btn-danger" href="{nombre}/consumir/1">-1 stock</a>

        <div class="center">
            <a class="btn btn-secondary" href="/ingredientes">Volver</a>
        </div>
    """

    return render_template("base.html", content=content)


@bp_ingredientes.route('/<nombre>/reponer/<int:cantidad>')
def reponer(nombre, cantidad):
    try:
        servicio.reponer_ingrediente(nombre, cantidad)
        return redirect(url_for('ingredientes.detalle', nombre=nombre))
    except ValueError as e:
        return render_error(str(e), 400)


@bp_ingredientes.route('/<nombre>/consumir/<int:cantidad>')
def consumir(nombre, cantidad):
    try:
        servicio.consumir_ingrediente(nombre, cantidad)
        return redirect(url_for('ingredientes.detalle', nombre=nombre))
    except ValueError as e:
        return render_error(str(e), 400)
    
@bp_ingredientes.route('/nuevo/<nombre>/<float:precio>/<int:stock>')
def crear(nombre, precio, stock):
    try:
        servicio.registrar_ingrediente(nombre, precio, stock)
        return redirect(url_for('ingredientes.listar'))
    except IngredienteDuplicadoError as e:
        return render_error(str(e), 409)
    except ValueError as e:
        return render_error(str(e), 400)
    
@bp_ingredientes.route('/<nombre>/eliminar')
def eliminar(nombre):
    try:
        servicio.eliminar_ingrediente(nombre)
        return redirect(url_for('ingredientes.listar'))
    except IngredienteEnUsoError as e:
        return render_error(str(e), 409)
    except ValueError as e:
        return render_error(str(e), 404)