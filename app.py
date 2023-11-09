from flask import Flask, render_template

app = Flask("__name__")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quemsomos")
def quemsomos():
    return render_template("quemsomos.html")

@app.route("/minhasconexoes")
def contatos():
    return render_template("minhasconexoes.html")

@app.route("/login")
def login():
    return render_template("login.html")