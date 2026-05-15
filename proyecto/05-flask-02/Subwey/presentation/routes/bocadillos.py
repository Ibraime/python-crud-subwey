from flask import Blueprint, render_template, request, redirect, url_for

from Subwey.infrastructure.repositorio_bocadillo import RepositorioBocadillo
from Subwey.infrastructure.repositorio_usuario import RepositorioUsuario
from Subwey.infrastructure.repositorio_ingrediente import crear_servicio_ingrediente

from Subwey.domain.usuario import Usuario
from Subwey.domain.ingrediente import Ingrediente

from Subwey.infrastructure.errores import (
    BocadilloDuplicadoError
)

bp_bocadillos = Blueprint('bocadillos', __name__, url_prefix='/bocadillos')

repo_bocadillo = RepositorioBocadillo()
repo_usuario = RepositorioUsuario()
servicio_ingrediente = crear_servicio_ingrediente()


def render_error(msg, code=400):
    content = f"""
        <h2>⚠️ Error</h2>
        <p>{msg}</p>
        <a class="btn btn-secondary" href="javascript:history.back()">Volver</a>
    """
    return render_template("base.html", content=content), code


# =========================
# LISTAR
# =========================
@bp_bocadillos.route('/')
def listar():
    bocadillos = repo_bocadillo.listar()

    def cortar_texto(texto, limite=50):
        if len(texto) <= limite:
            return texto
        return texto[:limite].rstrip() + "..."

    content = "<h2>🥪 Bocadillos</h2><ul>"

    for b in bocadillos:
        titulo = b.nombre

        # mostrar promo en el título
        if b.es_promocional():
            titulo += f" 🏷️ ({b.descuento}%)"

        ingredientes_txt = ", ".join(i.nombre for i in b.ingredientes)
        ingredientes_txt = cortar_texto(ingredientes_txt, 60)

        content += f"""
        <li class="boc-item">

            <div class="boc-info">

                <div class="boc-title">
                    {titulo}
                </div>

                <div class="boc-sub">
                    👤 {b.autor.nombre} · 💰 {b.precio:.2f}€ <br> 🥬 {ingredientes_txt}
                </div>

            </div>

            <div class="boc-actions">
                <a class="btn" href="/bocadillos/{b.nombre}">ver</a>
                <a class="btn btn-danger" href="/bocadillos/{b.nombre}/eliminar">eliminar</a>
            </div>

        </li>
        """

    content += """
    </ul>

    <div class="center">
        <a class="btn" href="/bocadillos/nuevo/">Crear bocadillo</a>
        <a class="btn btn-secondary" href="/">Inicio</a>
    </div>
    """

    return render_template("base.html", content=content)


# =========================
# CREAR
# =========================

@bp_bocadillos.route('/nuevo/<nombre>', methods=['GET', 'POST'])
def crear(nombre):
    usuarios = repo_usuario.listar()
    ingredientes = servicio_ingrediente.listar_ingredientes()

    if request.method == 'POST':
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

    ingredientes_html = "".join([
        f"""
        <label class="ing-box">
            <input type="checkbox" name="ingredientes" value="{i[0]}">
            <span>{i[0]}</span>
        </label>
        """
        for i in ingredientes
    ])

    content = f"""
        <h2>Nuevo bocadillo</h2>

        <form method="post">

            <p>Nombre:</p>
            <input value="{nombre}" disabled>

            <p>Usuario:</p>
            <select name="usuario">
                {''.join([f"<option value='{u.nombre}'>{u.nombre}</option>" for u in usuarios])}
            </select>

            <p>Ingredientes:</p>

            <div class="ing-grid">
                {ingredientes_html}
            </div>

            <p>Promoción:</p>
            <input type="checkbox" name="promo">

            <p>Descuento (%): <span id="val">10</span></p>

            <input type="range"
                name="descuento"
                min="1"
                max="90"
                value="10"
                oninput="document.getElementById('val').innerText = this.value">

            <br><br>

            <button class="btn">Crear</button>

        </form>

        <div class="center">
            <a class="btn btn-secondary" href="/bocadillos">Volver</a>
        </div>
    """

    return render_template("base.html", content=content)

# =========================
# DETALLE
# =========================
@bp_bocadillos.route('/<nombre>')
def detalle(nombre):
    bocadillo = repo_bocadillo.obtener_por_nombre(nombre)

    if bocadillo is None:
        return render_error("Bocadillo no encontrado", 404)

    ingredientes = ", ".join(i.nombre for i in bocadillo.ingredientes)

    promo_html = ""
    if bocadillo.es_promocional():
        promo_html = f"<p>🏷️ Promo: {bocadillo.descuento}%</p>"

    content = f"""
        <h2>{bocadillo.nombre}</h2>

        <p>👤 {bocadillo.autor.nombre}</p>
        <p>🥬 {ingredientes}</p>
        <p>💰 {bocadillo.precio:.2f}€</p>

        {promo_html}

        <div class="center">
            <a class="btn" href="/bocadillos/{nombre}/editar">Editar</a>
            <a class="btn btn-secondary" href="/bocadillos">Volver</a>
        </div>
    """

    return render_template("base.html", content=content)


# =========================
# EDITAR
# =========================
@bp_bocadillos.route('/<nombre>/editar', methods=['GET', 'POST'])
def editar(nombre):
    bocadillo = repo_bocadillo.obtener_por_nombre(nombre)

    if bocadillo is None:
        return render_error("Bocadillo no existe", 404)

    ingredientes = servicio_ingrediente.listar_ingredientes()

    if request.method == 'POST':
        ingredientes_sel = request.form.getlist('ingredientes')

        if not ingredientes_sel:
            return render_error("Debes seleccionar al menos un ingrediente", 400)

        ingredientes_obj = [
            Ingrediente(n, p, s)
            for n, p, s in ingredientes
            if n in ingredientes_sel
        ]

        repo_bocadillo.modificar_ingredientes(nombre, ingredientes_obj)

        promo = request.form.get("promo")
        descuento = int(request.form.get("descuento") or 10)
        descuento = max(1, min(90, descuento))

        conn = repo_bocadillo._conectar()

        if promo:
            conn.execute("""
                UPDATE bocadillos
                SET es_promocion = 1, descuento = ?
                WHERE nombre = ?
            """, (descuento, nombre))
        else:
            conn.execute("""
                UPDATE bocadillos
                SET es_promocion = 0, descuento = 0
                WHERE nombre = ?
            """, (nombre,))

        if not repo_bocadillo._conn:
            conn.commit()

        return redirect(url_for('bocadillos.detalle', nombre=nombre))

    ingredientes_actuales = [i.nombre for i in bocadillo.ingredientes]

    ingredientes_html = "".join([
        f"""
        <label class="ing-box">
            <input type="checkbox" name="ingredientes" value="{i[0]}"
            {"checked" if i[0] in ingredientes_actuales else ""}>
            <span>{i[0]}</span>
        </label>
        """
        for i in ingredientes
    ])

    promo_checked = "checked" if bocadillo.es_promocional() else ""
    descuento_val = bocadillo.descuento if bocadillo.es_promocional() else 10

    content = f"""
        <h2>Editar {bocadillo.nombre}</h2>

        <form method="post">

            <p>Ingredientes:</p>
            <div class="ing-grid">
                {ingredientes_html}
            </div>

            <p>Promoción:</p>
            <input type="checkbox" name="promo" {promo_checked}>

            <p>Descuento (%): <span id="val">{descuento_val}</span></p>

            <input type="range"
                name="descuento"
                min="1"
                max="90"
                value="{descuento_val}"
                oninput="document.getElementById('val').innerText = this.value">

            <br><br>
            <button class="btn">Guardar</button>
        </form>

        <div class="center">
            <a class="btn btn-secondary" href="/bocadillos/{nombre}">Volver</a>
        </div>
    """

    return render_template("base.html", content=content)


# =========================
# ELIMINAR
# =========================
@bp_bocadillos.route('/<nombre>/eliminar')
def eliminar(nombre):
    try:
        repo_bocadillo.eliminar(nombre)
        return redirect(url_for('bocadillos.listar'))

    except ValueError as e:
        return render_error(str(e), 404)