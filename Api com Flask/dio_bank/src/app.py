from flask import Flask, url_for, request

app = Flask(__name__)


# rotas e endpoints
@app.route("/")
def home():
    return "<p>Início</p>"


@app.route("/olamundo")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bemvindo/<usuario>")
def bemvindo(usuario):
    return f"<p>Bem vindo {usuario}</p>"


@app.route("/projects/")
def projects():
    return "The project page"


@app.route("/about", methods=['GET', 'POST'])
def about():
    return "The about page"


with app.test_request_context():
    print(url_for("hello_world"))
    print(url_for("bemvindo", usuario="Skol"))
    print(url_for("projects"))
    print(url_for("about", next="/"))
