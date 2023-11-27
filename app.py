import mysql.connector

app = Flask("__name__")

db = mysql.connector.connect(
host = 'localhost',
user = 'root',
password = 'INSERIR_SENHA',
database = 'desafio04'
)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quemsomos")
def quemsomos():
    return render_template("quemsomos.html")

@app.route("/minhasconexoes")
def contatos():
    return render_template("minhasconexoes.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        cur = db.cursor(buffered=True)
        cur.execute('INSERT INTO LOGIN (EMAIL, SENHA) VALUES  (%,%,%)', (email, senha))

        db.commit()

        cur.close()

        return 'Sucesso'
    
     return render_template("login.html")


@app.route('/users')
def users():
    cur = db.cursor(buffered=True)

    users = cur.execute("select * from login")

    userDetails = cur.fetchall()

    return render_template("users.html", userDetails=userDetails)
