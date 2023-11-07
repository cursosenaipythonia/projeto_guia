from flask import Flask, flash, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from database import db

app = Flask(__name__)
app.config['SQLALCHEMY_BINDS'] = {'default': 'sqlite:///database.sqlite'}

db = SQLAlchemy()
db.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

app.config['SECRET_KEY'] = 'meu-banco-de-dados'
"""
# Create a flask app
app = Flask(
  __name__ ,
  template_folder='templates',
  static_folder='static'
)
"""


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/cadastro')
def cadastro():
  return render_template('cadastro.html')


@app.route('/guia')
def guia():
  return render_template('guia.html')


@app.route('/perfil', methods=['GET', 'POST'])
def perfil():
  if request.method == 'POST':
    genero = request.form.getlist('genero')
    classificacao = request.form['classificacao']
    avaliacao = request.form['avaliacao']

    perfil = Perfil(genero=genero,
                    classificacao=classificacao,
                    avaliacao=avaliacao)
    db_session.add(perfil)
    db_session.commit()

    return "Perfil cadastrado com sucesso!"

  return render_template('perfil.html')


#@app.route('/perfil')
#def perfil():
# return render_template('perfil.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    # Handle form submission
    email = request.form['email']
    password = request.form['password']
    # Do something with the username and password, like validation or authentication
    # Redirect to a different page or perform some action

  return render_template('login.html')


"""
@app.route('/criar_perfil', methods=['GET', 'POST'])
def criar_perfil():
    form = PreferencesForm()

    if form.validate_on_submit():
        genres = ','.join(form.genres.data)
        adult = form.adult.data
        ratings = ','.join(form.ratings.data)

        # Salvar as preferências no banco de dados
        user_preference = UserPreferences(user_id="user_id_do_usuario", genres=genres, adult=adult, ratings=ratings)
        db.session.add(user_preference)
        db.session.commit()

        return redirect('/guia')  # Redireciona para a página de recomendações

    return render_template('criar_perfil.html', form=form)

@app.route('/recomendacoes')
def recomendacoes():
    # Aqui você pode implementar seu algoritmo de recomendação
    # Use as preferências do usuário, consulte o banco de dados para obter filmes e aplique o algoritmo.

    # Retorna uma lista de filmes recomendados
    recommended_movies = ["Filme 1", "Filme 2", "Filme 3"]

    return render_template('guia.html', recommended_movies=recommended_movies)
"""

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
