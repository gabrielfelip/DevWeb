from flask import Flask

app = Flask("__name__")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quemsomos.html")
def quemsomos():
    return render_template("quemsomos.html")

@app.route("/contatos.html")
def contatos():
    return render_template("contatos.html")

