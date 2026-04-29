from flask import Flask, render_template_string # type: ignore
from Subwey.presentation.routes.ingredientes import bp_ingredientes
from Subwey.presentation.routes.bocadillos import bp_bocadillos
from Subwey.presentation.routes.usuarios import bp_usuarios

app = Flask(__name__)

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


app.register_blueprint(bp_ingredientes)
app.register_blueprint(bp_bocadillos)
app.register_blueprint(bp_usuarios)

if __name__ == '__main__':
    app.run(debug=True)